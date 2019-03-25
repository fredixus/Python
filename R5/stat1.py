"""
Statistic
"""
from collections import Counter
import matplotlib.pyplot as plt
import math

num_friends         = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,
                        12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,
                        9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,
                        7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,
                        5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
                        3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,
                        2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def make_friend_counts_histogram (num_friends):
    friend_counts   = Counter(num_friends)
    xs              = range(101)
    ys              = [friend_counts[x] for x in xs]
    plt.bar     (xs, ys)
    plt.axis    ([0,101,0,25])
    plt.title   ("Histogram of Friend Counts")
    plt.xlabel  ("# of friends")
    plt.ylabel  ("# of people")
    plt.show    ()

#make_friend_counts_histogram(num_friends)

def mean (x):
    return      sum(x)*1.0/len(x)

print(mean(num_friends))

def median (v):
    """ Mid value of vector """
    n           = len(v)
    sorted_v    = sorted(v)
    mid_p       = n // 2

    if          (n % 2 == 1):
      return    sorted_v[mid_p] 
    else:
        low     = mid_p-1
        high    = mid_p
        return  (sorted_v[low] + sorted_v[high])*1.0 / 2  

print(median(num_friends))

def quantile (x, p):
    """ Zwraca p-ta wartosc zbioru x """
    p_index = int(p * len(x))
    return sorted (x)[p_index]

print("Decyl \t0.10: %s"    % quantile(num_friends,0.10))
print("Kwantyl 0.25: %s"    % quantile(num_friends,0.25))
print("Kwantyl 0.75: %s"    % quantile(num_friends,0.75))
print("Decyl \t0.10: %s"    % quantile(num_friends,0.90))

def mode(x):
    """Dominanta - moda - wartosc wystepujaca najczesciej"""
    counts      = Counter (x)
    max_count   = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count
            ]

print(mode(num_friends))

def data_range(x):
    """Rozpietosc danych - dyspersja okresla zroznicowanie danych"""
    return max(x) - min(x)

print(data_range(num_friends))

def de_mean(x):
    """Przekszta?ca x poprzez odj?cie ?redniej """
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x] 

def vector_dot(u,v):
    return sum(v_i * u_i for v_i, u_i in zip(v,u))

def sum_of_squers(v):
    return vector_dot(v,v)

def variance(x):
    """Zak?ada ?e x ma przynajmniej dwa elementy"""
    n = len(x) 
    if n < 2: return -1
    else:
        deviation = de_mean(x)
        return sum_of_squers(deviation) / (n - 1)

print(variance(num_friends))

"""
Warto?? ta przypomina ?rednie odchylenie od ?redniej podniesione do kwadratu, 
ale zamiast dzeili? przez n, dzielimy przez n - 1. 
Tak naprawde podczas pracy z pr¢dk? du?ego zbioru danych x_bar jest tylko ESTYMAT? rzeczywistej ?redniej,
a wi?c zwykle (x_i - x_bar **2 jest oszacowanym zbyt nisko kwadratem odchylenia od ?redniej - 
to w?a?nie jest przyczyna tego, ?e dzielimy przez n - 1 a nie przez n). Ci??ko jest to zrozumie?, 
a wi?c cz?sto zamiast z tego parametru b?dziemy korzysta? z odchylenia standardowego.
"""

def standard_deviation(x):
    return math.sqrt(variance(x))

