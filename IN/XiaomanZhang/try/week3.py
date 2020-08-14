import numpy as np

nwalks = 5000
nsteps = 1000
np.random.seed(1234)

steps = np.random.normal(loc=0, scale= 0.25, size =(nwalks, nsteps))
steps = np.where(steps > 0, 1 , -1)
walks = steps.cumsum(axis = 1)
hits50 = (walks <= -50).any(1)
num = hits50.sum() #caculate the count number of True values
print("The number of random walks that hit -50:", num)

crossing_times = (walks[hits50] <= -50).argmax(1)
averageTime = crossing_times.mean()
print("The average minimum crossing time: ",averageTime )




