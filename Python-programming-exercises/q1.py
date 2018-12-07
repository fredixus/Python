#q1
"""
Question:

Write a program which will find all such numbers which are divisible by 7 but 
are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on 
a single line.

"""

begin = 2000
# create new variable begin - set up start of section
end = 3200
# create new variable end - set up end of section

word = []
#create new empty list with name word

while begin <= end:
#do until begin is less or equal to end
    if begin % 7 == 0 and begin % 5 !=0:
    #chcech current number - begin if are divisible by 7 but are not a multiple of 5  
        word.append(begin)
        #add new number after previous
    begin+=1
    #to begin number add 1 to reach next number
    
print(word)
#print word into the screen
