#include "FastLED.h"
#define NUM_LEDS 140
#define PIN 6

String received_effect;
int a,b,c, bn;

CRGB leds[NUM_LEDS];

void setup() {
  // 
  Serial.begin(57600);
  Serial.println("======Arduino-Live-LED-System====");
  Serial.println("");
  delay(100);
  Serial.println("Start Serial Monitor listening...");
  FastLED.addLeds<WS2811, PIN, BRG>(leds, NUM_LEDS); 
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
      received_effect = Serial.readStringUntil('\n');
      if(received_effect == "rgb") {
        delay(10000);  //delay for debugging with Serial monitor
        received_effect = Serial.readStringUntil(',');
        a = received_effect.toInt();
        Serial.print("\nR: "); //debugging
        Serial.print(a, DEC);
        received_effect = Serial.readStringUntil(',');
        b = received_effect.toInt();
        Serial.print("\nG: "); //debugging
        Serial.print(b, DEC);
        received_effect = Serial.readStringUntil('\n');
        c = received_effect.toInt();
        Serial.print("\nB: "); //debugging
        Serial.print(c, DEC);
        for(int i=0; i<=NUM_LEDS; i++) {
           leds[i].setRGB( a, b, c);
        }
        FastLED.show();
        Serial.println("\nColor has been changed\n");
      }
//      if(received_effect=="br") {
//        delay(1000);
//        received_effect = Serial.readStringUntil('\n');
//        bn = received_effect.toInt();
//        for(int i=0; i<=NUM_LEDS; i++) {
//          leds[i] %= bn;
//        }
//        FastLED.setBrightness(bn);
//        FastLED.show();
//        Serial.print("\nBrightness has been changed to ");
//        Serial.print(bn, DEC);
//        Serial.println();
//      }
    }
}
