from tkinter import*
from tkinter import messagebox
import grids
    
def buttons():
     
     global root1
     global root2
     root1.destroy()

     root2=Tk()
        
     '''starting with buttons'''
     #start_easy
     butE=Button(root2,text="EASY",width=10,bg="light blue",fg="black",command=lambda : display("EASY")).grid(row=0,column=5,padx=50,pady=10)
     #start_medium
     butM=Button(root2,text="MEDIUM",width=10,bg="orange",fg="black",command=lambda : display("MEDIUM")).grid(row=1,column=5,padx=50,pady=10)
     #start_hard
     butH=Button(root2,text="HARD",width=10,bg="coral",fg="black",command=lambda : display("HARD")).grid(row=2,column=5,padx=50,pady=10)
     #go_back_to_main_menu
     butMENU=Button(root2,text="GO BACK",width=10,bg="lavender",fg="black",command=root2.destroy).grid(row=4,column=5,padx=50,pady=50)
     root2.mainloop()


def display(level):
    
    global Qg, Ag    
    global root2
    global root3
    global RE, CE, N
    root2.destroy()

    if level=="EASY" :
        L=grids.easy_puzzle()
    elif level=="MEDIUM":
        L=grids.medium_puzzle()
    elif level=="HARD":
        L=grids.hard_puzzle()

    Qg=L[0]
    Ag=L[1]


    root3=Tk()
    for x in range(0,9):
        for y in range(0,9):
            labS=Label(root3,text=Qg[x][y],width=6,height=3,bg='gold',fg="black",borderwidth = 2,relief='groove')
            labS.grid(row=x+1,column=y+1)
            
    #choosing
    frame1=LabelFrame(root3,text="COORDINATES:",padx=50,pady=50)
    frame1.grid(row=10,column=0,columnspan=9,padx=5,pady=5)
    
    labR=Label(frame1,text="ROW:",width=5)
    labR.grid(row=11,column=0,)
    RE=Entry(frame1,width=5)#rowentry
    RE.grid(row=11, column = 2)

    labC=Label(frame1,text="COLUMN:",width=20)
    labC.grid(row=12,column=0)
    CE=Entry(frame1,width=5)#COLUMNentry
    CE.grid(row= 12, column = 2)
    
    labN=Label(frame1,text="Enter The Number:",width=20)
    labN.grid(row=13,column=0)        
    N=Entry(frame1,width=5)
    N.grid(row=13,column=2)
    
    #check_button
    butGO=Button(root3,text="GO!",width=5,bg="black",fg="gold",command=GO)
    butGO.grid(row=15,column=5)


def GO():
    
               global Qg, Ag    
               global root2
               global root3
               re=int(RE.get())
               ce=int(CE.get())
               n=int(N.get())

               flag=False

               for i in range (0,9):
                   for j in range (0,9):
                       if Qg[i][j]!=Ag[i][j]:
                           flag=False
                           break
                       elif Qg[i][j]==Ag[i][j]:
                           flag=True
                           
               if (n==Ag[re-1][ce-1]):
                   Qg[re-1][ce-1]=n
                   labUPDATE=Label(root3,text=n,width=6,height=3,bg="light green",fg="black",borderwidth=2,relief='groove')
                   labUPDATE.grid(row=re,column=ce)
                   RE.delete(0,END)
                   CE.delete(0,END)
                   N.delete(0,END)

               elif (n!=Ag[re][ce]):
                   messagebox.showerror("Oops!","Try again with a different number!")
                   N.delete(0,END)

               elif flag==True:
                   messagebox.showinfo("YAY!","YOU HAVE SUCCESSFULLY COMPLETED THE PUZZLE")
                   root3.destroy()

               
 
            
'''____INTRO____'''
from tkinter import*
from tkinter import messagebox
root1=Tk()
root1.title('SUDOKU')
root1.geometry("710x530")

bg=PhotoImage(file="suds.png")
# Show image using label
label1=Label(root1,image=bg)
label1.place(x=0,y=0)
frame=LabelFrame(root1,text="",padx=30,pady=30,bg="black")
frame.place(x=400,y=10)
def Howtoplay():
    messagebox.showinfo("sudoku Rules:","Only use the numbers 1 to 9 \nAvoid trying to guess the solution to the puzzle \nOnly use each number once in each row, column, & grid")
b1=Button(frame,text="Start",padx=20,pady=5,command=buttons)
b1.config( height =1, width =10,bg="black",fg="gold",font=("Bold",20))
b2=Button(frame,text="How to play",command=Howtoplay,padx=20,pady=5)
b2.config( height =1, width =10,bg="black",fg="gold",font=("Bold",20))
b3=Button(frame,text="Quit",command=root1.destroy,padx=20,pady=5)
b3.config( height =1, width =10,bg="black",fg="gold",font=("Bold",20))
b1.pack()
b2.pack()
b3.pack()
root1.mainloop()



#grid_sample
#easy_puzzle
'''Qg=[
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
    ]

Ag=[
    [4,3,5,2,6,9,7,8,1],
    [6,8,2,5,7,1,4,9,3],
    [1,9,7,8,3,4,5,6,2],
    [8,2,6,1,9,5,3,4,7],
    [3,7,4,6,8,2,9,1,5],
    [9,5,1,7,4,3,6,2,8],
    [5,1,9,3,2,6,8,7,4],
    [2,4,8,9,5,7,1,3,6],
    [7,6,3,4,1,8,2,5,9]
    ]'''

        
