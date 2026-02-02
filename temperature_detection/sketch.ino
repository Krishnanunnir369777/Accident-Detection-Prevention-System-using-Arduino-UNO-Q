#include <Arduino_Modulino.h>
#include <Arduino_RouterBridge.h>

ModulinoThermo thermo;

void setup() {
  Serial.begin(115200);

  // Initialize Modulino Sensors
  Modulino.begin();
  thermo.begin();

  // Initialize Communication Bridge
  Bridge.begin();
}

void loop() {
  // 1. Read the physical sensor
  float temp = thermo.getTemperature();

  // 2. Send the data to the Python "process_temperature" function
  String response;
  bool success = Bridge.call("process_temperature", temp).result(response);

  if (success) {
    Serial.print("Data Synced. Temp: ");
    Serial.println(temp);
  } else {
    Serial.println("Bridge Error: Connection Lost");
  }

  delay(2000); // Check temperature every 2 seconds
}