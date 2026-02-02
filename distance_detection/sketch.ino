#include <Arduino_Modulino.h>

ModulinoDistance distance;
const int SERVO_PIN = 9;

void setup() {
  Serial.begin(115200);
  Modulino.begin();
  distance.begin();
  pinMode(SERVO_PIN, OUTPUT);
  Serial.println("--- Hardware Test Mode ---");
}

void loop() {
  int pulseWidth = 1500; // Default STOP

  if (distance.available()) {
    int dist = distance.get();
    Serial.print("Dist: ");
    Serial.println(dist);

    if (dist < 100) {
      pulseWidth = 1500; // STOP
    } else {
      pulseWidth = 1000; // RUN
    }
  }

  // Manually trigger the servo pulse
  digitalWrite(SERVO_PIN, HIGH);
  delayMicroseconds(pulseWidth);
  digitalWrite(SERVO_PIN, LOW);
  
  // Wait for the rest of the 20ms cycle
  delay(20); 
}