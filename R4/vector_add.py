"""
4_2
Add (+) two vectors 
example: [a = (1,2); b = (3,2): a + b: (4,4)]
"""
def vector_add(v, w):
    """(+)"""
    return [v_i + w_i for v_i, w_i in zip(v,w)]

# a = [1,2] 
# b = [3,2]

#print(vector_add(a,b))