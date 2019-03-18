"""
4_6
Mean of vector point
"""
from vector_sum import vector_sum
from scalar_multiply import scalar_multiply

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))