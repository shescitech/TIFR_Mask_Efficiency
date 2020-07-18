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
5. 
