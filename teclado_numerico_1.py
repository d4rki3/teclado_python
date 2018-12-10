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
        self.frame_123.pack(fill='both', expand=True)

        ###111
        self.butt_1 = Button(self.frame_123)
        self.butt_1['text'] = '1'
        self.butt_1['font'] = ('Arial', '16', 'bold')
        self.butt_1["command"] = self.key_1
        self.butt_1.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_1.pack(side='left', fill='both', expand=True)

        ###222
        self.butt_2 = Button(self.frame_123)
        self.butt_2['text'] = '2'
        self.butt_2['font'] = ('Arial', '16', 'bold')
        self.butt_2["command"] = self.key_2
        self.butt_2.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_2.pack(side='left', fill='both', expand=True)

        ###333
        self.butt_3 = Button(self.frame_123)
        self.butt_3['text'] = '3'
        self.butt_3['font'] = ('Arial', '16', 'bold')
        self.butt_3["command"] = self.key_3
        self.butt_3.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_3.pack(side='left', fill='both', expand=True)

        #frame 456
        self.frame_456 = Frame(self.frame_master)
        self.frame_456.configure(bg='sky blue')
        self.frame_456.pack(fill='both', expand=True)

        ###444
        self.butt_4 = Button(self.frame_456)
        self.butt_4['text'] = '4'
        self.butt_4['font'] = ('Arial', '16', 'bold')
        self.butt_4["command"] = self.key_4
        self.butt_4.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_4.pack(side='left', fill='both', expand=True)

        ###555
        self.butt_5 = Button(self.frame_456)
        self.butt_5['text'] = '5'
        self.butt_5['font'] = ('Arial', '16', 'bold')
        self.butt_5["command"] = self.key_5
        self.butt_5.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_5.pack(side='left', fill='both', expand=True)

        ###666
        self.butt_6 = Button(self.frame_456)
        self.butt_6['text'] = '6'
        self.butt_6['font'] = ('Arial', '16', 'bold')
        self.butt_6["command"] = self.key_6
        self.butt_6.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_6.pack(side='left', fill='both', expand=True)

        #frame 789
        self.frame_789 = Frame(self.frame_master)
        self.frame_789.configure(bg='sky blue')
        self.frame_789.pack(fill='both', expand=True)

        ###777
        self.butt_7 = Button(self.frame_789)
        self.butt_7['text'] = '7'
        self.butt_7['font'] = ('Arial', '16', 'bold')
        self.butt_7["command"] = self.key_7
        self.butt_7.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_7.pack(side='left', fill='both', expand=True)

        ###888
        self.butt_8 = Button(self.frame_789)
        self.butt_8['text'] = '8'
        self.butt_8['font'] = ('Arial', '16', 'bold')
        self.butt_8["command"] = self.key_8
        self.butt_8.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_8.pack(side='left', fill='both', expand=True)

        ###999
        self.butt_9 = Button(self.frame_789)
        self.butt_9['text'] = '9'
        self.butt_9['font'] = ('Arial', '16', 'bold')
        self.butt_9["command"] = self.key_9
        self.butt_9.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_9.pack(side='left', fill='both', expand=True)

        #frame 0
        self.frame_0 = Frame(self.frame_master)
        self.frame_0.configure(bg='sky blue')
        self.frame_0.pack(fill='both', expand=True)

        ###000
        self.butt_0 = Button(self.frame_0)
        self.butt_0['text'] = '0'
        self.butt_0['font'] = ('Arial', '16', 'bold')
        self.butt_0["command"] = self.key_0
        self.butt_0.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_0.pack(side='left', fill='both', expand=True)

        ###...
        self.butt_ponto = Button(self.frame_0)
        self.butt_ponto['text'] = '.'
        self.butt_ponto['font'] = ('Arial', '16', 'bold')
        self.butt_ponto["command"] = self.key_ponto
        self.butt_ponto.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_ponto.pack(side='left', fill='both', expand=True)

        #frame cancelar
        self.frame_cancelar = Frame(self.frame_master)
        self.frame_cancelar.configure(bg='sky blue')
        self.frame_cancelar.pack(fill='both', expand=True)

        ###cancelar
        self.butt_cancelar = Button(self.frame_cancelar)
        self.butt_cancelar['text'] = 'Cancelar'
        self.butt_cancelar['font'] = ('Arial', '16', 'bold')
        self.butt_cancelar["command"] = self.def_cancelar
        self.butt_cancelar.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_cancelar.pack(side='left', fill='both', expand=True)

        ###aceitar
        self.butt_aceitar = Button(self.frame_cancelar)
        self.butt_aceitar['text'] = 'Aceitar'
        self.butt_aceitar['font'] = ('Arial', '16', 'bold')
        self.butt_aceitar["command"] = self.def_cancelar
        self.butt_aceitar.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_aceitar.pack(side='left', fill='both', expand=True)

        ###_backspace
        self.butt_backspace = Button(self.frame_cancelar)
        self.butt_backspace['text'] = '←'
        self.butt_backspace['font'] = ('Arial', '16', 'bold')
        self.butt_backspace["command"] = self.def_backspace
        self.butt_backspace.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_backspace.pack(side='left', fill='both', expand=True)

    #1234567890
    def key_1(self):
        self.entry_text.insert(END, '1')

    def key_2(self):
        self.entry_text.insert(END, '2')

    def key_3(self):
        self.entry_text.insert(END, '3')

    def key_4(self):
        self.entry_text.insert(END, '4')

    def key_5(self):
        self.entry_text.insert(END, '5')

    def key_6(self):
        self.entry_text.insert(END, '6')

    def key_7(self):
        self.entry_text.insert(END, '7')

    def key_8(self):
        self.entry_text.insert(END, '8')

    def key_9(self):
        self.entry_text.insert(END, '9')

    def key_0(self):
        self.entry_text.insert(END, '0')

    def key_ponto(self):
        self.entry_text.insert(END, '.')

    #cancelar
    def def_cancelar(self):
        self.entry_text.delete(0, END)
        teclado.destroy()

    #espaco
    def def_espaco(self):
        self.entry_text.insert(END, ' ')

    #apagar
    def def_backspace(self):
        pos_fin = len(self.entry_text.get()) -1
        self.entry_text.delete(int(pos_fin))
        print(pos_fin)

    def posicao(self):
        pos_fin = len(self.entry_text.get())
        print(pos_fin)

global pos_fin
global pos_ini

if __name__ == '__main__':
    teclado = Tk()
    teclado.title('Teclado Virtual')
    teclado.geometry('400x250+200+200')
    #teclado.overrideredirect(True)
    teclado.resizable(False, False)
    App_teclado(teclado)
    teclado.mainloop()

