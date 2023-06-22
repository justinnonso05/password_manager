from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter.scrolledtext
import os
import sys


color = "#c9def8"
root = Tk()
root.title("SecureKey - Password Manager")
root.minsize(500, 300) 
root.maxsize(500, 300) 
root.configure(bg = color)

script_dir = getattr(sys,'_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
icon_path = os.path.join(script_dir, 'padlock.ico')
with open("saved.txt", "w") as f:
    f.write("")

with open("password.txt", "w") as f:
    f.write("000000")

file_path = os.path.join(script_dir, 'password.txt')
saved_path = os.path.join(script_dir, 'saved.txt')

root.iconbitmap(icon_path)


def export():
    confirm = messagebox.askyesno("Export", "Your passwords will be exported to a text file")
    if confirm == True:
        saved = open(saved_path, "r").read()
        files = filedialog.asksaveasfilename(defaultextension = ".txt", filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")])
        if files:
            with open(files, "w") as f:
                f.write(saved)

#menubar
def app_help():
    messagebox.showinfo("Help", "The default password is 000000. You can change it any time. \n\nDeleting this applicatiion will cause a loss of all saved passwords. You can back them up before deleting by exporting them.")
def app_about():
    messagebox.showinfo("About", "Simple Password Manager application.\n\nMade by Justin Chinonso")

menu_bar = Menu(root, background = "black", fg = "white") 
# menu_bar.configure(bg = color)
options_menu = Menu(menu_bar, tearoff = 0)
options_menu.add_command(label = "Export Password", command = export, state = "disabled")
options_menu.add_command(label = "Exit", command = root.quit)
menu_bar.add_cascade(label = "Options", menu = options_menu)

about_menu = Menu(menu_bar, tearoff = 0)
about_menu.add_command(label = "About", command = app_about)
menu_bar.add_cascade(label = "About", menu = about_menu)

help_menu = Menu(menu_bar, tearoff = 0)
help_menu.add_command(label = "Help", command = app_help)
menu_bar.add_cascade(label = "Help", menu = help_menu)


#main password saver interface
def app():
    def add():
        one = entry1.get()
        two = entry2.get()
        three = entry3.get()
        four = entry4.get()
        saved = open(saved_path, "r").read()
        if one != "" and two != "" and three != "" and four != "":
            if three in saved and four in saved:
                messagebox.showinfo("Info", "Already Exists!")
            else:
                saved = open(saved_path, "a")
                #saved.write("Site Name: " + one + "\n" + "Site Address: " + two + "\n" + "Username: " + three + "\n" + "Password: " four + "\n\n")
                saved.write("Site Name: " + one + "\n" + 'Site Adress: ' + two + '\n' + "Username: " + three + '\n' + "Password: " + four + "\n\n")
                messagebox.showinfo("Info", "Successful!")
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
        else:
            messagebox.showinfo("Info", "Fields cannot be left empty!")

    #saved passwords interface
    def saved():
        root.maxsize(500, 300) 
        root.minsize(500, 300)
        app_frame.destroy()
        saved_frame = Frame(root, bg = color)
        saved_frame.pack()
        saved = open(saved_path, "r")
        global text
        text = tkinter.scrolledtext.ScrolledText(saved_frame, wrap = "word", height = 12, bg = "#0b2947", fg = "white",  relief = FLAT, font = ("arial black", 9))
        text.insert("1.0", saved.read())
        #scrollbar = Scrollbar(saved_frame, orient= "vertical", command = text.yview)
        text.config(state = DISABLED)
        #scrollbar.pack(side = "right", fill = "y", expand = False)
        text.pack(side = TOP, expand = True)

        def back():
            saved_frame.destroy()
            app()
            
        def clear():
            answer = messagebox.askyesno("Confirmation", "Are you sure to delete all saved passwords?")
            if answer == True:
                with open(saved_path, "w") as saved:
                    saved.write("")
                text.config(state = NORMAL)     
                text.delete(1.0, END)
                text.config(state = DISABLED)  
            else:
                pass
            

        
        back_but = Button(saved_frame, text = "Back", width = 6, height = 2, bd = 1, font = ("arial black", 9),  command = back)
        back_but.pack(side = "left", padx = 80, pady = 15)
        clear_but = Button(saved_frame, text = "Clear", width = 6, height = 2, bd = 1, font = ("arial black", 9), command = clear)
        clear_but.pack(side = "right", padx = 80, pady = 15)        

    root.maxsize(500, 300) 
    root.minsize(500, 300)
    app_frame = Frame(root, bg = color)
    app_frame.pack()
    #menubar = Menu(app_frame)
    title = Label(app_frame, text = "Password Manager", pady = 15, font = ("arial black", 14), bg = color)
    title.grid(row = 0, column = 0, columnspan = 2)

    name = Label(app_frame, text = "   Site Name: ", font = ("arial black", 9, 'bold'), bg = color)
    name.grid(row = 1, column = 0)
    entry1 = Entry(app_frame, width = 25, relief = None, font = ("arial black", "9", 'bold'))
    entry1.grid(row = 1, column = 1, pady = (0, 10))

    address = Label(app_frame, text = "Site Address: ", font = ("arial black", 9, 'bold'), bg = color)
    address.grid(row = 2, column = 0)
    entry2 = Entry(app_frame, width = 25, relief = None, font = ("arial black", "9", 'bold'))
    entry2.grid(row = 2, column = 1, pady = (0, 10))

    username = Label(app_frame, text = "   Username: ", font = ("arial black", 9, 'bold'), bg = color)
    username.grid(row = 3, column = 0)
    entry3 = Entry(app_frame, width = 25, relief = None, font = ("arial black", "9", 'bold'))
    entry3.grid(row = 3, column = 1, pady = (0, 10))

    password = Label(app_frame, text = "    Password: ", font = ("arial black", 9, 'bold'), bg = color)
    password.grid(row = 4, column = 0)
    entry4 = Entry(app_frame, width = 25, relief = None, show = ".", font = ("arial black", "9", 'bold'))
    entry4.grid(row = 4, column = 1, pady = (0, 10))

    button1 = Button(app_frame, text = "ADD", width = 16, font = ("arial black", 9), command = add, bg = None, bd = 1, relief = None)
    button1.grid(row = 5, column = 1)
    button2 = Button(app_frame, text = "Saved Passwords", width = 16, font = ("arial black", 9), command = saved, bg = None, bd = 1, relief = None)
    button2.grid(row = 6, column = 1, pady = 5)

def password():
    def login():
        if pass_entry.get() == open(file_path, "r").read():
            input_pass.destroy()
            app()
            options_menu.entryconfig("Export Password", state = "normal")
        else:
            print("ok")
            pass_entry.delete(0, END)
            messagebox.showerror("info", "Wrong Password!\n Try Again")

    def set_pass():
        input_pass.pack_forget()
        set_pass_frame = Frame(root, bg = color)
        set_pass_frame.pack()
        def confirm_pass():
            if old.get() != "" and new.get() != "" and confirm.get() != "":
                if old.get() == open(file_path, "r").read():
                    if new.get() == confirm.get():
                        old_pass = open(file_path, "w")
                        old_pass.write(confirm.get())
                        messagebox.showinfo("Info", "Successful")
                        old.delete(0, END)
                        new.delete(0, END)
                        confirm.delete(0, END)
                    else:
                        messagebox.showerror("Error", "Passwords don't match")
                else:
                    messagebox.showerror("Error", "Old password not correct")
            else:
                messagebox.showerror("Error", "Fields cannot be left empty")
            

        space = Label(set_pass_frame, text = "\n", bg = color)
        space.grid(row = 0, column = 0)
        label1 = Label(set_pass_frame, text = "Enter old password:", font = ("arial black", 9), bg = color)
        label1.grid(row = 1, column = 0)
        old = Entry(set_pass_frame, width = 25, bd = 1, bg = "#edf0f3", show = ".", font = ("arial black", 9, "bold"))
        old.grid(row = 2, column = 0, pady = 5)
        label2 = Label(set_pass_frame, text = "Enter new password:", font = ("arial black", 9), bg = color)
        label2.grid(row = 3, column = 0)
        new = Entry(set_pass_frame, width = 25, bd = 1, bg = "#edf0f3", show = ".", font = ("arial black", 9, "bold"))
        new.grid(row = 4, column = 0, pady = 5)
        label3 = Label(set_pass_frame, text = "confirm new password:", font = ("arial black", 9), bg = color)
        label3.grid(row = 5, column = 0)
        confirm = Entry(set_pass_frame, width = 25, bd = 1, bg = "#edf0f3", show = ".", font = ("arial black", 9, "bold"))
        confirm.grid(row = 6, column = 0, pady = 5)

        def back():
            set_pass_frame.pack_forget()
            password()
            #input_pass.pack()

        set_button = Button(set_pass_frame, text = "Set Password", width = 10, padx = 10, pady = 5, font = ("calibri", 10, "bold"), command = confirm_pass, bg = None, relief = None, fg = "black", bd = 1)
        set_button.grid(row = 7, column = 0, pady = (20, 0))
        back_button = Button(set_pass_frame, text = "Back", width = 10, padx = 10, pady = 5, font = ("calibri", 10, "bold"), command = back, bg = None, relief = None, fg = "black", bd = 1)
        back_button.grid(row = 8, column = 0, pady = (10, 0))




    global input_pass
    input_pass = Frame(root, bg = color)
    input_pass.pack()
    space = Label(input_pass, text = "\n", bg = color)
    space.grid(row = 0, column = 0)
    label1 = Label(input_pass, text = "Enter Password:", font = ("arial black", 14), bg = color)
    label1.grid(row = 1, column = 0)
    pass_entry = Entry(input_pass, width = 25, bd = 1, bg = "#edf0f3", show = ".", font = ("arial black", 9, "bold"))
    pass_entry.grid(row = 2, column = 0, pady = 10)
    pass_button = Button(input_pass, text = "Login", width = 10, font = ("calibri", 10, "bold"), command = login, bg = None, relief = None, fg = "black", bd = 1)
    pass_button.grid(row = 3, column = 0)
    set_button = Button(input_pass, text = "Set Password", width = 10, padx = 10, pady = 5, font = ("calibri", 10, "bold"), command = set_pass, bg = None, relief = None, fg = "black", bd = 1)
    set_button.grid(row = 4, column = 0, pady = (50, 0))


password()
root.config(menu = menu_bar)
root.mainloop()
