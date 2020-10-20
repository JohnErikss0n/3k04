from tkinter import *
import os
def register():
    count = len(open("users.txt").readlines())
    if count>=10:
        Label(screennew, text = "Too many users",fg="red").pack()
    else:
        nameinfo=username.get()
        passinfo=password.get()
        f =open("users.txt","a")
        f.write(nameinfo+" "+passinfo+'\n')
        f.close()
        usernameentered.delete(0, END)
        passwordentered.delete(0, END)
        Label(screennew, text = "Successfully registered.", fg="green").pack()


def newuser():
    global username
    global password
    global screennew
    global passwordentered
    global usernameentered
    
    screennew = Toplevel(screen)
    screennew.title("Registration Info")
    screennew.geometry("500x250")
    username = StringVar()
    password = StringVar()
    Label(screennew,text = "UserID").pack()
    usernameentered = Entry(screennew,textvariable = username)
    usernameentered.pack()
    Label(screennew,text = "Password").pack()
    passwordentered = Entry(screennew,textvariable = password)
    passwordentered.pack()
    Button(screennew,text = "Complete registration", command=register).pack()

def completelogin():
    nameinfo=username.get()
    passinfo=password.get()
    f =open("users.txt","r")
    x = f.readlines()
    for i in x:
        x=i.split()
        print(x[0])
        print(nameinfo)
        if str(x[0]) == str(nameinfo) and  str(x[1]) == str(passinfo):
                Label(loginscreen,text="Success!", fg="green").pack()
                return
    Label(loginscreen,text="Login unsuccessful.", fg="red").pack()

    f.close()
    usernameentered.delete(0, END)
    passwordentered.delete(0, END)
    



def login():
    global username
    global password
    global loginscreen
    global passwordentered
    global usernameentered
    loginscreen = Toplevel(screen)
    loginscreen.title("Login")
    loginscreen.geometry("500x250")
    username = StringVar()
    password = StringVar()
    Label(loginscreen,text = "UserID").pack()
    usernameentered = Entry(loginscreen,textvariable = username)
    usernameentered.pack()
    Label(loginscreen,text = "Password").pack()
    passwordentered = Entry(loginscreen,textvariable = password)
    passwordentered.pack()
    Button(loginscreen,text = "Login", command=completelogin).pack()



def main_screen():
    global screen
    screen = Tk()
    screen.geometry("500x250")
    screen.title("DCM Main")
    Label(text = "Welcome to DCM", font = ("Times",13), bg="red").pack()
    Label(text = "        ",bg  ="red").pack()
    Label(text = "        ",bg  ="red").pack()
    Button(text = "Register new user", command = newuser).pack()
    Label(text = "        ",bg  ="red").pack()
    Button(text="Login existing user", command = login).pack()
    screen.configure(background='red')
    screen.mainloop()

main_screen()
    
