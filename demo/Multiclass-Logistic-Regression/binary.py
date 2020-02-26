import matplotlib
matplotlib.use('TkAgg')

import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


random_points  = [ (np.random.rand(2) - np.array([0.5,0.5])) for i in range(5000)]

w1 = np.random.rand(2) - np.array([0.5,0.5])
#w2 = np.random.rand(2) - np.array([0.5,0.5])
#w1 = w1/np.linalg.norm(w1)
#w2 = np.array([-2,-3])
#w3 = np.array([-4,7])

red = filter(lambda p: np.dot(p,w1)>0,random_points)
blue = filter(lambda p: np.dot(p,w1)<=0,random_points)


#points={"red":red,"blue":blue}
#df=pd.DataFrame(data=points)

print("W1:",w1,"mag:",np.linalg.norm(w1))

plt.scatter(*zip(*red),color="red",marker=".")
plt.scatter(*zip(*blue),color="blue",marker=".")
#print(*zip(*red))
#print(*zip(*blue))
plt.plot([0,w1[0]],[0,w1[1]],'ro-')
plt.show()
