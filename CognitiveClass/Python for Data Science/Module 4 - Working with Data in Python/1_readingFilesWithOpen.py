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
