import tkinter as tk
from tkinter.font import BOLD
window=tk.Tk()
window.geometry("1500x800")
window.config(bg="#2596be")
window.title("Py os")

#funzioni
def Avvio():
    window.destroy()

    window2=tk.Tk()
    window2.geometry("1500x800")
    window2.config(bg="#2596be")
    window2.title("Py os")

    def Note():
        window3=tk.Tk()
        window3.geometry("900x900")
        window3.config(bg="#fffb05")
        window3.resizable(False, False)

        Scritta=tk.Label(window3, text="Note/Appunti", font=("Arial", 30, BOLD), bg="#fffb05",)
        Scritta.grid(row=1,column=0)
    
        input=tk.Entry(window3, font=("Arial", 30), width=40)
        input.grid(row=2, column=0, pady=30,)
        def salva():
            
            Salvatore=tk.Label(window3, text=input, font=("Arial", 30, BOLD), bg="#fffb05", fg="black")
            Salvatore.grid(row=4, column=0, pady=50)
       
        Scritta=tk.Label(window3, text="Note/Appunti", font=("Arial", 30, BOLD), bg="#fffb05",)
        Scritta.grid(row=1,column=0)
        
       
        tasto_salva=tk.Button(window3, text="Salva", font=("Arial", 30, BOLD), width=20, bg="#fffb05", bd=3, fg="black", command=salva)
        tasto_salva.grid(row=3, column=0,)
    def calcolatrice():
        window4=tk.Tk()
        window4.geometry("900x500")
        window4.title("Calcolatrice")
        def click(tasto):
            if tasto == "=":
                try:
                    risultato = str(eval(display.get()))
                    display.delete(0, tk.END)
                    display.insert(0, risultato)
                except:
                    display.delete(0, tk.END)
                    display.insert(0, "Errore")
            elif tasto == "C":
                display.delete(0, tk.END)
            else:
                display.insert(tk.END, tasto)

        

        display = tk.Entry(window4, font=("Arial", 24), justify="right")
        display.pack(fill="both", padx=10, pady=10)

        # Pulsanti della calcolatrice
        pulsanti = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        frame = tk.Frame(window4)
        frame.pack()

        riga = 0
        colonna = 0

        for p in pulsanti:
            btn = tk.Button(frame, text=p, font=("Arial", 20), width=4, height=2,
                            command=lambda x=p: click(x))
            btn.grid(row=riga, column=colonna, padx=5, pady=5)

            colonna += 1
            if colonna > 3:
                colonna = 0
                riga += 1
    def spegni():
        window2.destroy()
    def Impostazioni(): 
        window5=tk.Tk()
        window5.geometry("900x500")
        window5.config(bg="#0e3f51")
        window5.title("Impostazioni")
        def rosso():
            window2.config(bg="#c81111")
        def giallo():
            window2.config(bg="#b7ff00")
        def blu():
            window2.config(bg="#2200ff")
        def bianco():
            window2.config(bd="#c4af14")
        Sfondo=tk.Label(window5, text="Sfondo", font=("Arial", 30, BOLD), bg="#2596be", )
        Sfondo.grid(row=1,column=0)
        Rosso_pulsante=tk.Button(window5, text="Rosso", font=("Arial", 30, BOLD), bg="#0e3f51", bd=3, width=20, command=rosso)
        Rosso_pulsante.grid(row=2,column=0)
        Giallo_pulsante=tk.Button(window5, text="Giallo", font=("Arial", 30, BOLD), bg="#0e3f51", bd=3, width=20, command=giallo)
        Giallo_pulsante.grid(row=3, column=0)
        blu_pulsante=tk.Button(window5, text="Blu", font=("Arial", 30, BOLD), bg="#0e3f51", bd=3, width=20, command=blu)
        blu_pulsante.grid(row=4, column=0)
        bianco_pulsante=tk.Button(window5, text="Arancione", font=("Arial", 30, BOLD), bg="#0e3f51", bd=3, width=20, command=bianco)
        bianco_pulsante.grid(row=5, column=0)
    def informazioni():
        window6=tk.Tk()
        window6.geometry("1000x500")
        window6.title("Informazioni")
        window6.config(bg="#6f8f6e")
        labella=tk.Label(window6, text="Questo sistema operativo è stato creato per essere utilizzato in ", font=("Arial", 30, BOLD))
        labella.grid(row=1,column=0)
        labella2=tk.Label(window6, text="luoghi attui al lavoro e riutilizzare vecchi computer con  ", font=("Arial", 30, BOLD))
        labella2.grid(row=2,column=0)                 
        labella3=tk.Label(window6, text="windows 3.1 e dargli dinuovo un utilità ", font=("Arial", 30, BOLD))
        labella3.grid(row=3,column=0)
    def giochi():
        window7=tk.Tk()
        window7.title("Giochi")
        window7.geometry("1000x500")
        window7.config(bg="#2d560c")

        gioco=tk.Label(window7, text="I giochi disponibili sono:", font=("Arial", 30, BOLD), bg="#2d560c")
        gioco.grid(row=1, column=0)
        def numero():
            window8=tk.Tk()
            window8.geometry("1000x500")
            window8.title("Indovina il numero")
            window8.config(bg="#2d560c")
            labelloso=tk.Label(window8, text="Indovina il numero da 1 a 5", font=("Arial", 30, BOLD), bg="#2d560c")
            labelloso.grid(row=1,column=0)
            def perso():
                label34=tk.Label(window8, text="Hai perso riprova", font=("Arial", 30, BOLD), bg="#2d560c")
                label34.grid(row=7)
            def vinto():
                labella98=tk.Label(window8, text="Hai vinto!", font=("Arial", 30, BOLD), bg="#2d560c")
                labella98.grid(row=7)
            
            
            numero1=tk.Button(window8, text="1", width=20, bd=3, command=perso)
            numero1.grid(row=2)
            numero2=tk.Button(window8, text="2", width=20, bd=3, command=perso)
            numero2.grid(row=3)
            numero3=tk.Button(window8, text="3", width=20, bd=3, command=vinto)
            numero3.grid(row=4)
            numero4=tk.Button(window8, text="4", width=20, bd=3, command=perso)
            numero4.grid(row=5)
            numero5=tk.Button(window8, text="5", width=20, bd=3, command=perso)
            numero5.grid(row=6)
        
        
        indovinailnumero=tk.Button(window7, text="Indovina il numero", font=("Arial", 30, BOLD), bd=3, command=numero)
        indovinailnumero.grid(row=2,column=0)
    
    Note=tk.Button(window2, text="Appunti/Note", font=("Arial", 30, BOLD), bg="#2596be", width=20, bd=3, command=Note)
    Note.grid(row=1,column=0)

    Calcolatrice=tk.Button(window2, text="Calcolatrice", font=("Arial", 30, BOLD), width=20, bg="#2596be", bd=3, command=calcolatrice)
    Calcolatrice.grid(row=2, column=0)

    esci=tk.Button(window2, text="Spegni", font=("Arial", 30, BOLD), width=20, bg="#2596be", bd=3, command=spegni)
    esci.grid(row=20,column=0,)

    Impostazioni=tk.Button(window2, text="Impostazioni", font=("Arial", 30, BOLD), width=20, bg="#2596be", bd=3, command=Impostazioni)
    Impostazioni.grid(row=4, column=0)

    info=tk.Button(window2, text="Informazioni sistema", font=("Arial", 30, BOLD), width=20, bg="#6f8f6e", bd=3, command=informazioni)
    info.grid(row=21,column=0)

    Giochi=tk.Button(window2, text="Giochi", font=("Arial", 30, BOLD), bd=3, width=20, command=giochi )
    Giochi.grid(row=3, column=0)

    


    

    
    

    
    



#elementi
label_title= tk.Label(window, text="Python os", font=("Arial", 50, BOLD ), bg="#2596be")
label_title.grid(row=1, column=0,pady=300, padx=550)

Start=tk.Button(window, text="Avvia il sistema", font=("Arial", 30, BOLD), bg="#2596be",width=20, bd=3, command=Avvio)
Start.grid(row=2,column=0)





window.mainloop()

#pady verticale padx orizzontale
