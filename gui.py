from tkinter import *


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Student: ')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)


