#define buzzerPin 4
#define buttonPin 2

void setup() {
  pinMode(buzzerPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9200);
}

void loop() {
  if(digitalRead(buttonPin) == HIGH) {
    tone(buzzerPin, 5000, 1000); // Play 1000 Hz tone for 1 second
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.println("Pressed");
  }
  else {
    noTone(buzzerPin); // Stop sound
    digitalWrite(LED_BUILTIN, LOW);
    Serial.println("Not pressed");
  }
  delay(50);
}
