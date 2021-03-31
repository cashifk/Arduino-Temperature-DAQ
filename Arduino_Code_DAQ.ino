#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into digital pin 2 on the Arduino
#define ONE_WIRE_BUS 2

// Setup a oneWire instance to communicate with any OneWire device
OneWire oneWire(ONE_WIRE_BUS);  

// Pass oneWire reference to DallasTemperature library
DallasTemperature sensors(&oneWire);

int deviceCount = 0;
float tempC;
double tempxx[20] = {0};

void setup(void)
{
  sensors.begin();  // Start up the library
  Serial.begin(9600);
  
  // locate devices on the bus
 //Serial.print(" ");
 // Serial.print(" ");
  deviceCount = sensors.getDeviceCount();
 // Serial.print(deviceCount, DEC);
 // Serial.println(" devices.");
 // Serial.println("");
}

void loop(void)
{ 
  // Send command to all the sensors for temperature conversion
  sensors.requestTemperatures(); 
  
  // Display temperature from each sensor
  for (int i = 0;  i < deviceCount;  i++)
  {
    //Serial.print("S");
    //Serial.print(i+1);
    //Serial.print(" ");
      {
        tempC = sensors.getTempCByIndex(i);
        tempxx[i] = sensors.getTempCByIndex(i);
        Serial.print(tempxx[i]);
    }
  Serial.print(","); //space
  }
  
  Serial.println();
 // delay(1000);
}
