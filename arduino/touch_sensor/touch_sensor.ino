#define TOUCH_PIN 2

void setup() {
  pinMode(TOUCH_PIN, INPUT);
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (digitalRead(TOUCH_PIN) == HIGH) {
    Serial.print("Touch detected!");
    digitalWrite(LED_BUILTIN, HIGH);
  } 
  else {
    Serial.print("No touch");
    digitalWrite(LED_BUILTIN, LOW);
  }
  delay(100); 
}
