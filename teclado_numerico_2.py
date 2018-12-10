#-*-coding:utf8;-*-
#teclado_virtual
#autor:jarson

from tkinter import *
import sys
import os

class App_teclado:
    def __init__ (self, master=None):

        #frame master
        self.frame_master = Frame(master)
        #self.frame_master["pady"] = 10
        self.frame_master.configure(bg='sky blue')
        self.frame_master.pack(fill='both', expand=True)

        #nome entry
        self.entry_text = Entry(self.frame_master)
        self.entry_text.config(relief=RIDGE)
        self.entry_text.pack()

        #frame 123
        self.frame_123 = Frame(self.frame_master)
        self.frame_123.configure(bg='sky blue')
        self.frame_123.pack(fill='both', expand=True)

        #frame 456
        self.frame_456 = Frame(self.frame_master)
        self.frame_456.configure(bg='sky blue')
        self.frame_456.pack(fill='both', expand=True)

        #frame 789
        self.frame_789 = Frame(self.frame_master)
        self.frame_789.configure(bg='sky blue')
        self.frame_789.pack(fill='both', expand=True)

        #frame 000
        self.frame_000 = Frame(self.frame_master)
        self.frame_000.configure(bg='sky blue')
        self.frame_000.pack(fill='both', expand=True)

        #frame space
        self.frame_space = Frame(self.frame_master)
        self.frame_space.configure(bg='sky blue')
        self.frame_space.pack(fill='both', expand=True)

        def teclas(valor):
            if valor == '←':
                posicao = len(self.entry_text.get()) -1
                self.entry_text.delete(int(posicao))
        
                print(posicao)
                
            elif valor == 'ok':
                self.entry_text.delete(0, END)
                teclado.destroy()
        
            elif valor == ' ':
                self.entry_text.insert(END, ' ')

            elif valor == 'esc':
                self.entry_text.delete(0, END)
                teclado.destroy()
                
            else:    
                self.entry_text.insert(END, valor)
        
        for i in lista_123:
            self.button = Button(self.frame_123)
            self.button['text'] = i
            self.button['font'] = ('Arial', '16', 'bold')
            self.button["command"] = lambda x = i: teclas(x)
            self.button.configure(bg='sky blue',
                                  activebackground='sky blue')
            self.button.pack(side='left', fill='both', expand=True)

        for i in lista_456:
            self.button = Button(self.frame_456)
            self.button['text'] = i
            self.button['font'] = ('Arial', '16', 'bold')
            self.button["command"] = lambda x = i: teclas(x)
            self.button.configure(bg='sky blue',
                                  activebackground='sky blue')
            self.button.pack(side='left', fill='both', expand=True)

        for i in lista_789:
            self.button = Button(self.frame_789)
            self.button['text'] = i
            self.button['font'] = ('Arial', '16', 'bold')
            self.button["command"] = lambda x = i: teclas(x)
            self.button.configure(bg='sky blue',
                                  activebackground='sky blue')
            self.button.pack(side='left', fill='both', expand=True)

        for i in lista_000:
            self.button = Button(self.frame_000)
            self.button['text'] = i
            self.button['font'] = ('Arial', '16', 'bold')
            self.button["command"] = lambda x = i: teclas(x)
            self.button.configure(bg='sky blue',
                                  activebackground='sky blue')
            self.button.pack(side='left', fill='both', expand=True)

        for i in lista_space:
            self.button = Button(self.frame_space)
            self.button['text'] = i
            self.button['font'] = ('Arial', '16', 'bold')
            self.button["command"] = lambda x = i: teclas(x)
            self.button.configure(bg='sky blue',
                                  activebackground='sky blue')
            self.button.pack(side='left', fill='both', expand=True)
        
lista_123=['1', '2', '3', '←']
lista_456=['4', '5', '6', '-']
lista_789=['7', '8', '9', '+']
lista_000=[',', '0', '.', '=']
lista_space=['ok', ' ', 'esc']

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

