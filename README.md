# nowater
Automatic system to alert (with a buzzer and a LED) when the water level in a tank drops below a given threshold.

## Hardware


| **Qt**  | **€/un*** | **Ʃ €** | **Photo**                                   | **Description**                                                                                                                                                                                                        | Notes                                                                               |
|---------|----------|----------|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| 1       | 7       | 7       |![](Media/BOM/ESP-32 dev.jpeg)            |[ESP-32 WROOM dev board](https://www.aliexpress.com/item/ESP32-ESP-32-ESP32S-ESP-32S-CP2102-Wireless-WiFi-Bluetooth-Development-Board-Micro-USB-Dual-Core/32867696371.html)                                       | Microcontroler                                                                            |
| 1       | 5     | 5     |![](Media/BOM/XKC-Y25-NPN.jpg)        |[XKC-Y25-NPN](https://www.aliexpress.com/item/XKC-Y25-NPN-Water-Level-Sensor-Non-Contact-Liquid-Level-Sensor-Detection-Tools-for-Airtight-Container/32864811235.html)                                                                                                                                     | Non-Contact Liquid Level Sensor                                                      |
| 1       | 0.1      | 0.1      |![](Media/images/sensors/buzzer.PNG)         |► [Active Buzzer Alarm 5 V](https://www.aliexpress.com/item/10pcs-5v-Active-Buzzer-Magnetic-Long-Continous-Beep-Tone-Alarm-Ringer-12mm-MINI-Active-Piezo-Buzzers/32914327679.html)                                     | Audible sound to alert for the end of a test                                         |



## Software  

The code was developed in micropython for controllers and flashed into the ESP32.