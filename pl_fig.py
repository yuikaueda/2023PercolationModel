import numpy as np
import matplotlib.pyplot as plt

data1 = np.loadtxt('tlong_change_n80_200_a001_b5.dat')
data2 = np.loadtxt('tlong_change_n150_200_a001_b5.dat')

x1 = data1[:,0]
y1 = data1[:,1]

x2 = data2[:,0]
y2 = data2[:,1]

l1 = []
p1 = []
l2 = []
p2 = []

for i in range(len(x1)):
    if 0 <= x1[i] <= 200:
        l1.append(x1[i])
        p1.append(y1[i])

for i in range(len(x2)):
    if 0 <= x2[i] <= 200:
        l2.append(x2[i])
        p2.append(y2[i])



fig, axe = plt.subplots(1, 1)

axe.plot(l1, p1, 'o-', c='black', label = r'$N_{s}=80$')#'$k_{on}^{c}=2,k_{off}=0.2$')
axe.plot(l2, p2, 's-', c='red', label = r'$N_{s}=150$')#'$k_{on}^{c}=5,k_{off}=0.2$')
#axe.plot(l3, p3, 'v-', c='blue', label = r'$N_{s}=150$')#'$k_{on}^{c}=10,k_{off}=0.2$')
#axe.plot(l4, p4, '-p',  c='green', label =r'$N_{s}=200$')#'$k_{on}^{c}=20,k_{off}=0.2$')
plt.xlabel("Time", fontsize = 18)
#plt.ylabel("Percolatin Probability", fontsize = 18)
plt.ylabel("Percolation plobability", fontsize = 18)
#plt.ylim(0, 1.1)
#plt.xlim(0, 100)
#plt.margins(x=5)
axe.legend(loc='best')
fig.savefig("chanege_t200_n80_150_to200.png")
plt.show()
