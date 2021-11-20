from tkinter import *
from Admin import *


def Home(root, frame1, frame2):

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    Button(frame2, text="Home", font=('Times', 10),command = lambda: Home(root, frame1, frame2)).grid(row=0,column=0)
    Label(frame2, text="                                                                         ").grid(row = 0,column = 1)
    Label(frame2, text="                                                                         ").grid(row = 0,column = 2)
    Label(frame2, text="         ").grid(row = 1,column = 1)
    frame2.pack(side=TOP)

    root.title("Home")

    Label(frame1, text="BIOMETRIC VOTER REGISTRATION", font=('Times', 20, 'bold','italic')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    admin = Button(frame1, text="Admin Login", width=15, font=('Times', 10), command = lambda: AdminHome(root, frame1, frame2))


    voter = Button(frame1, text="Voter Login",font=('Times', 10), width=15)

   
    Label(frame1, text="").grid(row = 2,column = 0)
    Label(frame1, text="").grid(row = 4,column = 0)

    admin.grid(row = 3, column = 1, columnspan = 2)
    voter.grid(row = 5, column = 1, columnspan = 2)

    frame1.pack()
    root.mainloop()


def new_home():
    root = Tk()
    root.geometry('600x600')
    frame1 = Frame(root)
    frame2 = Frame(root)
    Home(root, frame1, frame2)


if __name__ == "__main__":
    new_home()
