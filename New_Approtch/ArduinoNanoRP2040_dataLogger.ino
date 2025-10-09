const int Pin = A0;         
const unsigned int sampleRate = 10000; // 10 kHz (not used)
const unsigned int samplePeriodUs = 1000000 / sampleRate;

void setup() 
{
  Serial.begin(115200);  
  while (!Serial);
  analogReadResolution(10); // 10-bit resolution (0-1023)
}

void loop() 
{
  int val = analogRead(Pin);     // Read analog pin A0
  Serial.println(val);           // Print raw value
  delay(50);                     // 50 ms delay = ~20 Hz sampling rate
}
