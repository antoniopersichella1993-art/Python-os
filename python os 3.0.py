import tkinter as tk
from tkinter.font import BOLD, ITALIC
root=tk.Tk()
root.geometry("700x300")
root.config(bg="#302B2B")
root.resizable(False, False)
root.title("Login page")




def note():
    root2=tk.Tk()
    root2.geometry("1000x800")
    root2.title("Deocumenti")
    root2.config(bg="#d6eb34")
    root2.attributes("-topmost", True)
  
    areaditesto= tk.Text(root2, width=80, height=30, font=("Arial", 17),) #metodo per casella per scrivere testo
    areaditesto.pack()
    salva=tk.Button(root2, text="Salva", font=("Arial", 25), bg="#d6eb34", command=salva) 
    salva.pack(pady=10) #inserire il bottone nonostante la casella di testo .pack()

def calcolatric():
    root3=tk.Tk()
    root3.title("Calcolatrice Lite")
    root3.geometry("300x150")
    root3.attributes("-topmost", True)
    entry= tk.Entry(root3, text="", font=("Arial", 20))
    entry.pack()
    risultato = tk.Label(root3, text="", font=("Arial", 20))
    risultato.pack()

    tk.Button(root3, text="=", font=("Arial", 20), command=lambda: risultato.config(text=eval(entry.get()))).pack()


    
    



def registrati():
    
    root1=tk.Tk()
    root1.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root1.title("Super Lite os")
    root1.config(bg="#34dbeb")
    root1.overrideredirect(True)

    
    
    

    def impostazioni1():
        root4=tk.Tk()
        root4.attributes("-topmost", True)
        root4.title("Impostazioni Lite")
        root4.config(bg="#637566")
        root4.geometry("1000x500")
    
        impo=tk.Label(root4, text="Impostazioni:", font=("Arial", 30, BOLD), bg="#637566", ).grid(row=0, column=0)
        sfondi=tk.Label(root4, text="Sfondi:", font=("Arial", 30), width=15, bg="#637566").grid(row=1, column=0)
        rosso=tk.Button(root4, text="Rosso", font=("Arial", 25), bd=1, command=lambda: root1.config(bg="#B20707")).grid(row=2, column=0)
        nero=tk.Button(root4, text="Nero", font=("Arial", 25), bd=1, command=lambda: root1.config(bg="#000000")).grid(row=3, column=0)
        bianco=tk.Button(root4, text="Bianco", font=("Arial", 25), bd=1, command=lambda: root1.config(bg="#FFFFFF")).grid(row=4, column=0)
        fabbrica=tk.Button(root4, text="Colore predefinito", font=("Arial", 25), bd=1, command=lambda: root1.config(bg="#34dbeb")).grid(row=5, column=0)
    def terminal():
        root5=tk.Toplevel()
        root5.title("Terminale lite")
        root5.geometry("1000x500")
        root5.attributes("-topmost", True)
        root5.config(bg="#000000")

        output = tk.Label(root5, text="", font=("Consolas",14), bg="#000000", fg="white")
        output.grid(row=0, column=0)
        input1 = tk.Entry(root5)
        input1.grid(row=1,column=0)
        
        def invio(event=None):
            testo = input1.get()
            if testo == "help":
                output.config(text="Benvenuto in Lite terminal!!, per ora i comandi disponibili sono: help, indovina il numero ")
            

            else:
                output.config(text="comando non trovato")
            input1.delete(0, tk.END)
        
        tast=tk.Button(root5, text="invio",font=("Arial", 20), width=15, command=invio).grid(row=2, column=0)
        
            
        
        


    Note=tk.Button(root1, text="Deocumenti", font=("Arial", 30), bd=1, width=15, command=note).grid(row=0, column=0)
    calcolatrice=tk.Button(root1, text="Calcolatrice", font=("Arial", 30), bd=1, width=15, command=calcolatric).grid(row=1, column=0)
    impostazioni=tk.Button(root1, text="impostazioni", font=("Arial", 30), bd=1, width=15, command=impostazioni1).grid(row=2, column=0)
    spegni=tk.Button(root1, text="Spegni sistema", font=("Arial", 30), width=15, bd=1, command=lambda: root1.destroy()).grid(row=3, column=0)
    terminale=tk.Button(root1, text="Terminale", font=("Arial", 30), width=15, bd=1,command=terminal).grid(row=4, column=0)
    




#login page
Login=tk.Label(root, text="Registrati", font=("Arial", 30, ITALIC), bg="#302B2B", fg="white").grid(row=0,column=0, )
Label1=tk.Label(root, text="Nome", font=("Arial", 30), bg="#302B2B", width=10 , fg="white").grid(row=1,column=0)
input=tk.Entry(root, font=("Arial", 30),width=20).grid(row=1,column=1,)
label2=tk.Label(root, text="Cognome", font=("Arial", 30), bg="#302B2B", width=10, fg="white").grid(row=2 , column=0)
input2=tk.Entry(root, font=("Arial", 30), width=20).grid(row=2, column=1)

Invio=tk.Button(root, text="Registrati", font=("Arial", 30), width=19, bd=0, command=registrati).grid(row=3, column=1)




root.mainloop()