#define laserPin 2

void setup() {
  pinMode(laserPin, OUTPUT);
}

void loop() {
    digitalWrite(laserPin, HIGH);
    delay(2000); 
    digitalWrite(laserPin, LOW);
    delay(2000); 
}
