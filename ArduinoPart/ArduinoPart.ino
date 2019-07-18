#include "FastLED.h"

#define PIN         6
#define NUM_LEDS    40
#define BRIGHTNESS  64
#define LED_TYPE    WS2811
#define COLOR_ORDER BRG

String received_effect;
int a,b,c;
String break_;

CRGB leds[NUM_LEDS];

void setup() {
  // 
  Serial.begin(57600);
  Serial.println("======Arduino-Live-LED-System====");
  Serial.println("");
  delay(100);
  Serial.println("Start Serial Monitor listening...");
  FastLED.addLeds<WS2811, PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalSMD5050 );
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0) {
      received_effect = Serial.readStringUntil('\n');
      if(received_effect == "rgb") {
        Serial.setTimeout(5000);  //delay for debugging with Serial monitor
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
      
      if(received_effect == "rainbow") {
        Serial.println("Rainbow = 1");
        rainbow();
      }
  }
}
void rainbow() {
  Serial.setTimeout(1000);
  break_=Serial.readStringUntil('\n');
  if(break_ != "0") {
    Serial.setTimeout(1);
    while(break_ != "0") {
      static uint8_t starthue = 0;
      fill_rainbow( leds + 5, NUM_LEDS - 5, --starthue, 20);
      FastLED.setTemperature( Tungsten100W );
      leds[0] = Tungsten100W;
      FastLED.show();
      FastLED.delay(8);
      break_=Serial.readStringUntil('\n');
    }
  }
  Serial.println("Rainbow = 0");
  Serial.setTimeout(10000);
}
