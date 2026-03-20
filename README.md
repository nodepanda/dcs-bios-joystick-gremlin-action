# dcs-bios-joystick-gremlin-action
This is a very simple [**Joystick Gremlin R13**](https://github.com/WhiteMagic/JoystickGremlin/tree/r13) custom action (written by Gemini) that simply sends a command (or commands) to the default DCS-BIOS UDP port on 127.0.0.1:7778.
# Installation
1. Put the **dcs-bios** folder into your Joystick Gremlin installation folder under **action_plugins**. (C:\Program Files (x86)\H2ik\Joystick Gremlin\action_plugins)
3. Restart Joystick Gremlin.
# Usage
Add the action to a button and type in the command. You can execute multiple commands if you add them separated by comma.

<img width="1208" height="369" alt="image" src="https://github.com/user-attachments/assets/dd2b0d73-6e89-4c32-bb73-3ec8d08328f2" />

# FAQ
## I want to send the commands to a different IP or PORT
I don't know how to setup an interface inside Joystick Gremlin for this so you have to it manually.
1. Open the **\_\_init\_\_.py**
2. Set your IP address and/or PORT in the DCSBIOSFunctor class.
```python
class DCSBIOSFunctor(AbstractFunctor):
    def __init__(self, action):
        super().__init__(action)
        self.commands = action.commands
        self.ip = "127.0.0.1"
        self.port = 7778
```
