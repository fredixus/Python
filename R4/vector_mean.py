"""
4_6
Mean of vector point
"""
from vector_sum import vector_sum
from scalar_multiply import scalar_multiply

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1.0/n,vector_sum(vectors))

# a = [1,1] 
# b = [8,8]
# c = [3,3]

# sum = [a]+[b]+[c]
# print(vector_mean(sum))