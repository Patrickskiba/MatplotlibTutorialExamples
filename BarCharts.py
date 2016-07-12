import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

x2 = [3, 4, 21, 4, 10]
y2 = [6, 7, 8, 2, 4]

plt.bar(x, y, label='Bars1', color='green')
plt.bar(x2, y2, label='Bars2', color='purple')

plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.title('Interesting Graph')
plt.legend()

plt.show()
