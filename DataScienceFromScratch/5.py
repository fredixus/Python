#Wizualizacja
print("Wizualizacja 5")
from matplotlib import pyplot as plt

variance        = [1,2,4,8,16,32,64,128,256]
bias_squared    = [256,128,64,32,16,8,4,2,1]

total_error     = [x + y for x,y in zip(variance,bias_squared)]

xs              = range(len(variance))

plt.plot    (xs,variance,       'g-',   label='variance')
plt.plot    (xs,bias_squared ,  'r-.',  label='bias^2')
plt.plot    (xs,total_error ,   'b:',   label='total error')

plt.legend  (loc=9)
plt.xlabel  ("Stopien skomplikowania modelu")
plt.title   ("Kompromis miedzy wartoscia progowa i zlozonoscia modelu")
plt.show    ()
