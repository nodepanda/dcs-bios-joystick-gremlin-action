# -*- coding: utf-8; -*-
import os
import socket
from PyQt5 import QtCore, QtGui, QtWidgets
from xml.etree import ElementTree

from gremlin.base_classes import AbstractAction, AbstractFunctor
from gremlin.common import InputType
import gremlin.ui.input_item
from gremlin import util


class DCSBIOSWidget(gremlin.ui.input_item.AbstractActionWidget):
    """Widget for the DCS-BIOS action."""

    def __init__(self, action_data, parent=None):
        super().__init__(action_data, parent=parent)
        assert isinstance(action_data, DCSBIOSAction)

    def _create_ui(self):
        self.layout = QtWidgets.QHBoxLayout()
        
        # Commands Input
        self.commands_input = QtWidgets.QLineEdit()
        self.commands_input.setPlaceholderText("e.g. PITOT_HEAT 1")
        self.commands_input.textChanged.connect(self._command_changed)
        
        self.layout.addWidget(QtWidgets.QLabel("Commands (separate by commas):"))
        self.layout.addWidget(self.commands_input)
        self.main_layout.addLayout(self.layout)

    def _populate_ui(self):
        self.commands_input.setText(self.action_data.commands)

    def _command_changed(self, text):
        self.action_data.commands = text


class DCSBIOSFunctor(AbstractFunctor):
    def __init__(self, action):
        super().__init__(action)
        self.commands = action.commands
        self.ip = "127.0.0.1"
        self.port = 7778

    def process_event(self, event, value):
        #try:
            # Append newline and encode to bytes
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        commands = self.commands
        
        for command in commands.split(","):
            command = (command.strip()+"\n").encode("utf-8")
            sock.sendto(command, (self.ip, self.port))
            
        sock.close()
    #except Exception as e:
    #    print(f"DCS-BIOS Error: {e}")
    
        return True


class DCSBIOSAction(AbstractAction):
    """Action to send commands to DCS-BIOS via UDP."""

    name = "DCS-BIOS"
    tag = "dcs-bios"

    default_button_activation = (True, False)
    input_types = [
        InputType.JoystickAxis,
        InputType.JoystickButton,
        InputType.JoystickHat,
        InputType.Keyboard
    ]

    functor = DCSBIOSFunctor
    widget = DCSBIOSWidget

    def icon(self):
        # Standard icon path logic
        return "{}/icon.png".format(os.path.dirname(os.path.realpath(__file__)))

    def __init__(self, parent):
        super().__init__(parent)
        self.commands = ""
        
    def requires_virtual_button(self):
        return self.get_input_type() in [
            InputType.JoystickAxis,
            InputType.JoystickHat
        ]

    def _parse_xml(self, node):
        self.commands = node.get("commands", "")

    def _generate_xml(self):
        node = ElementTree.Element("dcs-bios")
        node.set("commands", self.commands)
        return node

    def _is_valid(self):
        return len(self.commands) > 0


version = 1
name = "dcs-bios"
create = DCSBIOSAction
