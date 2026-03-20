# dcs-bios-joystick-gremlin-action
This is a very simple [**Joystick Gremlin R13**](https://github.com/WhiteMagic/JoystickGremlin/tree/r13) custom action that simply sends a command (or commands) to the default DCS-BIOS UDP port on 127.0.0.1:7778.
# Installation
1. Put the **dcs-bios** folder into your Joystick Gremlin installation folder under **actions**.
2. Restart Joystick Gremlin.
# Usage
Add the action to a button and type in the command. You can execute multiple commands if you add them separated by comma.
# FAQ
## I want to send the commands to a different IP or PORT
I don't know how to setup an interface inside Joystick Gremlin for this so you have to it manually.
1. Open the **\_\_init\_\_.py**
2. Set your IP address or PORT.
