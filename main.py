from tkinter import *
from tkinter import messagebox
import os

color = "#c9def8"
root = Tk()
root.title("Password Manager")
x = 680
y = 440
root.minsize(x, y) 
root.maxsize(x, y) 
root.configure(bg = color)

#main password saver interface
def app():
    def add():
        one = entry1.get()
        two = entry2.get()
        three = entry3.get()
        saved = open("saved.txt", "r").read()
        if one != "" and two != "":
            if one in saved and two in saved:
                messagebox.showinfo("Info", "Already Exists!")
            else:
                saved = open("saved.txt", "a")
                saved.write("Site Name: " + one + "\n" + 'Site Adress: ' + two + '\n' + "Password: " + three + "\n\n")
                messagebox.showinfo("Info", "Successful!")
                entry1.delete(0, END)
                entry2.delete(0, END)
        else:
            messagebox.showinfo("Info", "Fields cannot be left empty!")

    #saved passwords interface
    def saved():
        root.maxsize(x, y) 
        root.minsize(x, y)
        app_frame.destroy()
        saved_frame = Frame(root, bg = color)
        saved_frame.pack()
        saved = open("saved.txt", "r")
        global text
        text = Text(saved_frame, wrap = "word", height = 10, bg = "#0b2947", fg = "white",  relief = FLAT, font = ("arial black", 9))
        text.insert("1.0", saved.read())
        #text.config(state = DISABLED)
        text.pack(side = TOP)

        def back():
            saved_frame.destroy()
            app()
            
        def clear():
            answer = messagebox.askyesno("Confirmation", "Are you sure to delete all saved passwords?")
            if answer == True:
                with open("saved.txt", "w") as saved:
                    saved.write("")
                text.config(state = NORMAL)     
                text.delete(1.0, END)
                text.config(state = DISABLED)  
            else:
                pass
            

        
        back_but = Button(saved_frame, text = "Back", width = 6, height = 7, bd = 1, font = ("arial black", 9),  command = back)
        back_but.pack(side = "left", padx = 80, pady = 10)
        clear_but = Button(saved_frame, text = "Clear", width = 6, height = 7, bd = 1, font = ("arial black", 9), command = clear)
        clear_but.pack(side = "right", padx = 80, pady = 10)        

    root.maxsize(x, y) 
    root.minsize(x, y)
    #global app_frame
    app_frame = Frame(root, bg = color)
    app_frame.pack()
    #menubar = Menu(app_frame)
    title = Label(app_frame, text = "Password Manager", pady = 15, font = ("calibri", 14, 'bold'), bg = color)
    title.grid(row = 0, column = 0, columnspan = 2)
    label1 = Label(app_frame, text = ".   Site Name:", font = ("arial black", 9, 'bold'), bg = color)
    label1.grid(row = 1, column = 0)
    entry1 = Entry(app_frame, width = 25, relief = None)
    entry1.grid(row = 1, column = 1, pady=10)
    
    label2 = Label(app_frame, text = "Site Address:", font = ("arial black", 9, 'bold'), bg = color)
    label2.grid(row = 2, column = 0)
    entry2 = Entry(app_frame, width = 25, relief = None)
    entry2.grid(row = 2, column = 1)

    label3 = Label(app_frame, text = "       Password: ", pady = 10, font = ("arial black", 9, 'bold'), bg = color)
    label3.grid(row = 3, column = 0)
    entry3 = Entry(app_frame, width = 22, show = "*", font = ("arial black", 9, "bold"), relief = None)
    entry3.grid(row = 3, column = 1, pady = 10)

    button1 = Button(app_frame, text = "Add", width = 16, font = ("arial black", 9, 'bold'), command = add, bg = None, bd = 1, relief = None)
    button1.grid(row = 4, column = 1)
    button2 = Button(app_frame, text = "Saved Passwords", width = 16, font = ("arial black", 9, 'bold'), command = saved, bg = None, bd = 1, relief = None)
    button2.grid(row = 5, column = 1, pady = 5)

def password():
    def login():
        if pass_entry.get() == open("file.txt", "r").read():
            input_pass.destroy()
            app()
        else:
            print("ok")
            pass_entry.delete(0, END)
            messagebox.showerror("info", "Wrong Password!\n Try Again")

    input_pass = Frame(root, bg = color)
    input_pass.pack()
    space = Label(input_pass, text = "\n", bg = color)
    space.grid(row = 0, column = 0)
    label1 = Label(input_pass, text = "Enter Password:", font = ("arial black", 14), bg = color)
    label1.grid(row = 1, column = 0)
    pass_entry = Entry(input_pass, width = 25, bd = 1, bg = "#edf0f3", show = "*", font = ("arial black", 9, "bold"))
    pass_entry.grid(row = 2, column = 0, pady = 10)
    pass_button = Button(input_pass, text = "Login", width = 10, font = ("calibri", 10, "bold"), command = login, bg = None, relief = None, fg = "black", bd = 1)
    pass_button.grid(row = 3, column = 0)

def main():
    password()


main()
root.mainloop()
