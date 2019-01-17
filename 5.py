#Wizualizacja
print("Wizualizacja 5")
from matplotlib import pyplot as plt

variance        = [1,2,4,8,16,32,64,128,256]
bias_squared    = [256,128,64,32,16,8,4,2,1]

total_error = [x + y for x,y in zip(variance,bias_squared)]
