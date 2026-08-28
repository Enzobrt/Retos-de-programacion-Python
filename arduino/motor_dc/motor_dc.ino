// Conecta un cable del pin 9 a uno de los pines del motor
// y conecta un cable de GND (tierra) al otro pin del motor

int motorPin = 9; // Connect motor control to pin 9

void setup() {
  pinMode(motorPin, OUTPUT);
}

void loop() {
  analogWrite(motorPin, 255);
  delay(2000);
  analogWrite(motorPin, 0);
  delay(2000);
}
