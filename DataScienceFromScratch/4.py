#Wizualizacja
print("Wizualizacja 4")
from matplotlib import pyplot as plt

mention = [500,505]
years = [2013,2014]

plt.bar(years, mention, 0.8)
plt.xticks(years)

plt.ylabel("Ile razy uslyszalem fraze nauka o danych?")

plt.ticklabel_format(useOffset=False)

mislead = True

if mislead:
    plt.axis([2012.5,2014.5,499,506])
    plt.title("Look at the 'Huge' Increase!")
else:
    plt.axis([2012.5,2014.5,0,550])
    plt.title("Not So Huge Anymore.")
plt.show()
