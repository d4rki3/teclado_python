#-*-coding:utf8;-*-
#teclado_virtual_v2
#autor:jarson

from tkinter import *
import tkinter
import sys
import os

class App_teclado:
    def __init__ (self, master=None):

        #frame master
        self.frame_master = Frame(master)
        self.frame_master["pady"] = 10
        self.frame_master.configure(bg='sky blue')
        self.frame_master.pack(fill='both', expand=True)

        #nome entry
        self.entry_text = Entry(self.frame_master)
        self.entry_text.config(relief=RIDGE)
        self.entry_text.pack()

        #frame 123
        self.frame_123 = Frame(self.frame_master)
        self.frame_123.configure(bg='sky blue')
        self.frame_123.pack()#fill='both', expand=True)

        #frame qwe
        self.frame_qwe = Frame(self.frame_master)
        self.frame_qwe.configure(bg='sky blue')
        self.frame_qwe.pack()#fill='both', expand=True)

        #frame asd
        self.frame_asd = Frame(self.frame_master)
        self.frame_asd.configure(bg='sky blue')
        self.frame_asd.pack()#fill='both', expand=True)

        #frame zxc
        self.frame_zxc = Frame(self.frame_master)
        self.frame_zxc.configure(bg='sky blue')
        self.frame_zxc.pack()#fill='both', expand=True)

        #frame space
        self.frame_space = Frame(self.frame_master)
        self.frame_space.configure(bg='sky blue')
        self.frame_space.pack(fill='both', expand=True)

        def key(valor):
            if valor == '←':
                posicao = len(self.entry_text.get()) -1
                self.entry_text.delete(int(posicao))
        
                print(posicao)
                
            elif valor == 'aceitar':
                self.entry_text.delete(0, END)
                teclado.destroy()
        
            elif valor == 'space':
                self.entry_text.insert(END, ' ')

            elif valor == 'cancelar':
                self.entry_text.delete(0, END)
                teclado.destroy()
                
            else:    
                self.entry_text.insert(END, valor)
        
        for i in lista_123:
            self.button = Button(self.frame_123)
            self.button['text'] = i
            self.button['font'] = ('Arial', '16', 'bold')
            self.button["command"] = lambda x = i: key(x)
            self.button.configure(bg='sky blue',
                                  activebackground='sky blue')
            self.button.pack(side='left', fill='both', expand=True)

        for i in lista_qwe:
            self.button = Button(self.frame_qwe)
            self.button['text'] = i
            self.button['font'] = ('Arial', '16', 'bold')
            self.button["command"] = lambda x = i: key(x)
            self.button.configure(bg='sky blue',
                                  activebackground='sky blue')
            self.button.pack(side='left', fill='both', expand=True)

        for i in lista_asd:
            self.button = Button(self.frame_asd)
            self.button['text'] = i
            self.button['font'] = ('Arial', '16', 'bold')
            self.button["command"] = lambda x = i: key(x)
            self.button.configure(bg='sky blue',
                                  activebackground='sky blue')
            self.button.pack(side='left', fill='both', expand=True)

        for i in lista_zxc:
            self.button = Button(self.frame_zxc)
            self.button['text'] = i
            self.button['font'] = ('Arial', '16', 'bold')
            self.button["command"] = lambda x = i: key(x)
            self.button.configure(bg='sky blue',
                                  activebackground='sky blue')
            self.button.pack(side='left', fill='both', expand=True)

        for i in lista_space:
            self.button = Button(self.frame_space)
            self.button['text'] = i
            self.button['font'] = ('Arial', '16', 'bold')
            self.button["command"] = lambda x = i: key(x)
            self.button.configure(bg='sky blue',
                                  activebackground='sky blue')
            self.button.pack(side='left', fill='both', expand=True)

lista_123=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '←']
lista_qwe=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']']
lista_asd=['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ç', '~', '^']
lista_zxc=['z', 'x', 'c', 'v', 'b', 'n', 'm', '<','>','.', ',', ':']
lista_space=['aceitar', 'space', 'cancelar']

#print(lista_123)

global posicao

if __name__ == '__main__':
    teclado = Tk()
    teclado.title('Teclado Virtual')
    #teclado.geometry('400x250+200+200')
    #teclado.overrideredirect(True)
    teclado.resizable(False, False)
    App_teclado(teclado)
    teclado.mainloop()

