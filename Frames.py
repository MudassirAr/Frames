from tkinter import*
root = Tk()
root.geometry("655x333")

f1 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root,borderwidth=10, bg="light grey", relief=RIDGE)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Project Tkinter - NOTEPAD")
l.pack(pady=142)


l = Label(f2, text="Welcome to-NOTEPAD", font="Helvetica 15 italic",  fg="red",pady=20 )





l.pack( )


















root.mainloop()
