from tkinter import*
from tkinter import messagebox
root=Tk()
root.title('SUDOKU')
root.geometry("1000x1000")

bg=PhotoImage(file="suds.png")
# Show image using label
label1=Label(root,image=bg)
label1.place(x=0,y=0)
frame=LabelFrame(root,text="",padx=50,pady=50,bg="black")
frame.place(x=600,y=30)
def Howtoplay():
    messagebox.showinfo("sudoku Rules:","Only use the numbers 1 to 9 \nAvoid trying to guess the solution to the puzzle \nOnly use each number once in each row, column, & grid")
b1=Button(frame,text="Start",padx=20,pady=5)
b1.config( height =1, width =10,bg="black",fg="gold",font=("Bold",20))
b2=Button(frame,text="How to play",command=Howtoplay,padx=20,pady=5)
b2.config( height =1, width =10,bg="black",fg="gold",font=("Bold",20))
b3=Button(frame,text="Quit",command=root.destroy,padx=20,pady=5)
b3.config( height =1, width =10,bg="black",fg="gold",font=("Bold",20))
b1.pack()
b2.pack()
b3.pack()
root.mainloop()
