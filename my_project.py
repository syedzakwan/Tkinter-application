import tkinter as tk 
from tkinter.ttk import Label, Style 
from tkinter import font
import os,sys
import time
import pdb


class Application(tk.Frame):
    #main_frame = tk.Frame(master=root)
    #main_frame.rowconfigure((0,1,2), weight=1)
    #main_frame.columnconfigure((0,1,2), weight=1)
    
    def __init__(self,master):
        super().__init__(master)
        self.master = master
        #self.main_frame = tk.Frame(master=root)
        self.master.rowconfigure((0,1,2), weight=1)
        self.master.columnconfigure((0,1,2), weight=1)
        #self.main_frame.rowconfigure((0,1,2), weight=1)
        #self.main_frame.columnconfigure((0,1,2), weight=1)
        
    #function to create button
    def create_button(self, text_name,n_row,n_column,fg,bg):
        self.text_name = text_name
        self.fg = fg
        self.bg= bg
        self.button = tk.Button(master=self.main_frame, text=self.text_name, fg=self.fg,bg=self.bg) #command= lambda: self.choose_android())
        self.button.grid(row=n_row, column=n_column)

    #function to create label
    def create_label(self,text_name,n_row,n_column,fg=None,bg=None, t_font=None, s_font=None):
        self.text_name = text_name
        self.fg =fg
        self.bg = bg
        self.label = tk.Label(master=self.main_frame, text=self.text_name, fg=self.fg, bg=self.bg)
        self.label.grid(row=n_row,column=n_column)#, sticky='nsew') 
        self.label.config(font=(t_font,s_font))

    def create_entry(self):
        pass

    def create_text(self):
        pass

    def set_position(self,n_row,n_column,s_padx=None, s_pady=None, t_sticky=None):
        self.main_frame.grid(row=n_row,column=n_column, padx=s_padx, pady=s_pady, sticky=t_sticky)

    def create_frame(self,t_relief=None, w_borderwidth=None):
        self.main_frame = tk.Frame(self.master, relief=t_relief, borderwidth= w_borderwidth)
    
    def font_style(self, family="Lucida Grande", size=20):
        self.fontstyle = font.Font(family,size)

    def choose_android(self):
        self.main_frame.destroy()

    
def android_main_page(root):
    widget_welcome.create_frame.destroy()
    widget_android.create_frame.destroy()
    widget_os_selection.create_frame.destroy()
    widget_yocto.create_frame.destroy()

    pass

def command(event):
        widget_welcome.destroy()


def yocto_main_page():
    pass

if __name__=="__main__":
    root=tk.Tk()
    root.geometry("500x400")
    root.title("Menuscript")
    
    widget_welcome = Application(root)
    widget_welcome.create_frame(t_relief='flat')
    widget_welcome.create_label("Welcome to Menuscript",0,0,t_font='Arial', s_font=8)
    widget_welcome.set_position(0,0,t_sticky='nw')

    widget_os_selection = Application(root)
    widget_os_selection.create_frame(t_relief='sunken')
    widget_os_selection.create_label("OS Selection",0,1,'black', 'white', 'Arial', 15)
    widget_os_selection.set_position(0,1,10,10)#,t_sticky='sew')

    
    widget_android = Application (root)
    widget_android.create_frame(t_relief='raised',w_borderwidth=5)
    widget_android.create_button('Android',n_row=1, n_column=1, fg='black', bg='white') 
    widget_android.set_position(1,0,5,5,t_sticky='en')
    widget_android.bind("<Button-1>", command) 

    widget_yocto = Application(root)
    widget_yocto.create_frame(t_relief='raised', w_borderwidth=5)
    widget_yocto.create_button("YOCTO",n_row=1, n_column=2, fg='black',bg='white')
    widget_yocto.set_position(1,2,5,5, t_sticky='wn')
    root.mainloop()
