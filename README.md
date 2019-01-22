# nowater
Automatic system to alert (with a buzzer and a LED) when the water level in a tank drops below a given threshold.

## Hardware


| **Qt**  | **€/un*** | **Ʃ €** | **Photo**                                   | **Description**                                                                                                                                                                                                        | Notes                                                                               |
|---------|----------|----------|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| 1       | 7       | 7       |![](Media/images/sensors/RPi.PNG)            |[Raspberry pi 3B](https://www.raspberrypi.org/products/#buy-now-modal)                                                                                                                                                  | Server                                                                              |
| 1       | 16.2     | 16.2     |![](Media/images/sensors/nextion.PNG)        |[Nextion HMI touch display 2.8"](https://www.itead.cc/nextion-nx3224t028-1933.html)                                                                                                                                     | Graphical User Interface (GUI)                                                      |
|

XKC-Y25-NPN Non-Contact Liquid Level Sensor
ESP-32 WROOM development board 


## Software  

The code was developed in micropython for controllers and flashed into the ESP32.