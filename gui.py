import tkinter
from tkinter import *
from grade import *
from tkinter import messagebox


class GUI:
    def __init__(self, window):
        self.window = window
        # Frame for STUDENT input.
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Student: ', font=25)
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)

        # Frame for SCORE input.
        self.frame_score = Frame(self.window)
        self.label_score = Label(self.frame_score, text='Score: ', font=25)
        self.entry_score = Entry(self.frame_score)
        self.label_score.pack(padx=5, side='left')
        self.entry_score.pack(padx=16, side='left')
        self.frame_score.pack(anchor='w', pady=10)

        # Frame for SAVE button.
        self.frame_save = Frame(self.window)
        self.label_save = Label(self.frame_save, text='Last entry: [None,None]', font=33)
        self.button_save = Button(self.frame_save, text='SAVE', command=self.clicked, font=25)
        self.label_save.pack(pady=1, side='left')
        self.button_save.pack(pady=30)
        self.frame_save.pack()

    def clicked(self):
        """
        Function executes when "SAVE" button is clicked by user:
            Gets user input and check for errors.
            If input is acceptable then the input is used to create/maintain a student grade .csv file.

        """
        name = self.entry_name.get()
        score = self.entry_score.get()

        if (name.strip() == '') or (score.strip() == ''):
            messagebox.showwarning(title='Input Error', message='NAME or SCORE cannot be empty!')
            self.clear_input()
        elif not check_name(name):
            messagebox.showwarning(title='Input Error',
                                   message='You must enter a valid name without numbers or special '
                                           'characters.')
            self.clear_input()
        elif not check_score(score):
            if check_score(score) == 0.0:
                self.save_update(name, score)
            else:
                messagebox.showwarning(title='Input Error', message='You must enter a number between 0 and 100!')
                self.clear_input()
        else:
            self.save_update(name, score)

    def clear_input(self):
        """
        Function to simplify input clearing calls and reduce code clutter.
        """
        self.entry_name.delete(0, END)
        self.entry_score.delete(0, END)

    def save_update(self, name, score):
        """
        Function to simplify csv save behavior and user interface "last entry" update.  Reduces clutter.
        :param name: User input passed from NAME entry box.
        :param score: User input passed from SCORE entry box.
        :return: None.
        """
        iterable = [name, determine_grade(check_score(score))]
        save_file(iterable)
        self.clear_input()
        self.label_save.config(text=f'Last entry: [{iterable[0]},{iterable[1]}]')
