from tkinter import Tk
a = Tk()
clipboard = a.clipboard_get()
a.destroy()
file = open('PATHTOTEXTFILE', 'a')
file.write('' + str(clipboard) + '\n')
file.close()