const int micPin = A0;
const int sampleWindow = 50;

void setup() {
  Serial.begin(9600);
}

void loop() {

  unsigned long startMillis = millis();

  int signalMax = 0;
  int signalMin = 1024;

  while (millis() - startMillis < sampleWindow) {

    int sample = analogRead(micPin);

    if (sample > signalMax)
      signalMax = sample;

    if (sample < signalMin)
      signalMin = sample;
  }

  int peakToPeak = signalMax - signalMin;

  Serial.println(peakToPeak);

  delay(20);
}