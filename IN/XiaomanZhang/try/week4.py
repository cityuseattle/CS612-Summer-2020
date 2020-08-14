import numpy as np 
import pandas as pd 
np.random.seed(1234)
#create dataframe data1
data1 = pd.DataFrame(np.random.randint(0,49,size = (6,8)), index = ['A','B','C','D','E','F'], columns = ['One','Two','Three','Four','Five','Six','Seven','Eight'])
#caculate IQR for each row
IQR = data1.quantile(.75, axis= 1) - data1.quantile(.25, axis= 1)
#caculate CV for each row
CV = data1.std(axis =1)/ data1.mean(axis =1)
#add IQR as a new column
data1['IQR'] = IQR
#add CV as a new column
data1['CV'] = CV
#caculate mean for each column
mean = data1.mean(axis = 0)

#add mean as a new row
data1.loc['mean'] = mean

print(data1)


