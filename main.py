'''
Main file for now for backend code....
Split out code as needed.
Brought to you by alcohol, my permanent companion.

Need to install and import keyboard to detect keypresses - global keypress monitor

'''



#1. Impot Django

#2. Start Django Project
        #myproject/
            #manage.py
            #myproject/
                #__init__.py
                #settings.py
                #urls.py
                #asgi.py
                #wsgi.py
#3. Create new app:
        #cd myproject
        #python manage.py startapp myapp
#myapp/
    #migrations/
     #   __init__.py
   # __init__.py
   #admin.py
    #apps.py
    #models.py
    #tests.py
    #views.py
#4.Configure settings.py
    #INSTALLED_APPS = [
    #    ...
    #    'myapp',
    #]
#Set Up a Database:
#Django comes with SQLite by default, but you can configure it to use other databases like PostgreSQL, MySQL, etc. in the DATABASES setting of settings.py.
    #Set Up URLs:
    #In myproject/urls.py, you can include the URLs of your app:

#5.Step 5: Run the Development Server
# Use the following command to run the development server:
    # python manage.py runserver
#You can then navigate to http://127.0.0.1:8000/ in your browser to view the default Django page.







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
