from tkinter import *
from grade import *
from tkinter import messagebox
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

        # Frame for SAVE button.
        self.frame_save = Frame(self.window)
        self.button_save = Button(self.frame_save, text='EXPORT', command=self.clicked)
        self.button_save.pack(pady=15)
        self.frame_save.pack()

    def clicked(self):

        if (self.entry_name.get().strip() == '') or (self.entry_score.get().strip()) == '':
            messagebox.showwarning(title='Input Error', message='NAME or SCORE cannot be empty!')

        name = self.entry_name.get()
        score = self.entry_score.get()

        if not check_name(name):
            messagebox.showwarning(title='Input Error', message='You must enter a valid name without numbers or special '
                                                              'characters.')
        if not check_score(score):
            messagebox.showwarning(title='Input Error', message='You must enter a number between 0 and 100!')

        iterable = [name, determine_grade(check_score(score))]
        print(iterable)
        save_file(iterable)

        self.entry_name.delete(0, END)
        self.entry_score.delete(0, END)

