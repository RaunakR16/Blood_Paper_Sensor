#include <Wire.h>
#include "AD5933.h"

#define TEST_FREQ   (10000UL)   // 10 kHz
#define REF_RESIST  (10000.0)   // Known resistor 10kΩ
#define SAMPLE_COUNT 100

double gain = 0;
int phase = 0;
int realPart, imagPart;

void setup() {
  Serial.begin(115200);
  Wire.begin();

  Serial.println("AD5933 Single Frequency Measurement Started...");

  // Initialize the AD5933
  if (!(AD5933::reset() &&
        AD5933::setInternalClock(true) &&
        AD5933::setStartFrequency(TEST_FREQ) &&
        AD5933::setIncrementFrequency(0) &&
        AD5933::setNumberIncrements(0) &&
        AD5933::setPGAGain(PGA_GAIN_X1))) {
    Serial.println("Initialization FAILED!");
    while (1);
  }

  // --- Manual Calibration ---
  Serial.println("Calibrating manually...");
  AD5933::setControlMode(CTRL_INIT_START_FREQ);
  AD5933::setControlMode(CTRL_START_FREQ_SWEEP);
  delay(100);

  while (!(AD5933::readStatusRegister() & STATUS_DATA_VALID));

  AD5933::getComplexData(&realPart, &imagPart);

  double magnitude = sqrt(pow(realPart, 2) + pow(imagPart, 2));
  if (magnitude > 0) {
    gain = 1.0 / (magnitude * REF_RESIST);
    Serial.print("Manual calibration successful. Gain = ");
    Serial.println(gain, 10);
  } else {
    Serial.println("Manual calibration failed (invalid data).");
    while (1);
  }

  AD5933::setPowerMode(POWER_STANDBY);
  delay(200);
  Serial.println("Starting 100 samples at 10 kHz...");
}

void loop() {
  for (int i = 0; i < SAMPLE_COUNT; i++) {
    AD5933::setControlMode(CTRL_INIT_START_FREQ);
    AD5933::setControlMode(CTRL_START_FREQ_SWEEP);

    while (!(AD5933::readStatusRegister() & STATUS_DATA_VALID));

    AD5933::getComplexData(&realPart, &imagPart);

    double magnitude = sqrt(pow(realPart, 2) + pow(imagPart, 2));
    double impedance = 1.0 / (magnitude * gain);

    Serial.print("Sample ");
    Serial.print(i + 1);
    Serial.print(": R=");
    Serial.print(realPart);
    Serial.print("  I=");
    Serial.print(imagPart);
    Serial.print("  |Z|=");
    Serial.println(impedance, 4);

    delay(10);
  }

  Serial.println("Measurement complete.");
  AD5933::setPowerMode(POWER_STANDBY);
  while (1);
}
