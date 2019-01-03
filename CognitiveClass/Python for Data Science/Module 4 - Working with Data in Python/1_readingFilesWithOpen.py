#From lecture

File1 = open("/examples/data/test.txt","w")
#print on screen: "/examples/data/test.txt" 
print(File1.name)
#print on screen: "w" 
print(File1.mode)

#always close the file:
File1.close()

"""
Beter practise is to open files with "with"
"""

with open("example.txt","r") an File1:
  file_stuff = File1.read()
  print(file_stuff)

print(File1.closed)
print(file_stuff)

"""
print(file_stuff)
return the file:
line 1,
line 2,
...
line x.
x < file.length()
"""
#you can take every element in file as a list object

with open("example.txt","r") an File1:
  file_stuff = File1.readlines()
  print(file_stuff)
  
"""
return the:
['line 1','line 2',...,line x]
x < file.length()
"""

with open("example.txt","r") an File1:
  file_stuff = File1.readline()
  print(file_stuff)
#print single line of file
  
with open("example.txt","r") an File1:
  for line in File1:
     print(line)
#print every single line of file   

with open("example.txt","r") an File1:
  file_stuff = File1.readlines(Z) #Z - any number - specify the number of character from every line.
  print(file_stuff)
 
#LABS
#https://gist.github.com/c1962f8cf7f0dc739d4e60b1ee3b5a2d


  
