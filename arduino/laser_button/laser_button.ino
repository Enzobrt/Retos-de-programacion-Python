#define laserPin 4
#define buttonPin 2

void setup() {
  pinMode(laserPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  if(digitalRead(buttonPin) == false) {
    digitalWrite(laserPin, HIGH);
  }
  else {
    digitalWrite(laserPin, LOW);
  }
  delay(100);
}
