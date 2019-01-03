#From lecture

File1 = open("/examples/data/test.txt","w")
#print on screen: "/examples/data/test.txt"
print(File1.name)
#print on screen: "w" #create new file
print(File1.mode)

File1.write("Simple text \n")
File1.write("Simple text - next line \n")

#always close the file:
File1.close()

Lines = ['line 1','line 2','line 3']

with open("example.txt","w") an File1:
  for line in Lines:
    File1.write(line)

with open("example.txt","a") an File1: #don't create new file (open existing)
    File1.write("Next line")
    
#copy the file:

with open("example.txt","r") an readFile:
  with open("example.txt","w") an copyFile:
    for line in readFile:
      copyFile.write(line) 

#LABS
#https://gist.github.com/b96188b3699a39b260da3df2cbb2b9fe

