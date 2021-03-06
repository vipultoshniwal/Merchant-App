#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jun 13, 2018 05:48:34 PM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import stockerlogin_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = stockerlogin (root)
    stockerlogin_support.init(root, top)
    root.mainloop()

w = None
def create_stockerlogin(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = stockerlogin (w)
    stockerlogin_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_stockerlogin():
    global w
    w.destroy()
    w = None


class stockerlogin:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {DejaVu Sans} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("325x303+533+140")
        top.title("stockerlogin")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.03, rely=0.03, relheight=0.94, relwidth=0.94)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="5")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#beadd8")
        self.Frame1.configure(width=304)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.2, rely=0.07, height=28, width=166)
        self.Label1.configure(background="#beadd8")
        self.Label1.configure(font=font9)
        self.Label1.configure(text='''stockerlogin''')
        self.Label1.configure(width=166)

        self.username = Label(self.Frame1)
        self.username.place(relx=0.03, rely=0.24, height=38, width=126)
        self.username.configure(background="#beadd8")
        self.username.configure(font=font9)
        self.username.configure(text='''username''')
        self.username.configure(width=126)

        self.password = Label(self.Frame1)
        self.password.place(relx=0.03, rely=0.42, height=38, width=126)
        self.password.configure(activebackground="#f9f9f9")
        self.password.configure(background="#beadd8")
        self.password.configure(font=font9)
        self.password.configure(text='''password''')
        self.password.configure(width=126)

        self.stocker_username = Entry(self.Frame1)
        self.stocker_username.place(relx=0.46, rely=0.27, height=20
                , relwidth=0.48)
        self.stocker_username.configure(background="white")
        self.stocker_username.configure(font="TkFixedFont")

        self.stocker_password = Entry(self.Frame1)
        self.stocker_password.place(relx=0.46, rely=0.44, height=21
                , relwidth=0.48)
        self.stocker_password.configure(background="white")
        self.stocker_password.configure(font="TkFixedFont")
        self.stocker_password.configure(selectbackground="#c4c4c4")
        self.stocker_password.configure(show="*")

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.29, rely=0.63, height=36, width=107)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#beadd8")
        self.Button1.configure(command=stockerlogin_support.stockerloginvalidation)
        self.Button1.configure(font=font9)
        self.Button1.configure(text='''Login''')
        self.Button1.configure(width=107)






if __name__ == '__main__':
    vp_start_gui()



