"""
4_5
Multiply (*) vector by scalar 
example: [a = (1,2); 2: a * b = (2,4)]
"""
def scalar_multiply(c,v):
    """ c * [x,y] = [c*x,c*y]"""
    return [c * v_i for v_i in v]

# b = [3,2]
# c = 2
# print(scalar_multiply(c,b))