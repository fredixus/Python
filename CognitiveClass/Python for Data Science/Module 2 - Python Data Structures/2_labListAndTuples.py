#Lab Instructions  
#https://gist.github.com/fredixus/5abe9005a6d5e65ec819987d5cfb1787
#https://gist.github.com/b110b85f4ff3e722eed20d9aa706bea2


"""
How do I run Python?
You can use the CC Labs environment to run Python code in Jupyter notebooks, by simply clicking on the "Start Lab" button below.

Do I need to download or install Python?
No, you can use Python directly within your web browser, through CC Labs. Just click on the "Start Lab" button below and CC Labs will load directly on this page.

Which version is used in these labs: Python 2 or Python 3?
All of these labs use Python 3.

What is "CC Labs"?
CC Labs is a virtual lab environment that lets you practice what you learn in these courses.

What are "Jupyter Labs"?
Jupiter Labs is a popular data science tool that lets Data Scientists write code, see the results, and describe what's happening -- all in a single document.
"""

#lab tuples

# Create your first tuple
tuple1 = ("disco",10,1.2 )
tuple1

# Print the type of the tuple you created
type(tuple1)

# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# Print the type of value on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# Use negative index to get the value of the last element
tuple1[-1]

# Use negative index to get the value of the last element
tuple1[-1]

# Use negative index to get the value of the third last element
tuple1[-3]

# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
tuple2

# Slice from index 0 to index 2
tuple2[0:3]

# Slice from index 3 to index 4
tuple2[3:5]

# Get the length of tuple
len(tuple2)

# A sample tuple
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple
RatingsSorted = sorted(Ratings)
RatingsSorted

# Create a nest tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

# Print element on each index
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

# Print the first element in the second nested tuples
NestedT[2][1][0]

# Print the second element in the second nested tuples
NestedT[2][1][1]

# Print the first element in the second nested tuples
NestedT[4][1][0]

# Print the second element in the second nested tuples
NestedT[4][1][1]


#Quiz on Tuples
#Find the length of the tuple, genres_tuple:
# sample tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple

len(genres_tuple)

