#Wizualizacja
print("Wizualizacja 2")
from matplotlib import pyplot as plt

movies = ["Annie Hall","Ben-Hur","Casablanca","Gandhi","West Side Story"]
oscars = [5,11,3,8,10]

xs = [i for i, _ in enumerate(movies)]
#set up width

plt.bar(xs, oscars)
#draw the bars for x[xs] with height[oscars]
plt.ylabel("Liczba nagrod")
plt.title("Moje ulubione filmy")

plt.xticks([i for i, _ in enumerate(movies)],movies)

plt.show()
