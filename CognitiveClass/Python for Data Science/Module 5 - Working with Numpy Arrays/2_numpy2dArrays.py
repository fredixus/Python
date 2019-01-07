"""
QUESTION 1
how many rows is the following numpy array:
A=np.array([[1,2],[3,4],[5,6],[7,8]])

() 2  
(*) 4 
() 6
"""

"""
QUESTION 2
how can you perform the following operation :
A=np.array([[1,2],[3,4],[5,6],[7,8]])
B=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.dot(A,B)

() yes  
(*) no
"""

#lecture
a=[[11,12,13],[21,22,23],[31,32,33]]
A = np.array(a)
A.ndim
#2

A.shape
#(3,3) secound columns

A.size
#9 (3*3)

"""
A[0][0]; A[0][1]; A[0][2];
A[1][0]; A[1][1]; A[1][2];
A[2][0]; A[2][1]; A[2][2];
# first row
#secound to the column index
"""

"""
you can acces as folows:
A[1,2] == A[1][2] # TRUE
"""

#adding
X = np.array([[1,0],[0,1]])
Y = np.array([[2,1],[1,2]])

Z = X + Y

Z
#array([[3,1],[1,3]])

#the some as 1d
#you can multipy matrices only when for A * B where A number of columns is equal to B number of rows

#https://gist.github.com/dcc59705e035da1be0e54d10805ec314
#https://gist.github.com/2f0319319e7362fdcba3ec6cfe14e25e


