from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import frontend.register
import backend.dbconnection
import frontend.dashboard

class Login_System:
    def __init__(self,root):
        self.root =root
        self.root.title("login System")
        self.root.geometry("650x600+100+50")
        self.root.configure(bg="white")

        self.db = backend.dbconnection.DBConnect()

        self.background_Pic = ImageTk.PhotoImage(file='ladylaptop.png')
        self.background_Pic_image = Label(self.root, image=self.background_Pic, bg="white")
        self.background_Pic_image.place(x=180, y=0, relwidth=1, relheight=1)

        #frame, labels, entery field & buttons
        main_frame = Frame(self.root,  relief=RIDGE, bd=10,bg="dodgerblue4")
        main_frame.place(x=10, y=50, width=360, height=500)

        Login = Label(main_frame, text="Sign In", font=("Arial", 16, "bold"),bg="dodgerblue4",fg="white")
        Login.grid(row=1, column=4, padx=20, pady=5)

        l_username = Label(main_frame, pady=20, padx=10,text="Username:", font=("Arial", 12, ), bg="dodgerblue4",fg="white")
        l_username.grid(row=2, column=3, stick=NW)
        self.username = Entry(main_frame, bd=3, relief=SUNKEN, width=20, font=20, bg="azure")
        self.username.grid(row=2, column=4)

        l_password = Label(main_frame,pady=20, padx=10, text="Password:", font=("Arial", 12, ), bg="dodgerblue4",fg="white")
        l_password.grid(row=3, column=3,stick=NW)
        self.password = Entry(main_frame, bd=3, relief=SUNKEN, width=20, font=20, show="*", bg="azure")
        self.password.grid(row=3, column=4)

        self.loginButton = Button(self.root, text="login", font=("Arial", 12, ) ,width=15, height=1,command=self.login_command )
        self.loginButton.place(x=130, y=300)
        self.reset_button = Button(self.root, text='Reset', font=("Arial", 12, ), width=15, height=1, command=self.reset_command)
        self.reset_button.place(x=130, y=350)

        self.label_signup = Label(self.root, text='No account?Sign up', font=("Arial", 12, ) , fg="turquoise", bg="dodgerblue4")
        self.label_signup.place(x=130, y=480)
        self.label_signup.bind('<Button-1>',self.lbl_signup_click )
        self.root.mainloop()


    def reset_command(self):
        """ function for clearing the entry field"""
        self.username.delete(0,END)
        self.username.insert(0, "")
        self.password.delete(0, END)
        self.password.insert(0, '')


    def login_command(self):
        """function for checking if the username and the password matched with database record """
        username=self.username.get()
        password=self.password.get()
        query="select * from librarian where Username=%s and Password=%s "
        values=(username,password)
        records=self.db.select(query,values)
        if not records:
            messagebox.showerror("Error!","Username doesn't exist")
        else:
            for row in records:
                if row[2]==self.password.get():
                    w=Toplevel()
                    frontend.dashboard.Dashboard(w)




    def lbl_signup_click(self, event):
        """function for register page """
        tk = Toplevel()
        frontend.register.Register_System(tk)

