from tkinter import *
from tkinter import messagebox as mb

class MyGUI:

    def exit_question(self): #function to ask if user wants to close program
        svar = mb.askyesno("Stäng programmet", "Vill du verkligen stänga programmet?") #using tkinter yesno 
        if svar == True:
            mb.showinfo("Stäng", "Stänger...")
            self.root.destroy() #closes application
        else:
            mb.showinfo("Återvänd", "Återvänder till program") #returning to program

    def get_budgetpost(self): #function to get the key and value from input
        self.get_budgetpost = self.svar_budgetpost.get() #gets key
        self.get_cost = self.svar_cost.get() #gets  value

        int(self.get_cost) #makes value to INT

        self.budget_posts[self.get_budgetpost] = self.get_cost #appends pair to dict

        print(self.budget_posts) #debugging

        self.svar_budgetpost.delete(0, END) #clears entry field
        self.svar_cost.delete(0, END) #clears entry field

    def val1(self): #choice 1 function
        self.btn_frame.forget() #forgets earlier frame
        self.val1_frame = Frame(self.root) #creates new frame

        self.val1_frame.columnconfigure(0, weight=1) #column configure...
        self.val1_frame.columnconfigure(1, weight=1) #column configure...

        message_budgetpost = Label(self.val1_frame, text="Skriv vilken budgetpost du skulle vilja lägga till:", font="Times, 12") #information message
        message_budgetpost.grid(column= 0, row=0, sticky="ew", padx=5,pady=5) 


        self.svar_budgetpost = Entry(self.val1_frame) #entry for budgetpost
        self.svar_budgetpost.grid(column=0, row=1, sticky="ew", padx=5, pady=5)

        message_cost = Label(self.val1_frame, text="Vad kostar denna budgetpost?", font="Times, 12") #information message
        message_cost.grid(column=0, row=2, sticky="ew", padx=5, pady=5)

        self.svar_cost = Entry(self.val1_frame) #entry for value for budgetpost
        self.svar_cost.grid(column=0, row=3, sticky="ew", padx=5, pady=5)



        btn = Button(self.val1_frame, text="Klar", font="Times, 12", command=self.get_budgetpost) #button for calling the get_budgetpost function
        btn.grid(column=0, row=5, sticky="ew", padx=5, pady=5)
        
        
        
        self.val1_frame.pack() #pack...


    def __init__(self): #main program 
        self.budget_posts = {} #dict with budget posts
        self.root = Tk() #window
        self.root.geometry("800x500") #set geometry of window

        self.btn_frame = Frame(self.root) #set main menu frame

        self.btn_frame.columnconfigure(0, weight= 1) #column configure
        self.btn_frame.columnconfigure(1, weight= 3) #column configure

        self.btn_1 = Button(self.btn_frame, text="Lägg till ny budgetpost", font="Times, 12", command=self.val1) #button for choice 1, add post
        self.btn_1.grid(column= 0, row= 0, sticky="ew", padx= 5, pady= 5) 

        self.btn_2 = Button(self.btn_frame, text= "Ändra budgetpost", font="Times, 12") #button for choice 2, change posts
        self.btn_2.grid(column= 0, row= 1, sticky="ew" , padx= 5, pady= 5)

        self.btn_3 = Button(self.btn_frame, text="Skriv ut budget", font="Times, 12") #button for choice 3, print budget
        self.btn_3.grid(column= 0, row= 2, padx=5, pady= 5, sticky="ew")

        self.btn_4 = Button(self.btn_frame, text="Avsluta program", font="Times, 12", command=self.exit_question) #button for choice 4, close program
        self.btn_4.grid(column= 0, row= 3, padx=5, pady=5, sticky="ew")

        self.btn_frame.pack()







        self.root.mainloop()

MyGUI()