from os import *
from tkinter import *
import webbrowser

janela4 = Tk()   
janela4.title('Login')
  
texto24 = Label(janela4, text="XERETA", font='Arial 25 bold italic', width=10, fg='#0E2954', bg='#FF8551')
texto24.grid(column=1, row=0)
 
texto20 = Label(janela4, text="Login:", bg='#FF8551')
texto20.grid(column=0, row=1)
 
entrada5 = Entry(janela4, width=22)
entrada5.grid(column=1, row=1)
login = entrada5.get()
login1 = "Caio"

texto21 = Label(janela4, text="Senha:", bg='#FF8551')
texto21.grid(column=0, row=2)
 
entrada6 = Entry(janela4, width=22)
entrada6.grid(column=1, row=2)
senha = entrada6.get()
senha1 = "123"

def entrar():
    if entrada5.get() == login1 and entrada6.get() == senha1:
          texto23 = Label(janela4, text="Login efetuado com sucesso!", fg='#1A5D1A', bg='#FF8551')
          texto23.grid(column=1, row=4)
           
          janela = Tk()   
          janela.title('Xereta')
            
          texto14 = Label(janela, text="XERETA", font='Arial 25 bold italic', width=10, fg='#0E2954', bg='#FF8551')
          texto14.grid(column=1, row=0)

          ##########   serviços
          def sevicos():
              texto3 = Label(janela, text=('Para mais informações ligue para: 3261-7000'), bg='#FF8551')
              texto3.grid(column=2, row=2)

              texto6 = Label(janela, text="", bg='#FF8551')
              texto6.grid(column=3, row=8)
              
          botao = Button(janela, command=sevicos, text="Serviços", width=10)
          botao.grid(column=1, row=2)

          ##########   produtos
          def produtos():
                texto8 = Label(janela, text=('Para ver produtos entre no site: https://www.xeretanet.com.br/'), bg='#FF8551')
                texto8.grid(column=2, row=3)
                
          botao1 = Button(janela, command=produtos, text="Produtos", width=10)
          botao1.grid(column=1, row=3)

          ##########   elasticos
          def elasticos():
               # webbrowser.open('https://www.xeretanet.com.br/categoria/4115528/elasticos/')
                texto7 = Label(janela, text=('Bicos / Rendas Estreitas / Debruns / Viéses / Bases / Cintura'), bg='#FF8551')
                texto7.grid(column=2, row=4)
                
               
          botao2 = Button(janela, command=elasticos, text="Elásticos", width=10)
          botao2.grid(column=1, row=4)

          texto = Label(janela, text="", bg='#FF8551')
          texto.grid(column=0, row=0)

          ##########   entrega
          def janela_entrega():
           texto9 = Label(janela, text=('Ligue para o nosso entregador: 99971-7771' ), bg='#FF8551')
           texto9.grid(column=2, row=5)

           janela1 = Tk()
           janela1.title('')
           
           texto16 = Label(janela1, text=('Produtos'))
           texto16.grid(column=0, row=4)
           
           entrada4 = Entry(janela1, width = 20)
           entrada4.grid(column=1, row=4)

           texto15 = Label(janela1, text=('Nome'))
           texto15.grid(column=0, row=0)

           entrada3 = Entry(janela1, width = 20)
           entrada3.grid(column=1, row=0)

           texto11 = Label(janela1, text=('Endereço'))
           texto11.grid(column=0, row=1)
           
           entrada = Entry(janela1, width = 20)
           entrada.grid(column=1, row=1)

           texto12 = Label(janela1, text=('Cidade'))
           texto12.grid(column=0, row=2)
           
           entrada1 = Entry(janela1, width = 20)
           entrada1.grid(column=1, row=2)

           texto13 = Label(janela1, text=('Adicional'))
           texto13.grid(column=0, row=3)
           
           entrada2 = Entry(janela1, width = 20)
           entrada2.grid(column=1, row=3)

           def dados():
                print("     Nome: ", entrada3.get())
                print(" Endereço: ", entrada.get())
                print("   Cidade: ", entrada1.get())
                print("Adicional: ", entrada2.get())
                print(" Produtos: ", entrada4.get())
           botao8 = Button(janela1, command=dados, text="Enviar")
           botao8.grid(column=1, row=5)

           janela1.mainloop()



           def entrega():
                texto9 = Label(janela, text=('Ligue para o nosso entregador: 99971-7771'), bg='#FF8551')
                texto9.grid(column=2, row=5)
                
          botao4 = Button(janela, command=janela_entrega, text="Entrega", width=10)
          botao4.grid(column=1, row=5)

          #########   site
          def site():
                webbrowser.open('https://www.xeretanet.com.br/')
                texto10 = Label(janela, text=('Conheça nosso site: https://www.xeretanet.com.br/'), bg='#FF8551')
                texto10.grid(column=2, row=6)
                
          botao5 = Button(janela, command=site,  text="Site", width=10)
          botao5.grid(column=1, row=6)


          #########   obrigado
          texto2 = Label(janela, text="Gostou do Atendimento?", bg='#FF8551')
          texto2.grid(column=1, row=7)

          texto1 = Label(janela, text="", bg='#FF8551')
          texto1.grid(column=0, row=8)
              

          def executar():
                texto11 = Label(janela, text=('Obrigado pela preferência!!!'), bg='#FF8551')
                texto11.grid(column=2, row=8)

          botao7 = Button(janela, command=executar, text="Claro", width=10)
          botao7.grid(column=1, row=8)

          texto5 = Label(janela, text="", bg='#FF8551')
          texto5.grid(column=0, row=8)

          texto4 = Label(janela, text="", bg='#FF8551')
          texto4.grid(column=0, row=9)

          janela.config(bg='#FF8551')

          janela.geometry = ('250x250')
          janela.mainloop()
        
    else:  texto22 = Label(janela4, text="Login ou senha errado!", fg='#D71313', width=25, bg='#FF8551')
    texto22.grid(column=1, row=4)
         
botao20 = Button(janela4, command=entrar, text='Entrar')
botao20.grid(column=1, row=3)

janela4.config(bg='#FF8551')
janela4.geometry('250x150')
janela4.mainloop()

