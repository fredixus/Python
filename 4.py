#Wizualizacja
print("Wizualizacja 4")
from matplotlib import pyplot as plt

mention = [500,505]
years = [2013,2014]

plt.bar(years, mention, 0.8)
plt.xticks(years)

plt.ylabel("Ile razy usłyszałem frazę nauka o danych?")

plt.ticklabel_format(useOffset=False)

#plt.axis([2012.5,2014.5,499,506])
plt.show()
