import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('data/LoadingDataFromFiles.csv', delimiter=',', unpack=True)

plt.plot(x, y, label="Loaded from file!")

plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.title('Interesting Graph')
plt.legend()

plt.show()
