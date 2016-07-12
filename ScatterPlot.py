import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [2,3,4,5,7,2,3,4]

plt.scatter(x,y,label='skitscat', color='blue', marker='x')

plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.title('Interesting Graph')
plt.legend()

plt.show()
