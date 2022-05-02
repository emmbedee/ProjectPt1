from gui import *


def main():
    window = Tk()
    window.title('Lab 10')  # Change the window title to 'Lab 10'.
    window.geometry('250x180')  # Set its length to 250 and height to 180.
    # window.resizable(False, False)  # Make the window non-resizable.
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
