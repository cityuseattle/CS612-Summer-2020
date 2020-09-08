Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import seaborn as sb
Matplotlib is building the font cache; this may take a moment.
>>> df=sb.load_dataset('tips')
>>> df
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2

[244 rows x 7 columns]
>>> df.sum(numeric_only=True, skipna=True)
total_bill    4827.77
tip            731.58
size           627.00
dtype: float64
>>> df.mean(numeric_only=True, skipna=True)
total_bill    19.785943
tip            2.998279
size           2.569672
dtype: float64
>>> df.dropna().describe()
       total_bill         tip        size
count  244.000000  244.000000  244.000000
mean    19.785943    2.998279    2.569672
std      8.902412    1.383638    0.951100
min      3.070000    1.000000    1.000000
25%     13.347500    2.000000    2.000000
50%     17.795000    2.900000    2.000000
75%     24.127500    3.562500    3.000000
max     50.810000   10.000000    6.000000
>>> df.groupby('time').sum()
        total_bill     tip  size
time                            
Lunch      1167.47  185.51   164
Dinner     3660.30  546.07   463
>>> df.groupby('time')['size'].sum()
time
Lunch     164
Dinner    463
Name: size, dtype: int64
>>> for(time, group) in df.groupby('time'):
	print(f'{time}:\n{group}')

	
Lunch:
     total_bill   tip     sex smoker   day   time  size
77        27.20  4.00    Male     No  Thur  Lunch     4
78        22.76  3.00    Male     No  Thur  Lunch     2
79        17.29  2.71    Male     No  Thur  Lunch     2
80        19.44  3.00    Male    Yes  Thur  Lunch     2
81        16.66  3.40    Male     No  Thur  Lunch     2
..          ...   ...     ...    ...   ...    ...   ...
222        8.58  1.92    Male    Yes   Fri  Lunch     1
223       15.98  3.00  Female     No   Fri  Lunch     3
224       13.42  1.58    Male    Yes   Fri  Lunch     2
225       16.27  2.50  Female    Yes   Fri  Lunch     2
226       10.09  2.00  Female    Yes   Fri  Lunch     2

[68 rows x 7 columns]
Dinner:
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2

[176 rows x 7 columns]
>>> df.groupby('time')['tip'].describe()
        count      mean       std   min  25%   50%     75%   max
time                                                            
Lunch    68.0  2.728088  1.205345  1.25  2.0  2.25  3.2875   6.7
Dinner  176.0  3.102670  1.436243  1.00  2.0  3.00  3.6875  10.0
>>> df.groupby('time').aggregate(['min',np.median,max])
       total_bill                  tip              size           
              min  median    max   min median   max  min median max
time                                                               
Lunch        7.51  15.965  43.11  1.25   2.25   6.7    1      2   6
Dinner       3.07  18.390  50.81  1.00   3.00  10.0    1      2   6
>>> df.groupby('time').aggregate({'tip':max,'size': min})
         tip  size
time              
Lunch    6.7     1
Dinner  10.0     1
>>> df.groupby('time').filter(lambda x: X['size'].std()>1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    df.groupby('time').filter(lambda x: X['size'].std()>1)
  File "C:\Users\Jamie Sim\AppData\Local\Programs\Python\Python38-32\lib\site-packages\pandas\core\groupby\generic.py", line 1617, in filter
    res = func(group, *args, **kwargs)
  File "<pyshell#16>", line 1, in <lambda>
    df.groupby('time').filter(lambda x: X['size'].std()>1)
NameError: name 'X' is not defined
>>> df.groupby('time').filter(lambda x: x['size'].std()>1)
     total_bill   tip     sex smoker   day   time  size
77        27.20  4.00    Male     No  Thur  Lunch     4
78        22.76  3.00    Male     No  Thur  Lunch     2
79        17.29  2.71    Male     No  Thur  Lunch     2
80        19.44  3.00    Male    Yes  Thur  Lunch     2
81        16.66  3.40    Male     No  Thur  Lunch     2
..          ...   ...     ...    ...   ...    ...   ...
222        8.58  1.92    Male    Yes   Fri  Lunch     1
223       15.98  3.00  Female     No   Fri  Lunch     3
224       13.42  1.58    Male    Yes   Fri  Lunch     2
225       16.27  2.50  Female    Yes   Fri  Lunch     2
226       10.09  2.00  Female    Yes   Fri  Lunch     2

[68 rows x 7 columns]
>>> df.groupby('time').std()
        total_bill       tip      size
time                                  
Lunch     7.713882  1.205345  1.040024
Dinner    9.142029  1.436243  0.910241
>>> df.groupby('time').transform(lambda x:x+x.std())
     total_bill       tip      size
0     26.132029  2.446243  2.910241
1     19.482029  3.096243  3.910241
2     30.152029  4.936243  3.910241
3     32.822029  4.746243  2.910241
4     33.732029  5.046243  4.910241
..          ...       ...       ...
239   38.172029  7.356243  3.910241
240   36.322029  3.436243  2.910241
241   31.812029  3.436243  2.910241
242   26.962029  3.186243  2.910241
243   27.922029  4.436243  2.910241

[244 rows x 3 columns]
>>> df.groupby('time').apply(lambda x:x['tip']+x['size'])
time       
Lunch   77     8.00
        78     5.00
        79     4.71
        80     5.00
        81     5.40
               ... 
Dinner  239    8.92
        240    4.00
        241    4.00
        242    3.75
        243    5.00
Length: 244, dtype: float64
>>> pd.pivot_table(df, index='time', columns='sex',values='tip',aggfunc=sum,fill_value=0)
sex       Male  Female
time                  
Lunch    95.11   90.40
Dinner  389.96  156.11
>>> 