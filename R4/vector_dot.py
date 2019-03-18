"""
4_7
Vector dot
"""

def vector_dot(u,v):
    return sum(v_i * u_i for v_i, u_i in zip(v,u))

# a = [1,2] 
# b = [3,2]

# print(vector_dot(a,b))
