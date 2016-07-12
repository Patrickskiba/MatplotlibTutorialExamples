import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7, 8, 5, 11, 9]
eating = [2, 4, 2, 3, 3]
working = [6, 7, 8, 8, 6]
playing = [8, 6, 5, 4, 6]

slices = [7, 2, 2, 13]
activites = ['sleeping', 'eating', 'working', 'playing']
plt.pie(slices, labels=activites, colors=['c', 'm', 'r', 'b'])

plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.title('Interesting Graph')
plt.legend()

plt.show()
