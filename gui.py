from tkinter import *
import csv


class GUI:
    def __init__(self, window):
        self.window = window
        # Frame for STUDENT input.
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Student: ')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)

        # Frame for SCORE input.
        self.frame_score = Frame(self.window)
        self.label_score = Label(self.frame_score, text='Score: ')
        self.entry_score = Entry(self.frame_score)
        self.label_score.pack(padx=5, side='left')
        self.entry_score.pack(padx=5, side='left')
        self.frame_score.pack(anchor='w', pady=10)

