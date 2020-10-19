from tkinter import *

main_screen = Tk()  

def main_account_screen():
    
    main_screen = Tk()   
    main_screen.geometry("300x250") 
    main_screen.title("DMC Login") 

Label(text="Choose Login Or Register", bg="red", width="300", height="4", font=("Times New Roman", 13)).pack() 
Label(text="").pack() 

Button(text="Login", height="3", width="15").pack() 
Label(text="").pack() 

Button(text="Register", height="3", width="15").pack()
 
main_screen.mainloop() 

main_account_screen() 

def registration():
    register = Toplevel(main_screen)
    register.title("Register new user")
    register.geometry("500x500")
    user = StringVar()
    password = StringVar()
    Label(register,text = "Enter the users details below:", bg="red").pack()
    Label(register, text="").pack()
    username = Label(register, text="Username *")
    username.pack()
