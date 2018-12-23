#dictionaries

#QUESTION 1
"""
Consider the following dictionary:
D={'a':0,'b':1,'c':2}
What is the result of the following: D.values()

() dict_keys([0, 1, 2])
(*) dict_values([0, 1, 2]) 
() dict_values(['a', 'b', 'c'])
() dict_keys(['a', 'b', 'c'])
"""

#QUESTION 2
"""
Consider the following dictionary:
D={'a':0,'b':1,'c':2}
What is the output of the following D['b'] :

() 0
(*) 1
() 2
"""

#Labs
# https://gist.github.com/8ebfd2a428de25a2b7c5b7724696ae77

A = {"a":1,"b":2,"c":3}
print(A)

A["d"] = 4
print(A)

del(A("a"))
print(A)

print("c" in A)
print("a" in A)

print(A.keys())
print(A.values())
