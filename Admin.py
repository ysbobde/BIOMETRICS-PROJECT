from tkinter import *
import homePage as hpg
from homePage import *


def AdminHome(root,frame1,frame3):
    root.title("Admin")
    for widget in frame1.winfo_children():
        widget.destroy()
    
    Label(frame1, text="ADMIN CONSOLE", font=('Times', 20, 'bold','italic')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    
    runServer = Button(frame1, text="Run Server", width=15)

    registerVoter = Button(frame1, text="Register Voter", width=15)

    showVotes = Button(frame1, text="Total vote count", width=15)

    
    Label(frame1, text="").grid(row = 2,column = 0)
    Label(frame1, text="").grid(row = 4,column = 0)
    Label(frame1, text="").grid(row = 6,column = 0)
    runServer.grid(row = 3, column = 1, columnspan = 2)
    registerVoter.grid(row = 5, column = 1, columnspan = 2)
    showVotes.grid(row = 7, column = 1, columnspan = 2)

    frame1.pack()
    root.mainloop()




if __name__ == "__main__":
    root = Tk()
    root.geometry('500x500')
    frame1 = Frame(root)
    frame3 = Frame(root)
    AdminHome(root,frame1,frame3)
