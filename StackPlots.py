import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7, 8, 5, 11, 9]
eating = [2, 4, 2, 3, 3]
working = [6, 7, 8, 8, 6]
playing = [8, 6, 5, 4, 6]

plt.plot([], [], color='m', label='Sleeping')
plt.plot([], [], color='c', label='Eating')
plt.plot([], [], color='r', label='Working')
plt.plot([], [], color='k', label='Playing')

plt.stackplot(days, [sleeping, eating, working, playing], colors=['m', 'c', 'r', 'b'])

plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.title('Interesting Graph')
plt.legend()

plt.show()
