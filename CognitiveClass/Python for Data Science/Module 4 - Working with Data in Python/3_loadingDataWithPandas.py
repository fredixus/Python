#Lecture

"""
QUESTION 1  
Consider the dataframe df, how would you find the element in the second-row and first column.

() df.ix[0,1] or df.iloc[0,1]  
(*) df.ix[1,0] or df.iloc[1,0]  
() df[1,1]
"""

"""
QUESTION 2  
will the following code run

import pandas as banana
df=banana.DataFrame({'a':[11,21,31],'b':[21,22,23]})
df.head()

(*) yes
() no  
"""

import pandas
#import liblary pandas

csv_path = "file1.csv"
df = pandas.read_csv(csv_path)

#you can import panda in another way:
"""
import pandas as pd
csv_path = "file1.csv"
df = pd.read_csv(csv_path)
"""

df.head()
#return a first 5 row of csv file

xlsx_path="file1.xlsx"
df = pandas.read_excel(xlsx_path)
#you can open xlsx files as above

songs = {'Album':['A','B','C','D'],'Number':[1,2,3,4],'Autor':['Adam','Banan','Cion','Dion']}
songs_F = pandas.DataFrame(songs)

print(songs_F["Album"])

print(songs_F[["Album",'Autor']])

#first row and column:
print(songs_F.ix[0,0])

#secound row and first column:
print(songs_F.ix[1,0])

#first row and third column:
print(songs_F.ix[0,2])

#first row and column "Number":
print(songs_F.ix[0,"Number"])

#third row and column "Number":
print(songs_F.ix[2,"Number"])

# assign to variable 2 rows and 3 columns
z = songs_F.ix[0:2,0:3]

