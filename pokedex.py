from tkinter import *
from tkinter import ttk

#importando pillow

from PIL import Image, ImageTk

#importando os dados

from dados import *

# cores ------------------------------------
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha
co6 = '#666666'    #grafite
co7 = '#DCDCDC'    #cinza


#criando janela

janela = Tk()
janela.title('')
janela.geometry('860x580')
janela.configure(bg=co5)

ttk.Separator(janela,orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use('clam')

#criando frame
frame_pokemon = Frame(janela, width=600, height=800, relief='flat',bg=co5)
frame_pokemon.grid(row=0, column=0)

#Criando função dos botões

def trocar_pokemon(i):
    global pok_imagem,imagem_pok

    #TROCANDO A COR DE FUNDO

    frame_pokemon['bg']=pokemon[i] ['Tipo'][3]


    #Tipo de pokemon
    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i] ['Status'][7]

    pok_tipo['text'] = pokemon[i] ['Tipo'][1]
    pok_tipo['bg'] = pokemon[i] ['Status'][7]

    pok_id['text'] = pokemon[i] ['Tipo'][0]
    pok_id['bg'] = pokemon[i] ['Status'][7]  

    pok_imagem = pokemon[i] ['Tipo'][2]
    
    #Adicionando imagem do pokemon
    pok_imagem = Image.open(pok_imagem)
    pok_imagem = pok_imagem.resize((240,240))
    pok_imagem = ImageTk.PhotoImage(pok_imagem)
    imagem_pok = Label(frame_pokemon,image=pok_imagem,relief='flat',bg=pokemon[i] ['Status'][7], fg=co0)
    imagem_pok.place(x=300,y=7)



    #para sobrepor uma label se usa variavel.lift()
    pok_tipo.lift()

    #Status do pokemon

    pok_vida['text'] = pokemon[i] ['Status'][0]
    pok_vida['bg'] = pokemon[i] ['Status'][7]

    pok_ataque['text'] = pokemon[i] ['Status'][1]
    pok_ataque['bg'] = pokemon[i] ['Status'][7]

    pok_defesa['text']  = pokemon[i] ['Status'][2]
    pok_defesa['bg'] = pokemon[i] ['Status'][7]

    pok_spatk['text']  = pokemon[i] ['Status'][3]
    pok_spatk['bg'] = pokemon[i] ['Status'][7]

    pok_spdef['text']  = pokemon[i] ['Status'][4]
    pok_spdef['bg'] = pokemon[i] ['Status'][7]

    pok_velocidade['text'] = pokemon[i] ['Status'][5]
    pok_velocidade['bg'] = pokemon[i] ['Status'][7]

    pok_total['text'] = pokemon[i] ['Status'][6]
    pok_total['bg'] = pokemon[i] ['Status'][7]





    #Habilidades do pokemon

    pok_atk1['text']= pokemon[i] ['Habilidades'][0]
    pok_atk1['bg'] = pokemon[i] ['Status'][7]

    pok_atk2['text']= pokemon[i] ['Habilidades'][1]
    pok_atk2['bg'] = pokemon[i] ['Status'][7]

    pok_atk3['text']= pokemon[i] ['Habilidades'][2]
    pok_atk3['bg'] = pokemon[i] ['Status'][7]
    
    pok_atk4['text']= pokemon[i] ['Habilidades'][3]
    pok_atk4['bg'] = pokemon[i] ['Status'][7]


#Colando o nome do pokemon
pok_nome = Label(frame_pokemon, text='POKEDEX', relief='flat', anchor=CENTER, font=('Verdana 25 bold'),bg=co7)
pok_nome.place(x=12,y=15)

#Colando o ID pokemon
pok_id = Label(frame_pokemon, text='Criada por Miguel', relief='flat', anchor=CENTER, font=('Arial 13 bold'),bg=co5)
pok_id.place(x=15,y=65)

#Colando tipo do pokemon
pok_tipo = Label(frame_pokemon, text='2023', relief='flat', anchor=CENTER, font=('Arial 13 bold'),bg=co5)
pok_tipo.place(x=16,y=95)


#Adicionando imagem do pokemon
pok_imagem = Image.open('images/pokedex.png')
pok_imagem = pok_imagem.resize((238,238))
pok_imagem = ImageTk.PhotoImage(pok_imagem)
imagem_pok = Label(frame_pokemon,image=pok_imagem,relief='flat',bg=co5, fg=co6)
imagem_pok.place(x=300,y=7)

#Criando status
pok_status = Label(frame_pokemon, text='Status:', relief='flat', anchor=CENTER, font=('Verdana 20 bold'),bg=co7)
pok_status.place(x=16,y=310)

#Criando HP
pok_vida = Label(frame_pokemon, text='*', relief='flat', anchor=CENTER, font=('Ivy 13 bold'),bg=co5)
pok_vida.place(x=16,y=360)

#Criando ataque
pok_ataque = Label(frame_pokemon, text='*', relief='flat', anchor=CENTER, font=('Ivy 13 bold'),bg=co5)
pok_ataque.place(x=16,y=390)

#Criando defesa
pok_defesa = Label(frame_pokemon, text='*', relief='flat', anchor=CENTER, font=('Ivy 13 bold'),bg=co5)
pok_defesa.place(x=16,y=420)

#Criando velocidade
pok_velocidade = Label(frame_pokemon, text='*', relief='flat', anchor=CENTER, font=('Ivy 13 bold'),bg=co5)
pok_velocidade.place(x=16,y=450)

#Criando Sp.Atk

pok_spatk = Label(frame_pokemon, text='*', relief='flat', anchor=CENTER, font=('Ivy 13 bold'),bg=co5)
pok_spatk.place(x=16,y=480)

#Criando Sp.Def

pok_spdef = Label(frame_pokemon, text='*', relief='flat', anchor=CENTER, font=('Ivy 13 bold'),bg=co5)
pok_spdef.place(x=16,y=510)

#Criando total
pok_total = Label(frame_pokemon, text='*', relief='flat', anchor=CENTER, font=('Ivy 13 bold'),bg=co5)
pok_total.place(x=16,y=540)

#Criando habilidades
pok_habilidade = Label(frame_pokemon, text='Habilidades:', relief='flat', anchor=CENTER, font=('Verdana 20 bold'),bg=co7)
pok_habilidade.place(x=330,y=310)

#Ataque1
pok_atk1 = Label(frame_pokemon, text='*', relief='flat', anchor=CENTER, font=('Ivy 13 bold'),bg=co5)
pok_atk1.place(x=330,y=360)

#Ataque2
pok_atk2 = Label(frame_pokemon, text='*', relief='flat', anchor=CENTER, font=('Ivy 13 bold'),bg=co5)
pok_atk2.place(x=330,y=390)

#Ataque3
pok_atk3 = Label(frame_pokemon, text='*', relief='flat', anchor=CENTER, font=('Ivy 13 bold'),bg=co5)
pok_atk3.place(x=330,y=420)

#Ataque4
pok_atk4 = Label(frame_pokemon, text='*', relief='flat', anchor=CENTER, font=('Ivy 13 bold'),bg=co5)
pok_atk4.place(x=330,y=450)


#Criando botões / Obs: sempre soma 55 no eixo Y /

#Pikachu

pok1 = Image.open('images/cabeca-pikachu.png')
pok1 = pok1.resize((40,40))
pok1 = ImageTk.PhotoImage(pok1)

imagem_pika = Button(janela,command=lambda:trocar_pokemon('Pikachu'),image=pok1,text='Pikachu',width=150,relief='raised',overrelief=RIDGE,compound=LEFT,anchor=NW,padx=5,font=('Verdana 12 bold'),bg='yellow')
imagem_pika.place(x=600,y=15)

#Gengar

pok2 = Image.open('images/cabeca-gengar.png')
pok2 = pok2.resize((40,40))
pok2 = ImageTk.PhotoImage(pok2)

imagem_gengar = Button(janela,command=lambda:trocar_pokemon('Gengar'),image=pok2,text='Gengar',width=150,relief='raised',overrelief=RIDGE,compound=LEFT,anchor=NW,padx=5,font=('Verdana 12 bold'),bg='MediumPurple')
imagem_gengar.place(x=600,y=70)

#Dragonite

pok3 = Image.open('images/cabeca-dragonite.png')
pok3 = pok3.resize((40,40))
pok3 = ImageTk.PhotoImage(pok3)

imagem_dragonite = Button(janela,command=lambda:trocar_pokemon('Dragonite'),image=pok3,text='Dragonite',width=150,relief='raised',overrelief=RIDGE,compound=LEFT,anchor=NW,padx=5,font=('Verdana 12 bold'),bg='#00CED1')
imagem_dragonite.place(x=600,y=125)

#Gyarados

pok4 = Image.open('images/cabeca-gyarados.png')
pok4 = pok4.resize((40,40))
pok4 = ImageTk.PhotoImage(pok4)

imagem_gyarados = Button(janela,command=lambda:trocar_pokemon('Gyarados'),image=pok4,text='Gyarados',width=150,relief='raised',overrelief=RIDGE,compound=LEFT,anchor=NW,padx=5,font=('Verdana 12 bold'),bg='#00BFFF')
imagem_gyarados.place(x=600,y=180)

#Charmander

pok5 = Image.open('images/cabeca-charmander.png')
pok5 = pok5.resize((40,40))
pok5 = ImageTk.PhotoImage(pok5)

imagem_charmander = Button(janela,command=lambda:trocar_pokemon('Charmander'),image=pok5,text='Charmander',width=150,relief='raised',overrelief=RIDGE,compound=LEFT,anchor=NW,padx=5,font=('Verdana 12 bold'),bg='#FF8C00')
imagem_charmander.place(x=600,y=235)

#Bulbasaur

pok6 = Image.open('images/cabeca-bulbasaur.png')
pok6 = pok6.resize((40,40))
pok6 = ImageTk.PhotoImage(pok6)

imagem_bulbasaur = Button(janela,command=lambda:trocar_pokemon('Bulbasaur'),image=pok6,text='Bulbasaur',width=150,relief='raised',overrelief=RIDGE,compound=LEFT,anchor=NW,padx=5,font=('Verdana 12 bold'),bg='#32CD32')
imagem_bulbasaur.place(x=600,y=290)

janela.mainloop()