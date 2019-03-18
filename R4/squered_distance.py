"""
4_10
Squered distance
"""
from sum_of_squers import sum_of_squers
from vector_sub import vector_sub

def squered_distance(v,w):
    return sum_of_squers(vector_sub(v,w))

# a = [1,2] 
# b = [3,2]

# print(squered_distance(a,b))