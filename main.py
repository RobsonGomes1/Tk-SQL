import sqlite3
from  tkinter import *

#BD
conn = sqlite3.connect('db/databa.db')
c = conn.cursor()


def consultar(s):
    lb_dados.configure(image='')

    conn = sqlite3.connect('db/databa.db')
    c = conn.cursor()

    dado = c.execute(f"SELECT * FROM FUNCIONARIOS WHERE NOME = '{s}';").fetchall()
    print(dado)
    
    if dado[0][4] == 1:
        lb_dados.configure(image=img_rh)
    elif dado[0][4] == 2:
        lb_dados.configure(image=img_ti)
    elif dado[0][4] == 3:
        lb_dados.configure(image=img_adm)

    conn.close()

root = Tk()
root.title('Cadastro de Clientes')
root.configure(background='#ffffff')
root.resizable(0, 0)

v_nome = StringVar()

img_adm = PhotoImage(file='img/adm.png')
img_rh = PhotoImage(file='img/rh.png')
img_ti = PhotoImage(file='img/ti.png')

lb_letreiro = Label(root, text='Cadastro de Clientes', font=('Arial', 20), bg='#ffffff')
lb_nome = Label(root, text='Nome:', font=('Arial', 12), bg='#ffffff')
txt_nome = Entry(root, width=30, font=('Arial', 12),textvariable=v_nome)
bt_consultar = Button(root, text='consultar', font=('Arial', 12), bg='#ffffff', command=lambda: consultar(v_nome.get()))
lb_dados = Label(root, font=('Arial', 12), bg='#ffffff')

lb_letreiro.grid(row=0, column=0, columnspan=2, pady=10)
lb_nome.grid(row=1, column=0, sticky=W, padx=10, pady=10)
txt_nome.grid(row=1, column=1, sticky=W, padx=10, pady=10)
bt_consultar.grid(row=3, column=0, columnspan=2, pady=10)
lb_dados.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
