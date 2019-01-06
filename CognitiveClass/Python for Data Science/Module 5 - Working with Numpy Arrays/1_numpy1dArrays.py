#lecture

"""
- the basics and array creation
- indexing and slicing
- basic operations
- universal functions
"""

#how to create np array
import numpy as np
a = np.array([0,1,2,3,4])
#a[0] --> 0
#a[3] --> 3

type(a)
#returns numpy.ndarray

a.dtype
#return dtype('int64')

a.size
#return 5

a.ndim
#return how many D (dimensions): 1

a.shape(5,)
#dimensions of the array

b=np.array([3.1,11.02,6.2,2.5])
type(b) #numpy.ndarray
a.dtype #dtype('float64')


c = np.array([20,1,2,3,4])
c [0] = 100
c #array([100,1,2,3,4])

c [4] = 0
c #array([100,1,2,3,0])

d = c[1:4]
d #array([1,2,3])

c[3:5]=300,400
c #array([100,1,2,300,400])

#vector adding
u = np.array([1,0])
v = np.array([0,1])

z = u + v
z #array([1,1])

z = u - v
z #array([1,-1])

y =  np.array([1,2])
z = 2*y
z #array([1,4])

#vector product
u = np.array([1,2])
v = np.array([3,2])

z = u * v
z #array([3,4])

#dot product u^T v
# represents how similar dwo vectors are
u = np.array([1,2])
v = np.array([3,2])

z = np.dot(u,v)
z #5

#adding const
u = np.array([1,2,3,-1])
z = u + 1
z #array([2,3,4,0])

#universal functions
a = np.array([1,-1,1,-1])
mean_a = a.mean() #0

b = np.array([1,-2,3,4,5])
max_b=b.max() #5

np.pi #3,141592
x=np.array([0,np.pi/2,np.pi])
y = np.sin(x)
y #([0,1,1.2e-16])

np.linspace(-2,2,num=5)
#start point of sequence: -2
#end point of sequence: 2
#num = how many samples are indicate -- space bettwen numbers is one
#[-2,-1,0,1,2]

np.linspace(-2,2,num=9)
#[-2,-1.5,-1,-0.5,0,0.5,1,1.5,2]

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
import matplotlib.pyplot as plt

%matplotlib line
plt.plot(x,y)


#Questions:

"""
QUESTION 1
What is the result of the following operation
np.array([1,-1])*np.array([1,1])

() array([ 0, 0]) 
(*) array([ 1, -1])  
() 0
"""

"""
QUESTION 2
What is the result of the following operation
np.dot(np.array([1,-1]),np.array([1,1]))

() array([ 0, 0]) 
() array([ 1, -1])  
(*) 0
"""

#Labs to lecture
#https://gist.github.com/690a19e28ec32305864270c881786df4

#full labs
https://gist.github.com/0928d12fd7eea5f0a9d863dabfd7c8f0



