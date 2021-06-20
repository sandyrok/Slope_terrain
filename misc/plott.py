import matplotlib.pyplot as plt
import numpy as np
f = open('training5.txt', 'r')

a = [float(x) for x in f]
a = [np.mean(a[i:i+3]) for i in range(0,len(a)-5,6)]
plt.plot(range(1,len(a)+1), a)
plt.xlabel("Epochs")
plt.ylabel("Average Return")
plt.title("PPO with Linear Activation")
plt.show()
