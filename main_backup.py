'''
Main file for now for backend code....
Split out code as needed.
Brought to you by alcohol, my permanent companion.

Need to install and import keyboard to detect keypresses - global keypress monitor

'''

# import sys
# import termios
# import tty
# #import keyboard
# import tkinter as tk


# # Purpose: Listends to key events
# # Parameters: None.
# # Returns: None
# def onTextChange(input, field):
#     field.unbind("<<TextModified>>")
#     # To prevent infinite loop, unbind the event !!!!!!!!!!!!!
#     current = input.get()
#     input.set(current + 'n')
    

# ### Backend Dev ###

# # Intial commit should be a consol UI, inputManager handles all input and changes
# class inputManager():
#     def __init__(self):
#         self.buffer = ''
    
#     # Purpose: Listends to key events
#     # Parameters: None.
#     # Returns: None
#     def onTextChange(self):
#         pass


# main_window = tk.Tk()
# main_window.geometry("400x600")
# main_window.title('Text Box')
# text_box = tk.Text(main_window,wrap=tk.WORD, height=10,width=10)

# user_string = tk.StringVar()

# def get_box():
#     print(text_box.get())

# test_button = tk.Button(main_window, text="Test", command=get_box) #if we want to test initialize the function

# text_box.bind("<<Modified>>", onTextChange(user_string,text_box))
# text_box.pack()
# test_button.pack()

# tk.mainloop()

