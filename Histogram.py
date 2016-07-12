import matplotlib.pyplot as plt

population_age = [3,5,1,5,23,25,123,54,52,92,17,43]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

plt.hist(population_age, bins, histtype='bar', rwidth=0.8)

plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.title('Interesting Graph')
plt.legend()

plt.show()
