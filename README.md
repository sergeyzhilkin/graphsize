#Simple usage  
python3 graph.py 

#Description  
Function 'fsize' accepts matrix (list of lists with 1 and 0 characters), calculates number of figures in this matrix, size of every figure, returns size of the biggest figure.
Figure consists of '1' charachters connected vertically or horizontally (not diagonally)
Figure also can be a single '1' character 

for example here we are have three figures: square, cross and single 1.

a = [  
         [1,1,0,0,1],  
         [1,1,0,0,0],  
         [0,0,0,1,0],  
         [0,0,1,1,1],  
         [0,0,0,1,0]  
]  
  
fsize(a)  
  
number of figures: 3  
size of the biggest figure: 5

