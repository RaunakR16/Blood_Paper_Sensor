#include <Wire.h>

// AD5933 I2C address
#define SLAVE_ADDR 0x0D
#define ADDR_PTR 0xB0

// Register map
#define CTRL_REG      0x80
#define STATUS_REG    0x8F
#define START_FREQ_R1 0x82
#define START_FREQ_R2 0x83
#define START_FREQ_R3 0x84
#define RE_DATA_R1    0x94
#define RE_DATA_R2    0x95
#define IMG_DATA_R1   0x96
#define IMG_DATA_R2   0x97

// Constants
const float MCLK = 16.776e6;      // Internal clock frequency (Hz)
const float TEST_FREQ = 10e3;     // 10 kHz
const int SAMPLE_COUNT = 100;     // 100 samples

// Function declarations
void writeData(int addr, int data);
int readData(int addr);
byte getFrequency(float freq, int n);

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("AD5933 Single Frequency Test (10 kHz, 100 Samples)");

  // Reset and setup control
  writeData(CTRL_REG, 0x00);   // Clear control reg
  delay(10);

  // Program start frequency = 10 kHz
  writeData(START_FREQ_R1, getFrequency(TEST_FREQ, 1));
  writeData(START_FREQ_R2, getFrequency(TEST_FREQ, 2));
  writeData(START_FREQ_R3, getFrequency(TEST_FREQ, 3));

  // Set range and gain: Range 1, PGA x1
  writeData(CTRL_REG, 0x01);
  delay(10);
}

void loop() {
  short re, img;
  double mag, impedance;
  double gain = 5.677e-9; // example calibration constant, adjust for your setup

  Serial.println("Starting measurements...");

  for (int i = 0; i < SAMPLE_COUNT; i++) {
    // Initialize frequency
    writeData(CTRL_REG, (readData(CTRL_REG) & 0x07) | 0x10); // Init start freq
    writeData(CTRL_REG, (readData(CTRL_REG) & 0x07) | 0x20); // Start freq sweep (single point)

    // Wait for data ready
    while (!(readData(STATUS_REG) & 0x02));

    // Read real and imaginary data
    byte R1 = readData(RE_DATA_R1);
    byte R2 = readData(RE_DATA_R2);
    re = (R1 << 8) | R2;

    R1 = readData(IMG_DATA_R1);
    R2 = readData(IMG_DATA_R2);
    img = (R1 << 8) | R2;

    // Calculate magnitude and impedance
    mag = sqrt(pow((double)re, 2) + pow((double)img, 2));
    impedance = 1 / (gain * mag);

    // Print result
    Serial.print("Sample ");
    Serial.print(i + 1);
    Serial.print(": R=");
    Serial.print(re);
    Serial.print(" I=");
    Serial.print(img);
    Serial.print(" |Z|=");
    Serial.print(impedance / 1000.0, 4);
    Serial.println(" kΩ");

    delay(10); // small delay between samples (~100 Hz sample rate)
  }

  Serial.println("Measurement complete. Going to standby.");
  writeData(CTRL_REG, 0xA0); // Power down
  while (1);
}

// ------------------- Helper Functions -------------------

void writeData(int addr, int data) {
  Wire.beginTransmission(SLAVE_ADDR);
  Wire.write(addr);
  Wire.write(data);
  Wire.endTransmission();
  delay(1);
}

int readData(int addr) {
  int data;
  Wire.beginTransmission(SLAVE_ADDR);
  Wire.write(ADDR_PTR);
  Wire.write(addr);
  Wire.endTransmission();
  delay(1);
  Wire.requestFrom(SLAVE_ADDR, 1);
  if (Wire.available() >= 1) {
    data = Wire.read();
  } else {
    data = -1;
  }
  return data;
}

byte getFrequency(float freq, int n) {
  long val = long((freq / (MCLK / 4.0)) * pow(2, 27));
  byte code;
  switch (n) {
    case 1: code = (val >> 16) & 0xFF; break;
    case 2: code = (val >> 8) & 0xFF; break;
    case 3: code = val & 0xFF; break;
    default: code = 0; break;
  }
  return code;
}
