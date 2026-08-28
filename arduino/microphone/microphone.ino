#define analogPin A0
#define digitalPin 2

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(digitalPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  int analogValue = analogRead(analogPin);
  int digitalValue = digitalRead(digitalPin);

  Serial.print("Analog: ");
  Serial.print(analogValue);
  Serial.print(" | Digital: ");
  Serial.println(digitalValue);

  if (digitalValue == HIGH) {
    digitalWrite(LED_BUILTIN, HIGH);
  } else {
    digitalWrite(LED_BUILTIN, LOW);
  }
  delay(300);
}
