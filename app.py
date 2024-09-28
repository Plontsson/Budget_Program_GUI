from tkinter import *

root = Tk()


root.title("Duntis Budgetprogram!")
root.geometry("800x400")
welcome_message = Label(root, text="Välkommen till Duntis´s budgetprogram!", font= ("Times 20 bold"), )
welcome_message.pack()

#Button 1, add budgetpost
B_1 = Button(root, text="Lägg till budgetpost")
B_1.pack(fill=BOTH, expand=TRUE)

#Button 2 change budgetpost

B_2 = Button(root, text="Ändra Kategori")
B_2.pack(fill=BOTH, expand=TRUE)

#Button 3 write budget

B_3= Button(root, text="Skriv ut budget")
B_3.pack(fill=BOTH, expand=TRUE)

#Button 4 Exit program

B_4 = Button(root, text="Avsluta program", command=exit)
B_4.pack(fill=BOTH, expand=TRUE)


root.mainloop()