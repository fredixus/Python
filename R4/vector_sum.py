"""
4_4
Sum of vectors in list 
example: [a = (1,2); b = (3,2);c = (1,1): a + b + c: (5,5)]
"""

from vector_add import vector_add

def vector_sum(vectors):
    """(+) of vectors"""
    result = vectors [0]
    for vector in vectors[1:]:
        result = vector_add(result,vector)
    return result

a = [1,2] 
b = [3,2]
c = [1,1]

sum = [a]+[b]+[c]
print(vector_sum(sum))