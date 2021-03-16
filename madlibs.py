import random 
from tkinter import * 
from tkinter import messagebox 

window = Tk()

window.geometry("400x400")


Label1 = Label(window, text="Enter an adjective: ")
entry1 = Entry(window)

Label2 = Label(window, text="Enter a verb: ")
entry2 = Entry(window)

Label3 = Label(window, text="Enter an adjective: ")
entry3 = Entry(window)

Label4 = Label(window, text="Enter a noun: ")
entry4 = Entry(window)

Label5 = Label(window, text="Enter a color: ")
entry5 = Entry(window)

Label6 = Label(window, text="Enter a plural noun: ")
entry6= Entry(window)

Label7 = Label(window, text="Enter a verb: ")
entry7 = Entry(window)

Label8 = Label(window, text="Enter an adjective: ")
entry8 = Entry(window)

Label9 = Label(window, text="Enter a verb: ")
entry9 = Entry(window)

Label10 = Label(window, text="Enter a noun: ")
entry10 = Entry(window)

Label11 = Label(window, text="Enter an adjective: ")
entry11 = Entry(window)

Label1.grid(row = 0, column = 0, sticky = W, pady = 2) 
Label2.grid(row = 1, column = 0, sticky = W, pady = 2) 
Label3.grid(row = 2, column = 0, sticky = W, pady = 2) 
Label4.grid(row = 3, column = 0, sticky = W, pady = 2) 
Label5.grid(row = 4, column = 0, sticky = W, pady = 2) 
Label6.grid(row = 5, column = 0, sticky = W, pady = 2) 
Label7.grid(row = 6, column = 0, sticky = W, pady = 2) 
Label8.grid(row = 7, column = 0, sticky = W, pady = 2) 
Label9.grid(row = 8, column = 0, sticky = W, pady = 2) 
Label10.grid(row = 9, column = 0, sticky = W, pady = 2) 
Label11.grid(row = 10, column = 0, sticky = W, pady = 2) 

entry1.grid(row = 0, column = 1, sticky = W, pady = 2)
entry2.grid(row = 1, column = 1, sticky = W, pady = 2)
entry3.grid(row = 2, column = 1, sticky = W, pady = 2)
entry4.grid(row = 3, column = 1, sticky = W, pady = 2)
entry5.grid(row = 4, column = 1, sticky = W, pady = 2)
entry6.grid(row = 5, column = 1, sticky = W, pady = 2)
entry7.grid(row = 6, column = 1, sticky = W, pady = 2)
entry8.grid(row = 7, column = 1, sticky = W, pady = 2)
entry9.grid(row = 8, column = 1, sticky = W, pady = 2)
entry10.grid(row =9, column = 1, sticky = W, pady = 2)
entry11.grid(row =10, column = 1, sticky = W, pady = 2)

def print_text():
    messagebox.showinfo("Result", "Tonight is the night when all of the "+entry1.get()+" monsters come out to "+entry2.get()+". "+entry3.get()+" witches with big "+entry4.get()+" and "+entry5.get()+" shoes make potions and very spooky brews. Vampires with "+entry6.get()+" and long red capes visit with friends and search for neck napes. Ogres and ghosts sometimes "+entry7.get()+" and play, on this "+entry8.get()+" October day. All the Trick-or-Treaters "+entry9.get()+" and hunt for "+entry10.get()+" and a scare, dressed up as princesses and cowboys here and there. Have a "+entry11.get()+" Halloween in 2021!")

button = Button(window,text="Enter",command=print_text)

button.grid(row =11, column = 1, sticky = W, pady = 2)

window.mainloop()