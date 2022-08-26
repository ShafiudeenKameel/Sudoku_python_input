from tkinter import *
root=Tk()


#GRIDS
Qg=[                    #question
    [1,0,0,4,8,9,0,0,6],
    [7,3,0,0,0,0,0,4,0],
    [0,0,0,0,0,1,2,9,5],
    [0,0,7,1,2,0,6,0,0],
    [5,0,0,7,0,3,0,0,8],
    [0,0,6,0,9,5,7,0,0],
    [9,1,4,6,0,0,0,0,0],
    [0,2,0,0,0,0,0,3,7],
    [8,0,0,5,1,2,0,0,4]

]
Ag=[                    #answer
    [1,5,2,4,8,9,3,7,6],
    [7,3,9,2,5,6,8,4,1],
    [4,6,8,3,7,1,2,9,5],
    [3,8,7,1,2,4,6,5,9],
    [5,9,1,7,6,3,4,2,8],
    [6,4,6,8,9,5,7,1,3],
    [9,1,4,6,3,7,5,8,2],
    [6,2,5,9,4,8,1,3,7],
    [8,7,3,5,1,2,9,6,4]
]


        
def easy():
   

        for x in range(0,9):

            for y in range(0,9):

                

                lab=Label(root,text=Qg[x][y],width=8,height=4,bg='pink',borderwidth = 2,relief='groove')
                lab.grid(row=x+1,column=y+1)
        

        #chossing
        lab2=Label(root,text="COORDINATES:",width=15,height=3,bg="black",fg="white")
        lab2.grid(row=13,column=0)

        Re=Entry(root,width=10)#rowentry
        Re.grid(row= 15, column = 0)
        Re.insert(0,"ROW-")

        Ce=Entry(root,width=10)#COLUMNentry
        Ce.grid(row= 16, column = 0)
        Ce.insert(0,"COLUMN-")

        N=Entry(root,width=20)
        N.grid(row=17,column=0)
        N.insert(0,"Enter the number-")

        '''def GO():

            global Qg, Ag, Re, Ce
            
            Re=int(Re.get())
            Ce=int(Ce.get())
            
            if Qg[Re-1][Ce-1]==Ag[Re-1][Ce-1]:
                Qg[Re-1][Ce-1]=N'''

                
            
            
        but2=Button(root,text="GO!",width=5,bg="black",fg="white",command=GO)
        but2.grid(row=19,column=5)
            

            

        
#start_easy
but=Button(root,text="EASY",width=5,bg="blue",fg="black",command=easy).grid(row=0,column=5)
root.mainloop()



