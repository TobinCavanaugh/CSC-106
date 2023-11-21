#include <Arduino.h>
#include <stdlib.h>

//Use #define so the values are compile time const
#define green_led 4
#define yellow_led 3
#define red_led 2
#define delayVal 400

void setup() {
  //Setup LEDs
  pinMode(green_led, OUTPUT);
  pinMode(yellow_led, OUTPUT);
  pinMode(red_led, OUTPUT);
  pinMode(13, OUTPUT);
}

//Method that sets the digital pin `pin` to high, then waits dv ms then sets the pin to low
void Toggle(uint8_t pin, uint8_t dv) {
  digitalWrite(pin, HIGH);
  delay(dv);
  digitalWrite(pin, LOW);
}

// the loop function runs over and over again forever
void loop() {

  //We digital write 13 to high so i can do other projects with pin 13
  digitalWrite(13, HIGH);

  //Flash the green led 2.5s, then yellow 1.25s, then red 3.5s.
  Toggle(green_led, 2500);
  Toggle(yellow_led, 1250);
  Toggle(red_led, 3500);
}