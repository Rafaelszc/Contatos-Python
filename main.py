import customtkinter as tk
from PIL import Image
import maindb

#características da janela
janela = tk.CTk()
janela.geometry('500x700')
janela.title('Contatos')
janela.resizable(False, False)
tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')

main = tk.CTkFrame(master=janela, width=500, height=700)
main.pack()

lupa = Image.open("fotos/lupa.png")
user = Image.open("fotos/user.png")
seta = Image.open("fotos/seta.png")
setaback = Image.open("fotos/setaback.png")
add = Image.open("fotos/add.png")

q = 0
def qmais():
    global q
    q += 1
    return q
def qmenos():
    global q 
    q -= 1
    return q
def verificarq(num):
    global q
    if q >= num-1:
        q = -1
        return q
    elif q <= -1:
        q = 1
        return q
    else:
        pass

nome_var, num_var, desc_var = tk.StringVar(), tk.StringVar(), tk.StringVar()

def tela2():
    tela2 = tk.CTkFrame(master=main, width=500, height=700, fg_color='#212121')
    tela2.pack()

    frame2 = tk.CTkFrame(master=main, width=460, height=680, corner_radius=30)
    frame2.place(x = 250, y = 350, anchor = 'center')
    
    foto = tk.CTkLabel(master=frame2, text='', image=tk.CTkImage(user, user, size=(50, 50)), corner_radius=30)
    foto.place(x = 60, y= 60, anchor = 'center')

    entradanome = tk.CTkEntry(master=frame2, placeholder_text='Nome...', width=250, height=30, textvariable=nome_var)
    entradanome.place(x= 100, y= 50)
    tnome = tk.CTkLabel(master=frame2, text='Nome')
    tnome.place(x= 360, y= 50)

    entradanumero = tk.CTkEntry(master=frame2, placeholder_text='Número...', width=250, height=30, textvariable=num_var)
    entradanumero.place(x= 100, y= 90)
    tnum = tk.CTkLabel(master=frame2, text='Número')
    tnum.place(x= 360, y= 90)
    
    entradadesc = tk.CTkEntry(master=frame2, placeholder_text='Número...', width=250, height=30, textvariable=desc_var)
    entradadesc.place(x= 100, y= 130)
    tdesc = tk.CTkLabel(master=frame2, text='Descrição')
    tdesc.place(x= 360, y= 130)

    adicionar = tk.CTkButton(master=frame2, fg_color='transparent', hover_color='#383838', corner_radius=30, width=35, height=35, image=tk.CTkImage(add, add), text='', command=lambda: (tela2.destroy(), frame2.destroy(), maindb.verificar(nome_var.get(), num_var.get(), desc_var.get())))
    adicionar.place(x = 400, y= 620)



#principal->frame1
frame1 = tk.CTkFrame(master=main, width=460, height=650, corner_radius=30)
frame1.place(x = 250, y = 370, anchor = 'center')

adicionar = tk.CTkButton(master=frame1, fg_color='transparent', hover_color='#383838', text='', corner_radius=30, width=20, height=20, image=tk.CTkImage(add, add), command=lambda: (tela2()))
adicionar.place(x = 400, y= 580)

#principal->frame1->frame3
frame3= tk.CTkFrame(master=frame1, width=320, height=420, corner_radius=30)
frame3.place(x = 225, y = 390, anchor = 'center')
try:
    imagem = tk.CTkLabel(master=frame1, text='', image=tk.CTkImage(user, user, size=(80, 80)), corner_radius=30)
    imagem.place(x = 80, y= 80, anchor = 'center')

    user_nome = tk.CTkLabel(master=frame1, text=maindb.mostrar(q)[0], font=('Arial', 40))
    user_nome.place(x = 200, y = 60)

    user_num = tk.CTkLabel(master=frame3, text=maindb.mostrar(q)[1], font=('Arial', 25))
    user_num.pack(padx = 20, pady = 20)

    back = tk.CTkButton(master=frame1, text='', image=tk.CTkImage(setaback, setaback), width= 20, height= 20, corner_radius=40, fg_color='transparent', hover_color='#383838', command= lambda: (verificarq(maindb.mostrar('quantidade')),qmenos(), user_num.configure(text= maindb.mostrar(q)[1]), user_nome.configure(text= maindb.mostrar(q)[0])))
    back.place(x = 30, y= 325, anchor='center')

    next = tk.CTkButton(master=frame1, text='', image=tk.CTkImage(seta, seta), width= 20, height= 20, corner_radius=40, fg_color='transparent', hover_color='#383838', command= lambda: (verificarq(maindb.mostrar('quantidade')), qmais(), user_num.configure(text= maindb.mostrar(q)[1]), user_nome.configure(text= maindb.mostrar(q)[0])))
    next.place(x = 430, y= 325, anchor='center')

    

except:
    imagem.destroy()

    nomeerro = tk.CTkLabel(master=frame3, text='Nenhum número adcionado.\n Crie um novo contato e reinicie o programa', font=('Arial', 20))
    nomeerro.pack(padx= 20, pady= 20)
    

#principal
pesquisa = tk.CTkEntry(master=main, width=400,height=30, placeholder_text= 'Pesquisa...')
pesquisa.place(x = 10, y = 7)
bpesquisar = tk.CTkButton(master=main, width=25, height=35, corner_radius=35, text='', fg_color='transparent', hover_color='#383838', image=tk.CTkImage(lupa, lupa), command=lambda: (user_nome.configure(text=maindb.pesquisar(pesquisa.get())[0]), user_num.configure(text=maindb.pesquisar(pesquisa.get())[1])))
bpesquisar.place(x = 460, y = 23, anchor = 'center')

janela.mainloop()
