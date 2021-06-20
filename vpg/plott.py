import matplotlib.pyplot as plt
f = open('results.txt','r')
a = f.read().split()
l = []
s = 0
for i in range(1,200):
	s += float(a[i-1])
	if i%2 == 0:
		l.append(s/2)
		s = 0
plt.xlabel('No. of Epochs')
plt.ylabel('Average return')
plt.plot(l)
plt.show()
