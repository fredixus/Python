"""
4_11
Distance
"""
from magniture import magnitude
from vector_sub import vector_sub

def distance(v,w):
    return magnitude(vector_sub(v,w))

# a = [1,2] 
# b = [3,2]

# print(distance(a,b))