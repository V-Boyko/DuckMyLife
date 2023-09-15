'''
Main file for now for backend code....
Split out code as needed.
Brought to you by alcohol, my permanent companion.

Need to install and import keyboard to detect keypresses - global keypress monitor

'''

import sys
import termios
import tty
import keyboard

### Backend Dev ###

# Intial commit should be a consol UI, inputManager handles all input and changes
class inputManager():
    def __init__(self):
        self.buffer = ''
    
    # Purpose: Listends to key events
    # Parameters: None.
    # Returns: None
    def listenToKeys(self):
        # Save the terminal's current settings

        while True:
            event = keyboard.read_event()
            print(self.buffer)
            if event.event_type == 'enter':
                print("Users output: " + self.buffer)
                self.buffer = ''
            elif event.name == 'backspace':
                self.buffer = self.buffer[:-1]
            elif len(event.name) == 1:
                self.buffer += event.name



# Tracks keyboard events.

    
# Autocomplete Engine.

# A retrospective auto complete that triggers every so many key strokes.

# test area


user_test = print("Type something for the listener: ")

testo = inputManager().listenToKeys()
