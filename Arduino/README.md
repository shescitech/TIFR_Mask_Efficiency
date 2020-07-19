# Usage Instructions 

This folder consists of code to inetgrate Plantower air quality sensor PMS7003 with any ESP8266 based board (Wemos D1 R2, Nodemcu, Wemos D1 mini etc) and stream the particle count data to local http web server as well as to local telent server.


## Installation

1. Install the Arduino IDE from https://www.arduino.cc/en/Main/Software based on the operating system of your computer
2. Start Arduino application and open Preferences window.
3. Enter https://arduino.esp8266.com/stable/package_esp8266com_index.json into Additional Board Manager URLs field.
4. Open Boards Manager from Tools > Board menu and search for esp8266.
5. There will be one by ESP8266 community. Select the latest version from the drop-down box and click install button. 

## Using the code

1. After downloading the repository go to the "PMS7003_OTA_update_httpserver" folder and open the main code "PMS7003_OTA_update_httpserver.ino" file.
2. Connect the esp8266 based board to your computer via a usb cable.
3. Choose the correct port from Tools > Port. In case of windows operating system you can get the port no. from Device Manager > Ports. Look for the one which mentions usb-serial.
4. Go back to arduino IDE and select your ESP8266 board from Tools > Board menu after installation.
5. In the expressions of "const char* ssid" and "const char* password" respectively, change the name and password of the WiFi network you want to connect to (inside the double        quotes).
6. Upload the code from Sketch > Upload option.
7. If there is no error, the uploadong will finish and arduino IDE will show a message something like "Leaving...Hard resetting via RTS pin" in the bottom black panel and reset      the board. This is not an error. It means your code is uploaded succesfully to the ESP module.
8. Open the serial monitor from Tools > Serial Monitor to know the IP address of the ESP module. Alternatively you can also download any android application which supports local      mDNS, e.g. "BonjourBrowser" and get the IP address corresponding to the host "esp8266-webupdate". For this to work your smartphone must be connected to the same WiFi network as    the ESP module.
9. Change the IP address in the downloaded html file and open it in any web browser use as instructed in the web folder. For getting data through python refer to the python folder in this repository.
10. If you want to make changes to the code (e.g. change wifi name and password, acquisition rate in seconds etc.) you can change the required things in the code and either upload it via connecting the ESP module to the computer same as the initial setup (points 1 - 8) or you can do it via OTA (over the air) update through WiFi network without connecting    physically to the computer. Read below for OTA update.  
11. Compile the sketch from Sketch > export compiled binary option. It will create a binary (.bin) file in the same folder as your code. Now get the IP address of the module from the android application mentioned in 8. If the wifi information is not changed and your WiFi router uses static IP, then IP address will remain unchanged. Now go to "http://xxx.xxx.xxx.xxx/update", where xxx.xxx.xxx.xxx is the IP address. You will be required to use a username and password if you are going to open this link for the first time in your computer. Default username and password are "admin" and "admin" respectively. If needed you can also change these in the code (const char* update_username and const char* update_password" variables). Click on "choose your file" button to browse to the location of the .bin file generated and select it. Click on the "update firmware" button and wait for it to upload. If the upload is done successfully, a message will be displayed "Update Success! Rebooting..."
12. If you want to use multiple ESP modules in the same WiFi network, change the host name (const char* host) in the code to uniquely identify each modules for getting their IP addresses.
13. By mistake if you upload wrong WiFi name or password it will not connect to the WiFi network. If there is no way to connect it to a computer because of any reason there is a option to correct it in the code. Create a WiFi hotspot from your smartphone named "PMS7003_your WiFi ssid_your WiFi password", where put your correct WiFi name and password. The ESP module will scan the WiFi network and get the correct WiFi name and password to connect. Once it is connected to the network, change the correct Wifi name or password in the Arduino IDE and recompile and upload via OTA (step 11).
