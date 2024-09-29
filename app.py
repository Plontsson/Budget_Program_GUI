from tkinter import *
from tkinter import messagebox as mb

class MyGUI:


    def exit_question(self):
        svar = mb.askyesno("Stäng programmet", "Vill du verkligen stänga programmet?")
        if svar == True:
            mb.showinfo("Stäng", "Stänger...")
            self.root.destroy()
        else:
            mb.showinfo("Återvänd", "Återvänder till program")

    def get_budgetpost(self):
        self.get_budgetpost = self.svar_budgetpost.get()
        meddelande = Label(self.val1_frame, text=self.get_budgetpost)
        meddelande.grid()

    def val1(self):
        self.btn_frame.destroy()
        self.val1_frame = Frame(self.root)

        self.val1_frame.columnconfigure(0, weight=1)
        self.val1_frame.columnconfigure(1, weight=1)

        message = Label(self.val1_frame, text="Skriv vilken budgetpost du skulle vilja lägga till:", font="Times, 12")
        message.grid(column= 0, row=0, sticky="ew", padx=5,pady=5)


        self.svar_budgetpost = Entry(self.val1_frame)
        self.svar_budgetpost.grid(column=0, row=1, sticky="ew", padx=5, pady=5)

        btn = Button(self.val1_frame, text="Visa entry", font="Times, 12", command=self.get_budgetpost)
        btn.grid(column=0, row=2, sticky="ew", padx=5, pady=5)
        
        
        
        self.val1_frame.pack()


    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x500")

        self.btn_frame = Frame(self.root)

        self.btn_frame.columnconfigure(0, weight= 1)
        self.btn_frame.columnconfigure(1, weight= 3)

        self.btn_1 = Button(self.btn_frame, text="Lägg till ny budgetpost", font="Times, 12", command=self.val1)
        self.btn_1.grid(column= 0, row= 0, sticky="ew", padx= 5, pady= 5)

        self.btn_2 = Button(self.btn_frame, text= "Ändra budgetpost", font="Times, 12")
        self.btn_2.grid(column= 0, row= 1, sticky="ew" , padx= 5, pady= 5)

        self.btn_3 = Button(self.btn_frame, text="Skriv ut budget", font="Times, 12")
        self.btn_3.grid(column= 0, row= 2, padx=5, pady= 5, sticky="ew")

        self.btn_4 = Button(self.btn_frame, text="Avsluta program", font="Times, 12", command=self.exit_question)
        self.btn_4.grid(column= 0, row= 3, padx=5, pady=5, sticky="ew")

        self.btn_frame.pack()







        self.root.mainloop()

MyGUI()