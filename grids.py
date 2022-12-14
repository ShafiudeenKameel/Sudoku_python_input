#easy_puzzle
'''QE4=

AE4=[
    [4,3,5,2,6,9,7,8,1],
    [6,8,2,5,7,1,4,9,3],
    [1,9,7,8,3,4,5,6,2],
    [8,2,6,1,9,5,3,4,7],
    [3,7,4,6,8,2,9,1,5],
    [9,5,1,7,4,3,6,2,8],
    [5,1,9,3,2,6,8,7,4],
    [2,4,8,9,5,7,1,3,6],
    [7,6,3,4,1,8,2,5,9]
    ]

QE5=[
    [1,0,0,4,8,9,0,0,6],[7,3,0,0,0,0,0,4,0],[0,0,0,0,0,1,2,9,5],[0,0,7,1,2,0,6,0,0],[5,0,0,7,0,3,0,0,8],[0,0,6,0,9,5,7,0,0],[9,1,4,6,0,0,0,0,0],[0,2,0,0,0,0,0,3,7],[8,0,0,5,1,2,0,0,4]
    ]

AE5=[
    [1,5,2,4,8,9,3,7,6],[7,3,9,2,5,6,8,4,1],[4,6,8,3,7,1,2,9,5],[3,8,7,1,2,4,6,5,9],[5,9,1,7,6,3,4,2,8],[6,4,6,8,9,5,7,1,3],[9,1,4,6,3,7,5,8,2],[6,2,5,9,4,8,1,3,7],[8,7,3,5,1,2,9,6,4]]
'''
import random

def easy_puzzle():
    

    Q1=[
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

    Q2=[
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
        

    A1=[
        [4,3,5,2,6,9,7,8,1],
        [6,8,2,5,7,1,4,9,3],
        [1,9,7,8,3,4,5,6,2],
        [8,2,6,1,9,5,3,4,7],
        [3,7,4,6,8,2,9,1,5],
        [9,5,1,7,4,3,6,2,8],
        [5,1,9,3,2,6,8,7,4],
        [2,4,8,9,5,7,1,3,6],
        [7,6,3,4,1,8,2,5,9]
       ]

    A2=[
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

    QL=(Q1,Q2)
    AL=(A1,A2)

    Q=random.choice(QL)

    i=QL.index(Q)

    A=AL[i]

    F=(Q,A)

    return F

def medium_puzzle():

    Q1
    Q2
    Q3
    A1
    A2
    A3
     
    QL=(Q1,Q2,Q3)
    AL=(A1,A2,A3)

    Q=random.choice(QL)

    i=QL.index(Q)

    A=AL[i]

    F=(Q,A)

    return F
    
def hard_puzzle():

    Q1
    Q2
    Q3
    A1
    A2
    A3
     
    QL=(Q1,Q2,Q3)
    AL=(A1,A2,A3)

    Q=random.choice(QL)

    i=QL.index(Q)

    A=AL[i]

    F=(Q,A)

    return F

#print(easy_puzzle())
        

    
        
