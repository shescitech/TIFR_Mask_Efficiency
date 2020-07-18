# Usage Instructions 

This folder consists of code to inetgrate Plantower air quality sensor PMS7003 with any ESP8266 based board (Wemos D1 R2, Nodemcu, Wemos D1 mini etc) and stream the particle count data to local http web server as well as to local telent server.


## Installation

1. Install the Arduino IDE from https://www.arduino.cc/en/Main/Software based on the operating system of your computer
2. Start Arduino application and open Preferences window.
3. Enter https://arduino.esp8266.com/stable/package_esp8266com_index.json into Additional Board Manager URLs field.
4. Open Boards Manager from Tools > Board menu and search for esp8266.
5. Ther will be one by ESP8266 community. Select the latest version from the drop-down box and click install button. 

## Using the code

1. After downloading the repository go to the "PMS7003_OTA_update_httpserver" folder and open the main code "PMS7003_OTA_update_httpserver.ino" file.
2. Connect the esp8266 based board to your computer via a usb cable.
3. Choose the correct port from Tools > Port. In case of windows operating system you can get the port no. from Device Manager > Ports. Look for the one which mentions usb-serial.
4. Go back to arduino IDE and select your ESP8266 board from Tools > Board menu after installation.
5. In the expressions of "const char* ssid" and "const char* password" respectively, change the name and password of the WiFi network you want to connect to (inside the double        quotes).
6. Upload the code from Sketch > Upload option.
7. If there is no error, the uploadong will finish and arduino IDE will show a message something like "Leaving...Hard resetting via RTS pin" in the bottom black panel and reset      the board. This is not an error. It means your code is uploaded succesfully to the ESP module.
8. Open the serial monitor from Tools > Serial Monitor to know the IP address of the ESP module. Alternatively you can also download any android application which supports local      mDNS, e.g. "BonjourBrowser" and get the IP address corresponding to the host "esp8266-webupdate".

