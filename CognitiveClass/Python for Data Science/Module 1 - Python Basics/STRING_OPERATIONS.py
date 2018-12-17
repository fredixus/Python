#STRING OPERATIONS
Letters="ABCDEFGHIJK"
Good="GsoAo+d"
x = "uppercase"
print(x.upper())

test = 30*"I don't late for school again"
print(test)

print("Michael Jackson" == 'Michael Jackson')
print("Michael Jackson" == 'michael Jackson')
print("michael Jackson" == 'Michael Jackson')

print('@#2_#]&*^%$')

Name = "Michael Jackson"
Name

print(Name[0])
print(Name[6])
print(Name[13])

print(Name[-1])
print(Name[-15])

z = len("Michael Jackson")
print(z)
# Get every second element. The elments on index 1, 3, 5 ...
print(Name[0:4],Name[8:12])
# Get every second element in the range from index 0 to index 4
print(Name[::2],Name[0:5:2])

# Concatenate two strings
Statement = Name + "is the best"
Statement

# Print the string for 3 times
3 * "Michael Jackson"

# Concatenate strings
Name = "Michael Jackson"
Name = Name + " is the best"

# New line escape sequence
print(" Michael Jackson \n is the best" )

# Tab escape sequence
print(" Michael Jackson \t is the best" )

# Include back slash in string
print(" Michael Jackson \\ is the best" )

# r will tell python that string will be display as raw string
print(r" Michael Jackson \ is the best" )

# Convert all the characters in string to upper case
A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)

# Replace the old substring with the new target substring is the segment has been found in the string
A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
B

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
Name = "Michael Jackson"
Name.find('el')

# Find the substring in the string.
Name.find('Jack')

# If cannot find the substring in the string
Name.find('Jasdfasdasdf')


