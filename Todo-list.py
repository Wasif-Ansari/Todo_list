from tkinter import *


root = Tk()
root.title("MY TODO LIST")
root.geometry("400x650+400+100")
root.resizable(False,False)

heading = Label(root,text="TO-DO-LIST",justify=CENTER,font="50px")
heading.place(x=125,y=20,height=100,width=150)

frame = Frame(root,width=400,height=50, bg="white")
frame.place(x=0 , y=120)

task = StringVar()
task_entry = Entry(frame,width=22,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()



root.mainloop()