#QUESTION 1

"""
What is the result of the following lines of code:
S={'A','B','C'}
U={'A','Z','C'}
U.union(S)

(*) {'A', 'B', 'C', 'Z'} 
() {'A','Z','C'}
() {'A','B','C'}
() {'A'}
"""

#QUESTION 2

"""
What is the intersection of set S and U
S={'A','B','C'}
U={'A','Z','C'}

() {'A','B','C'}
() {'A','B','C','Z'}
(*) {'A','C'}
() {'A','B','C','Z'}
"""

#LABS
#https://gist.github.com/cc0772c74f21638962b45fb39cf6d596

list = []
#conver to set
x = set(list)
print(x)

A = {"A","B","C"}
A.add("D")
A.add("D")
A.remove("A")

print(A)
print("A" in A)
print("B" in A)

A = {"A","B","C","D"}
B = {"B","C","D","E","F"}

print(A & B)
print(A.intersection(B))

print(A.union(B))

C = {"B","C"}
print(B.issubset(A))
