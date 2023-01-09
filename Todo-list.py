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

b =Button(frame,text="ADD",font="arial 20 bold", width=6,bg="#5a95ff",fg="#fff",bd=0)
b.place(x=300 ,y=0)


frame1 = Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(200,20))

listbox = Listbox(frame1,font=("arial",18) , width=40,height=16,bg="#32405b",fg="white", cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT , fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.mainloop()