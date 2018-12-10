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
        self.frame_1 = Frame(self.frame_master)
        self.frame_1.configure(bg='sky blue')
        self.frame_1.pack(fill='both', expand=True)

        ###111
        self.butt_1 = Button(self.frame_1)
        self.butt_1['text'] = '1'
        self.butt_1['font'] = ('Arial', '16', 'bold')
        self.butt_1["command"] = self.key_1
        self.butt_1.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_1.pack(side='left', fill='both', expand=True)

        ###222
        self.butt_2 = Button(self.frame_1)
        self.butt_2['text'] = '2'
        self.butt_2['font'] = ('Arial', '16', 'bold')
        self.butt_2["command"] = self.key_2
        self.butt_2.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_2.pack(side='left', fill='both', expand=True)

        ###333
        self.butt_3 = Button(self.frame_1)
        self.butt_3['text'] = '3'
        self.butt_3['font'] = ('Arial', '16', 'bold')
        self.butt_3["command"] = self.key_3
        self.butt_3.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_3.pack(side='left', fill='both', expand=True)

        ###444
        self.butt_4 = Button(self.frame_1)
        self.butt_4['text'] = '4'
        self.butt_4['font'] = ('Arial', '16', 'bold')
        self.butt_4["command"] = self.key_4
        self.butt_4.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_4.pack(side='left', fill='both', expand=True)

        ###555
        self.butt_5 = Button(self.frame_1)
        self.butt_5['text'] = '5'
        self.butt_5['font'] = ('Arial', '16', 'bold')
        self.butt_5["command"] = self.key_5
        self.butt_5.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_5.pack(side='left', fill='both', expand=True)

        ###666
        self.butt_6 = Button(self.frame_1)
        self.butt_6['text'] = '6'
        self.butt_6['font'] = ('Arial', '16', 'bold')
        self.butt_6["command"] = self.key_6
        self.butt_6.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_6.pack(side='left', fill='both', expand=True)

        ###777
        self.butt_7 = Button(self.frame_1)
        self.butt_7['text'] = '7'
        self.butt_7['font'] = ('Arial', '16', 'bold')
        self.butt_7["command"] = self.key_7
        self.butt_7.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_7.pack(side='left', fill='both', expand=True)

        ###888
        self.butt_8 = Button(self.frame_1)
        self.butt_8['text'] = '8'
        self.butt_8['font'] = ('Arial', '16', 'bold')
        self.butt_8["command"] = self.key_8
        self.butt_8.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_8.pack(side='left', fill='both', expand=True)

        ###999
        self.butt_9 = Button(self.frame_1)
        self.butt_9['text'] = '9'
        self.butt_9['font'] = ('Arial', '16', 'bold')
        self.butt_9["command"] = self.key_9
        self.butt_9.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_9.pack(side='left', fill='both', expand=True)

        ###000
        self.butt_0 = Button(self.frame_1)
        self.butt_0['text'] = '0'
        self.butt_0['font'] = ('Arial', '16', 'bold')
        self.butt_0["command"] = self.key_0
        self.butt_0.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_0.pack(side='left', fill='both', expand=True)

        #frame qwe
        self.frame_q = Frame(self.frame_master)
        self.frame_q.configure(bg='sky blue')
        self.frame_q.pack(fill='both', expand=True)

        ###QQQ
        self.butt_q = Button(self.frame_q)
        self.butt_q['text'] = 'Q'
        self.butt_q['font'] = ('Arial', '16', 'bold')
        self.butt_q["command"] = self.key_q
        self.butt_q.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_q.pack(side='left', fill='both', expand=True)

        ###WWW
        self.butt_w = Button(self.frame_q)
        self.butt_w['text'] = 'W'
        self.butt_w['font'] = ('Arial', '16', 'bold')
        self.butt_w["command"] = self.key_w
        self.butt_w.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_w.pack(side='left', fill='both', expand=True)

        ###EEE
        self.butt_e = Button(self.frame_q)
        self.butt_e['text'] = 'E'
        self.butt_e['font'] = ('Arial', '16', 'bold')
        self.butt_e["command"] = self.key_e
        self.butt_e.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_e.pack(side='left', fill='both', expand=True)

        ###RRR
        self.butt_r = Button(self.frame_q)
        self.butt_r['text'] = 'R'
        self.butt_r['font'] = ('Arial', '16', 'bold')
        self.butt_r["command"] = self.key_r
        self.butt_r.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_r.pack(side='left', fill='both', expand=True)

        ###TTT
        self.butt_t = Button(self.frame_q)
        self.butt_t['text'] = 'T'
        self.butt_t['font'] = ('Arial', '16', 'bold')
        self.butt_t["command"] = self.key_t
        self.butt_t.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_t.pack(side='left', fill='both', expand=True)

        ###YYY
        self.butt_y = Button(self.frame_q)
        self.butt_y['text'] = 'Y'
        self.butt_y['font'] = ('Arial', '16', 'bold')
        self.butt_y["command"] = self.key_y
        self.butt_y.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_y.pack(side='left', fill='both', expand=True)

        ###UUU
        self.butt_u = Button(self.frame_q)
        self.butt_u['text'] = 'U'
        self.butt_u['font'] = ('Arial', '16', 'bold')
        self.butt_u["command"] = self.key_u
        self.butt_u.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_u.pack(side='left', fill='both', expand=True)

        ###III
        self.butt_i = Button(self.frame_q)
        self.butt_i['text'] = 'I'
        self.butt_i['font'] = ('Arial', '16', 'bold')
        self.butt_i["command"] = self.key_i
        self.butt_i.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_i.pack(side='left', fill='both', expand=True)

        ###OOO
        self.butt_o = Button(self.frame_q)
        self.butt_o['text'] = 'O'
        self.butt_o['font'] = ('Arial', '16', 'bold')
        self.butt_o["command"] = self.key_o
        self.butt_o.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_o.pack(side='left', fill='both', expand=True)

        ###PPP
        self.butt_p = Button(self.frame_q)
        self.butt_p['text'] = 'P'
        self.butt_p['font'] = ('Arial', '16', 'bold')
        self.butt_p["command"] = self.key_p
        self.butt_p.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_p.pack(side='left', fill='both', expand=True)

        #frame asd
        self.frame_a = Frame(self.frame_master)
        self.frame_a.configure(bg='sky blue')
        self.frame_a.pack(fill='both', expand=True)

        ###AAA
        self.butt_a = Button(self.frame_a)
        self.butt_a['text'] = 'A'
        self.butt_a['font'] = ('Arial', '16', 'bold')
        self.butt_a["command"] = self.key_a
        self.butt_a.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_a.pack(side='left', fill='both', expand=True)

        ###SSS
        self.butt_s = Button(self.frame_a)
        self.butt_s['text'] = 'S'
        self.butt_s['font'] = ('Arial', '16', 'bold')
        self.butt_s["command"] = self.key_s
        self.butt_s.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_s.pack(side='left', fill='both', expand=True)

        ###DDD
        self.butt_d = Button(self.frame_a)
        self.butt_d['text'] = 'D'
        self.butt_d['font'] = ('Arial', '16', 'bold')
        self.butt_d["command"] = self.key_d
        self.butt_d.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_d.pack(side='left', fill='both', expand=True)

        ###FFF
        self.butt_f = Button(self.frame_a)
        self.butt_f['text'] = 'F'
        self.butt_f['font'] = ('Arial', '16', 'bold')
        self.butt_f["command"] = self.key_f
        self.butt_f.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_f.pack(side='left', fill='both', expand=True)

        ###GGG
        self.butt_g = Button(self.frame_a)
        self.butt_g['text'] = 'G'
        self.butt_g['font'] = ('Arial', '16', 'bold')
        self.butt_g["command"] = self.key_g
        self.butt_g.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_g.pack(side='left', fill='both', expand=True)

        ###HHH
        self.butt_h = Button(self.frame_a)
        self.butt_h['text'] = 'H'
        self.butt_h['font'] = ('Arial', '16', 'bold')
        self.butt_h["command"] = self.key_h
        self.butt_h.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_h.pack(side='left', fill='both', expand=True)

        ###JJJ
        self.butt_j = Button(self.frame_a)
        self.butt_j['text'] = 'J'
        self.butt_j['font'] = ('Arial', '16', 'bold')
        self.butt_j["command"] = self.key_j
        self.butt_j.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_j.pack(side='left', fill='both', expand=True)

        ###KKK
        self.butt_k = Button(self.frame_a)
        self.butt_k['text'] = 'K'
        self.butt_k['font'] = ('Arial', '16', 'bold')
        self.butt_k["command"] = self.key_k
        self.butt_k.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_k.pack(side='left', fill='both', expand=True)

        ###LLL
        self.butt_l = Button(self.frame_a)
        self.butt_l['text'] = 'L'
        self.butt_l['font'] = ('Arial', '16', 'bold')
        self.butt_l["command"] = self.key_l
        self.butt_l.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_l.pack(side='left', fill='both', expand=True)

        ###ÇÇÇ
        self.butt_ç = Button(self.frame_a)
        self.butt_ç['text'] = 'Ç'
        self.butt_ç['font'] = ('Arial', '16', 'bold')
        self.butt_ç["command"] = self.key_ç
        self.butt_ç.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_ç.pack(side='left', fill='both', expand=True)

        #frame zxc
        self.frame_z = Frame(self.frame_master)
        self.frame_z.configure(bg='sky blue')
        self.frame_z.pack(fill='both', expand=True)

        ###ZZZ
        self.butt_z = Button(self.frame_z)
        self.butt_z['text'] = 'Z'
        self.butt_z['font'] = ('Arial', '16', 'bold')
        self.butt_z["command"] = self.key_z
        self.butt_z.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_z.pack(side='left', fill='both', expand=True)

        ###XXX
        self.butt_x = Button(self.frame_z)
        self.butt_x['text'] = 'X'
        self.butt_x['font'] = ('Arial', '16', 'bold')
        self.butt_x["command"] = self.key_x
        self.butt_x.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_x.pack(side='left', fill='both', expand=True)

        ###CCC
        self.butt_c = Button(self.frame_z)
        self.butt_c['text'] = 'C'
        self.butt_c['font'] = ('Arial', '16', 'bold')
        self.butt_c["command"] = self.key_c
        self.butt_c.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_c.pack(side='left', fill='both', expand=True)

        ###VVV
        self.butt_v = Button(self.frame_z)
        self.butt_v['text'] = 'V'
        self.butt_v['font'] = ('Arial', '16', 'bold')
        self.butt_v["command"] = self.key_v
        self.butt_v.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_v.pack(side='left', fill='both', expand=True)

        ###BBB
        self.butt_b = Button(self.frame_z)
        self.butt_b['text'] = 'B'
        self.butt_b['font'] = ('Arial', '16', 'bold')
        self.butt_b["command"] = self.key_b
        self.butt_b.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_b.pack(side='left', fill='both', expand=True)

        ###NNN
        self.butt_n = Button(self.frame_z)
        self.butt_n['text'] = 'N'
        self.butt_n['font'] = ('Arial', '16', 'bold')
        self.butt_n["command"] = self.key_n
        self.butt_n.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_n.pack(side='left', fill='both', expand=True)

        ###MMM
        self.butt_m = Button(self.frame_z)
        self.butt_m['text'] = 'M'
        self.butt_m['font'] = ('Arial', '16', 'bold')
        self.butt_m["command"] = self.key_m
        self.butt_m.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_m.pack(side='left', fill='both', expand=True)

        ###,,,
        self.butt_virgula = Button(self.frame_z)
        self.butt_virgula['text'] = ','
        self.butt_virgula['font'] = ('Arial', '16', 'bold')
        self.butt_virgula["command"] = self.key_virgula
        self.butt_virgula.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_virgula.pack(side='left', fill='both', expand=True)

        ###...
        self.butt_ponto = Button(self.frame_z)
        self.butt_ponto['text'] = '.'
        self.butt_ponto['font'] = ('Arial', '16', 'bold')
        self.butt_ponto["command"] = self.key_ponto
        self.butt_ponto.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_ponto.pack(side='left', fill='both', expand=True)

        ###:::
        self.butt_dois_ponto = Button(self.frame_z)
        self.butt_dois_ponto['text'] = ':'
        self.butt_dois_ponto['font'] = ('Arial', '16', 'bold')
        self.butt_dois_ponto["command"] = self.key_dois_ponto
        self.butt_dois_ponto.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_dois_ponto.pack(side='left', fill='both', expand=True)

        #frame espaco
        self.frame_espaco = Frame(self.frame_master)
        #self.frame_espaco.configure(bg='sky blue')
        self.frame_espaco.pack(fill='both', expand=True)

        ###cancelar
        self.butt_cancelar = Button(self.frame_espaco)
        self.butt_cancelar['text'] = 'Cancelar'
        self.butt_cancelar['font'] = ('Arial', '16', 'bold')
        self.butt_cancelar["command"] = self.def_cancelar
        self.butt_cancelar.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_cancelar.pack(side='left', fill='both', expand=True)

        ###espaco
        self.butt_espaco = Button(self.frame_espaco)
        self.butt_espaco['text'] = 'Espaco'
        self.butt_espaco['font'] = ('Arial', '16', 'bold')
        self.butt_espaco["command"] = self.def_espaco
        self.butt_espaco.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_espaco.pack(side='left', fill='both', expand=True)

        ###aceitar
        self.butt_aceitar = Button(self.frame_espaco)
        self.butt_aceitar['text'] = 'Aceitar'
        self.butt_aceitar['font'] = ('Arial', '16', 'bold')
        self.butt_aceitar["command"] = self.def_cancelar
        self.butt_aceitar.configure(bg='sky blue',
                                     activebackground='sky blue')
        self.butt_aceitar.pack(side='left', fill='both', expand=True)

        ###_backspace
        self.butt_backspace = Button(self.frame_espaco)
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

    #qwertyuiop
    def key_q(self):
        self.entry_text.insert(END, 'Q')

    def key_w(self):
        self.entry_text.insert(END, 'W')

    def key_e(self):
        self.entry_text.insert(END, 'E')

    def key_r(self):
        self.entry_text.insert(END, 'R')

    def key_t(self):
        self.entry_text.insert(END, 'T')

    def key_y(self):
        self.entry_text.insert(END, 'Y')

    def key_u(self):
        self.entry_text.insert(END, 'U')

    def key_i(self):
        self.entry_text.insert(END, 'I')

    def key_o(self):
        self.entry_text.insert(END, 'O')

    def key_p(self):
        self.entry_text.insert(END, 'P')

    #asdfghjklç
    def key_a(self):
        self.entry_text.insert(END, 'A')

    def key_s(self):
        self.entry_text.insert(END, 'S')

    def key_d(self):
        self.entry_text.insert(END, 'D')

    def key_f(self):
        self.entry_text.insert(END, 'F')

    def key_g(self):
        self.entry_text.insert(END, 'G')

    def key_h(self):
        self.entry_text.insert(END, 'H')

    def key_j(self):
        self.entry_text.insert(END, 'J')

    def key_k(self):
        self.entry_text.insert(END, 'K')

    def key_l(self):
        self.entry_text.insert(END, 'L')

    def key_ç(self):
        self.entry_text.insert(END, 'Ç')

    #zxcvbnm
    def key_z(self):
        self.entry_text.insert(END, 'Z')

    def key_x(self):
        self.entry_text.insert(END, 'X')

    def key_c(self):
        self.entry_text.insert(END, 'C')

    def key_v(self):
        self.entry_text.insert(END, 'V')

    def key_b(self):
        self.entry_text.insert(END, 'B')

    def key_n(self):
        self.entry_text.insert(END, 'N')

    def key_m(self):
        self.entry_text.insert(END, 'M')
        self.posicao()

    def key_virgula(self):
        self.entry_text.insert(END, ',')

    def key_ponto(self):
        self.entry_text.insert(END, '.')

    def key_dois_ponto(self):
        self.entry_text.insert(END, ':')

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
    #teclado.geometry('400x250+200+200')
    #teclado.overrideredirect(True)
    teclado.resizable(False, False)
    App_teclado(teclado)
    teclado.mainloop()

