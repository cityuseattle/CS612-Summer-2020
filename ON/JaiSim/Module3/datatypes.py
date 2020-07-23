Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> dt = np.array([1,2])
>>> print(dt.dtype)
int32
>>> dt=np.array([1.0,2.0])
>>> print(dt.dtype)
float64
>>> dt=np.array([1,2], dtype=np.float64)
>>> print(dt)
[1. 2.]
>>> print(dt.dtype)
float64
>>> 