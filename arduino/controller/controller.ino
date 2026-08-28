#include <XInput.h>

void setup() {
  XInput.begin();  // Initialize the XInput library
}

void loop() {
  XInput.press(BUTTON_A);    // Press the 'A' button
  delay(1000);
  XInput.release(BUTTON_A);  // Release the 'A' button
  delay(1000);
}
