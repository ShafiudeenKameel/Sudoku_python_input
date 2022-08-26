from tkinter import *

root=Tk()
bg="black"

class main:

    
     def display_grid(self,level):
          self.level=level

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
          
          root1=Toplevel()
          
          for x in range(0,9):

            for y in range(0,9):

                lab=Label(root1,text=Qg[x][y],width=6,height=3,bg='pink',borderwidth = 2,relief='groove')
                lab.grid(row=x+1,column=y+1)

          def GO():

               nonlocal Qg, Ag

               if(Qg==Ag):
                    #messagebox.showinfo("YAY!","YOU HAVE SUCCESSFULLY COMPLETED THE PUZZLE")
                    rooT1.destroy()

               else:
                    #messagebox.showinfo("oh no","Try Again")
                    labxyz=Label(root1,text="yay").grid(row=20,column=0)
                    
               re=int(RE.get())
               ce=int(CE.get())
               n=int(N.get())

               
               '''if (n==Ag[re][ce]):
                         Qg[re][ce]=n
                         labUPDATE=Label(root1,text=n,width=6,height=3,bg="light green",borderwidth=2,relief='groove')
                         labUPDATE.grid(row=re,column=ce)

               else:
                         self.display_grid(level)'''

               
                   
          #choosing

          frame1=LabelFrame(root1,text="COORDINATES:",padx=50,pady=50)
          frame1.grid(row=13,column=0,columnspan=9,padx=5,pady=5)

          
          labR=Label(frame1,text="ROW:",width=5)
          labR.grid(row=14,column=0,)
          RE=Entry(frame1,width=5)#rowentry
          RE.grid(row= 14, column = 2)
          
          labC=Label(frame1,text="COLUMN:",width=20)
          labC.grid(row=15,column=0)
          CE=Entry(frame1,width=5)#COLUMNentry
          CE.grid(row= 15, column = 2)

          
          labN=Label(frame1,text="Enter The Number:",width=20)
          labN.grid(row=16,column=0)        
          N=Entry(frame1,width=5)
          N.grid(row=16,column=2)
          

          #check_button

          butGO=Button(root1,text="GO!",width=5,bg="black",fg="gold",command=GO)
          butGO.grid(row=18,column=5)
          

obj=main()


'''starting with buttons'''
#start_easy
butE=Button(root,text="EASY",width=10,bg="light blue",fg="black",command=lambda : obj.display_grid("EASY")).grid(row=0,column=5,padx=50,pady=10)

#start_medium
butM=Button(root,text="MEDIUM",width=10,bg="orange",fg="black",command=lambda : obj.display_grid("MEDIUM")).grid(row=1,column=5,padx=50,pady=10)

#start_hard
butH=Button(root,text="HARD",width=10,bg="coral",fg="black",command=lambda : obj.display_grid("HARD")).grid(row=2,column=5,padx=50,pady=10)

#go_back_to_main_menu
butMENU=Button(root,text="GO BACK",width=10,bg="lavender",fg="black",command=root.destroy).grid(row=4,column=5,padx=50,pady=50)


root.mainloop()
