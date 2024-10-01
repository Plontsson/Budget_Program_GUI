from tkinter import *
from tkinter import messagebox as mb
import os


class Calculations: #Class only for calculating or functions retrieving
    def __init__(self,gui):
        self.gui = gui #reference gui
        self.budget_posts = {}

    def load_budget_file(self): #loads old txt file if it exists
        if os.path.exists("budget.txt"):
            with open("budget.txt", "r") as file:
                for line in file:
                    if "Summan av dina kostnäder är: " in line or "Du har såhär mycket pengar över: " in line:
                        continue
                    key, value = line.split(": ")
                    self.budget_posts[key] = float((value.replace("kr", "")).strip())

    def change_value(self): #function that appends the new value to the budget post dict

        self.new_value = self.gui.new_value.get()

        if len(self.new_value) == 0:
            mb.showinfo("Fel!", "Du måste skriva något i fältet")

        else:
            
            try:
                self.new_value = float(self.new_value)
                self.budget_posts[self.change_post] = self.new_value
                mb.showinfo("Klart", "Din budgetpost är ändrad!")
                self.gui.main_menu()

            except ValueError:
                mb.showinfo("Fel!", "Du måste skriva med nummer!")

        

    def change_budget_post(self): #function that gets the budget post
        self.change_post = self.gui.answer_val_2.get()
        self.change_post = self.change_post.lower()

        if len(self.change_post) == 0:
            mb.showinfo("Fel!", "Du måste skriva något i fältet!")

        elif self.change_post in self.budget_posts:
            self.gui.val_2_second()

        else:
            mb.showinfo("Fel!", "Den budgetposten finns inte!")
    

    def sum_costs(self): #function to sum the costs
        self.costs = sum(self.budget_posts.values())
        return self.costs
    
    def excess_salary(self): #function calculate excess salary
        self.salary = float(self.salary)
        self.excess = self.salary - self.costs
        return self.excess

    def print_budget(self): #function to print the budget to a txt file
        svar = mb.askyesno("Skriv ut", "Vill du verkligen skriva ut din budget?") #question user if he/she really wants to create budget txt file
        if svar == True:
            file = open("budget.txt", "w")
            for key, value in self.budget_posts.items():
                file.write(f"{key}: {value} kr \n")

            file.write(f"Summan av dina kostnader är: {self.sum_costs()}\n")
            file.write(f"Du har såhär mycket pengar över: {self.excess_salary()}")
        else:
            mb.showinfo("Återvänder", "Återvänder till program")

    def get_salary(self): #function to get salary
        self.salary = self.gui.answer_salary.get() #retrieves value
        if len(self.salary) == 0: #checks if user written anything
            mb.showinfo("Fel", "Du måste skriva ett tal")  
            
        else:
            try:
                self.salary = float(self.salary) #checks if input can be turned to float
                print(self.salary) #debugging
                mb.showinfo("Klar!", "Din lön är sparad!")
                self.gui.main_menu()

            except ValueError:
                mb.showinfo("Fel", "Du måste skriva med nummer!")

    def get_answer(self): #function to get the key and value from input
        self.get_budgetpost = self.gui.svar_budgetpost.get() #gets key
        self.get_cost = self.gui.svar_cost.get() #gets  value
        self.get_budgetpost = self.get_budgetpost.lower() #lowercase key  
        
        if len(self.get_budgetpost) == 0 or len(self.get_cost) == 0: #checks if the entry fields are empty
            mb.showinfo("Fel", "Du måste skriva i båda fälten!")

        elif self.get_budgetpost in self.budget_posts: #Checks if key already exists
            mb.showinfo("Fel", "Den budgetposten finns redan!")

        else:
            try: #try to turn the value to int, if valueerror print error message
                float(self.get_cost) #checks if entry can be turned to float

                self.budget_posts[self.get_budgetpost] = float(self.get_cost) #appends pair to dict

                print(self.budget_posts.values()) #debugging
                mb.showinfo("Klart", "Budgetposten är sparad!")
                self.gui.svar_budgetpost.delete(0, END) #clears entry field
                self.gui.svar_cost.delete(0, END) #clears entry field
                
            except ValueError:
                mb.showinfo("Fel!", "Du måste skriva en siffra i andra fältet!")

    def exit_question(self): #function to ask if user wants to close program
        svar = mb.askyesno("Stäng programmet", "Vill du verkligen stänga programmet?") #using tkinter yesno 
        if svar == True:
            self.gui.root.destroy() #closes application
        else:
            mb.showinfo("Återvänd", "Återvänder till program") #returning to program

class MyGUI: #Class for the frames and main program


    def __init__(self): #main program 
        self.calc = Calculations(self) #create instance and pass itself
        self.val1_frame = None #to make the attributes exist from start
        
        self.val_2_frame = None

        self.val_2_second_frame = None

        self.btn_frame = None #-.-

        self.salary_frame = None #-.-

        self.calc.load_budget_file()

        self.root = Tk() #window
        self.root.geometry("800x500") #set geometry of window
        self.root.title("Budget Program")
        self.salary_login() #calls the login frame menu

        self.root.protocol("WM_DELETE_WINDOW", self.calc.exit_question) #Closing procedure for X on window aswell

        self.root.mainloop()



    def salary_login(self): #salary menu, shows on startup
        self.salary_frame = Frame(self.root) #sets frame
        self.salary_frame.columnconfigure(0, weight=1) #columnconfigure

        message_salary = Label(self.salary_frame, text="Skriv din lön nedan:", font="Times, 12") #welcome message
        message_salary.grid(column=0, row=0, sticky="ew", padx=5, pady=5)

        self.answer_salary = Entry(self.salary_frame) #entry for user input salary
        self.answer_salary.grid(column=0, row=1, sticky="ew", padx=5, pady=5)

        btn_salary = Button(self.salary_frame, text="Klar", font="Times, 12", command=self.calc.get_salary) #button to enter main menu and pass salary
        btn_salary.grid(column=0, row = 2, sticky="ew", padx=5, pady=5)

        self.salary_frame.pack()


    def main_menu(self): #main menu frame
        if self.salary_frame is not None: #create instance and checks if it already is activated
            self.salary_frame.forget()
        if self.val1_frame is not None: #create instance and checks if it already is activated
            self.val1_frame.forget()
        if self.val_2_frame is not None:
            self.val_2_frame.forget()
        if self.val_2_second_frame is not None:
            self.val_2_second_frame.forget()
            
        self.btn_frame = Frame(self.root) #set main menu frame

        self.btn_frame.columnconfigure(0, weight= 1) #column configure
        self.btn_frame.columnconfigure(1, weight= 3) #column configure

        welcome_message = Label(self.btn_frame, text="Välkommen till budgetprogrammet!", font=("Times, 12"))
        welcome_message.grid(column=0, row=0, sticky="ew", padx=5, pady=5)

        btn_1 = Button(self.btn_frame, text="Lägg till ny budgetpost", font="Times, 12", command=self.val1) #button for choice 1, add post
        btn_1.grid(column= 0, row= 1, sticky="ew", padx= 5, pady= 5) 

        btn_2 = Button(self.btn_frame, text= "Ändra budgetpost", font="Times, 12", command=self.val_2_main) #button for choice 2, change posts
        btn_2.grid(column= 0, row= 2, sticky="ew" , padx= 5, pady= 5)

        btn_3 = Button(self.btn_frame, text="Skriv ut budget", font="Times, 12", command=self.calc.print_budget) #button for choice 3, print budget
        btn_3.grid(column= 0, row= 3, padx=5, pady= 5, sticky="ew")

        btn_4 = Button(self.btn_frame, text="Avsluta program", font="Times, 12", command=self.calc.exit_question) #button for choice 4, close program
        btn_4.grid(column= 0, row= 4, padx=5, pady=5, sticky="ew")

        self.btn_frame.pack()
        self.btn_frame.update_idletasks()

    def val1(self): #choice 1 frame

        if self.btn_frame is not None:
            self.btn_frame.forget() #forgets earlier frame
        self.val1_frame = Frame(self.root) #creates new frame

        self.val1_frame.columnconfigure(0, weight=1) #column configure...
        self.val1_frame.columnconfigure(1, weight=1) #column configure...

        message_budgetpost = Label(self.val1_frame, text="Skriv vilken budgetpost du skulle vilja lägga till:", font="Times, 12") #information message
        message_budgetpost.grid(column= 0, row=0, sticky="ew", padx=5,pady=5) 


        self.svar_budgetpost = Entry(self.val1_frame, bg="white") #entry for budgetpost
        self.svar_budgetpost.grid(column=0, row=1, sticky="ew", padx=5, pady=5)

        message_cost = Label(self.val1_frame, text="Vad kostar denna budgetpost?", font="Times, 12") #information message
        message_cost.grid(column=0, row=2, sticky="ew", padx=5, pady=5)

        self.svar_cost = Entry(self.val1_frame, bg="white") #entry for value for budgetpost
        self.svar_cost.grid(column=0, row=3, sticky="ew", padx=5, pady=5)

        btn = Button(self.val1_frame, text="Klar", font="Times, 12", command=self.calc.get_answer) #button for calling the get_budgetpost function
        btn.grid(column=0, row=5, sticky="ew", padx=5, pady=5)
        btn_2 = Button(self.val1_frame, text="Tillbaka till menyn", font="Times, 12", command=self.main_menu)
        btn_2.grid(column=1, row=5, sticky="ew", padx=5,pady=5)
        
        self.val1_frame.pack() #pack...
        self.val1_frame.update_idletasks() #force update the frame, problem on macos

    def val_2_main(self): #choice 2 frame for changing the value of existing budget post
        if self.btn_frame is not None:
            self.btn_frame.forget()
        self.val_2_frame = Frame(self.root)

        self.val_2_frame.columnconfigure(0, weight = 1)
        self.val_2_frame.columnconfigure(1, weight=1)            

        welcome = Label(self.val_2_frame, text="Vilken budgetpost skulle du vilja ändra?", font="Times, 12")
        welcome.grid(column=0, row=0, sticky="ew",padx=5, pady=5)
        
        self.answer_val_2 = Entry(self.val_2_frame, font="Times, 12")
        self.answer_val_2.grid(column=0, row=1, sticky="ew", padx=5, pady=5)

        btn = Button(self.val_2_frame, text="Klar", font="Times, 12", command=self.calc.change_budget_post)
        btn.grid(column=0, row=2, sticky="we", padx=5,pady=5)

        btn_2 = Button(self.val_2_frame, text="Tillbaka till huvudmenyn", font="Times, 12", command=self.main_menu)
        btn_2.grid(column=1, row=2, sticky="ew", padx=5, pady=5)

        self.val_2_frame.pack()
        self.val_2_frame.update_idletasks()

    def val_2_second(self): #second frame where you enter the changed value
        self.val_2_frame.forget()

        self.val_2_second_frame = Frame(self.root)

        self.val_2_second_frame.columnconfigure(0, weight=1)
        self.val_2_second_frame.columnconfigure(1, weight=1)

        message = Label(self.val_2_second_frame, text="Hur mycet kostar budegtposten?", font="Times, 12")
        message.grid(column=0, row=0, sticky="ew", padx=5, pady=5)

        self.new_value = Entry(self.val_2_second_frame, font="Times, 12")
        self.new_value.grid(column=0, row=1, sticky="we", padx=5, pady=5)

        btn = Button(self.val_2_second_frame, text="Klar", font="Times, 12", command=self.calc.change_value)
        btn.grid(column=0, row=2, sticky="we", padx=5, pady=5)
        
        self.val_2_second_frame.pack()
        self.val_2_second_frame.update_idletasks()
MyGUI()
