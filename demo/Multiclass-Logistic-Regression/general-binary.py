import matplotlib
matplotlib.use('TkAgg')

import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


random_points  = [ (np.random.rand(2) - np.array([0.5,0.5])) for i in range(5000)]

w1 = np.random.rand(2) - np.array([0.5,0.5])
w2 = np.random.rand(2) - np.array([0.5,0.5])
#w2 = np.random.rand(2) - np.array([0.5,0.5])
#w1 = w1/np.linalg.norm(w1)
#w2 = np.array([-2,-3])
#w3 = np.array([-4,7])

red = filter(lambda p: np.dot(p,w1)>np.dot(p,w2),random_points)
green = filter(lambda p: np.dot(p,w1)<=np.dot(p,w2),random_points)



print ("W1-red:",w1,"mag:",np.linalg.norm(w1))
print ("W2-green:",w2,"mag:",np.linalg.norm(w2))



plt.scatter(*zip(*red),color="red",marker=".",)
plt.scatter(*zip(*green),color="green",marker=".")
#print(*zip(*red))
#print(*zip(*green))
plt.plot([0,w1[0]],[0,w1[1]],'ro-')
plt.plot([0,w2[0]],[0,w2[1]],'go-')
plt.show()
