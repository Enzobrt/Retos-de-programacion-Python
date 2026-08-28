#include <IRremote.h>

const int IR_RECEIVE_PIN = 8;  // Define the pin number for the IR Sensor
String lastDecodedValue = "";  // Variable to store the last decoded value
const int PIN_LEDS[] = { 9, 10 };
int LUCES[] = { 0, 0 };  // Entre 0 y 255
int NUM_LEDS = 2;
int ACTIVA = 0;  // Led activo
int INC = 20;

void setup() {
  Serial.begin(9600);                                     // Start serial communication at 9600 baud rate
  IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);  // Start the IR receiver

  // Activar todos los leds
  for (int i = 0; i < NUM_LEDS; i = i + 1) {
    pinMode(PIN_LEDS[i], OUTPUT);
  }
}

void loop() {
  if (IrReceiver.decode()) {
    String decodedValue = decodeKeyValue(IrReceiver.decodedIRData.command);
    if (decodedValue != "ERROR") {
      Serial.println(decodedValue);
      delay(100);
    }
    if (decodedValue == "POWER") {  // Maxima potencia led
      LUCES[ACTIVA] = 255;
      digitalWrite(LED_BUILTIN, HIGH);
    }
    if (decodedValue == "MUTE") {  // Apagar led
      LUCES[ACTIVA] = 0;
      digitalWrite(LED_BUILTIN, LOW);
    }
    if (decodedValue == "+") {
      LUCES[ACTIVA] += INC;
      if (LUCES[ACTIVA] > 255) {
        LUCES[ACTIVA] = 255;
      }
    }
    if (decodedValue == "-") {
      LUCES[ACTIVA] -= INC;
      if (LUCES[ACTIVA] < 0) {
        LUCES[ACTIVA] = 0;
      }
    }
    if (decodedValue == "MODE") {
      // Apagar led
      LUCES[ACTIVA] = 100;
      
    // Seleccion del led activo
    if (decodedValue == "1") {
      ACTIVA = 0;
    }
    if (decodedValue == "2") {
      ACTIVA = 1;
    }

    IrReceiver.resume();  // Enable receiving of the next value
  }
}

String decodeKeyValue(long result) {
  switch (result) {
    case 0x16:
      return "0";
    case 0xC:
      return "1";
    case 0x18:
      return "2";
    case 0x5E:
      return "3";
    case 0x8:
      return "4";
    case 0x1C:
      return "5";
    case 0x5A:
      return "6";
    case 0x42:
      return "7";
    case 0x52:
      return "8";
    case 0x4A:
      return "9";
    case 0x9:
      return "+";
    case 0x15:
      return "-";
    case 0x7:
      return "EQ";
    case 0xD:
      return "U/SD";
    case 0x19:
      return "CYCLE";
    case 0x44:
      return "PLAY/PAUSE";
    case 0x43:
      return "FORWARD";
    case 0x40:
      return "BACKWARD";
    case 0x45:
      return "POWER";
    case 0x47:
      return "MUTE";
    case 0x46:
      return "MODE";
    case 0x0:
      return "ERROR";
    default:
      return "ERROR";
  }
}
