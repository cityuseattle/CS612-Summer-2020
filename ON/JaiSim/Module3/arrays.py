Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> arr=np.array([1,2,3])
>>> print(type(arr))
<class 'numpy.ndarray'>
>>> print(aa.dtype)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(aa.dtype)
NameError: name 'aa' is not defined
>>> print(arr.dtype)
int32
>>> print(arr.shape)
(3,)
>>> print(arr[0],arr[1],arr[2])
1 2 3
>>> print(arr)
[1 2 3]
>>> #create an array of zeros with 2 dim and size of 2 each
>>> zero = np.zeros((2,2))
>>> print(zero)
[[0. 0.]
 [0. 0.]]
>>> #create an array of ones with 1 dim and size of 2 each
>>> one=np.ones((1,2))
>>> print(one)
[[1. 1.]]
>>> #create a new aray with given shape, type, and filled with value
>>> constant = np.full((2,2),5)
>>> print(constant)
[[5 5]
 [5 5]]
>>> #create a 2-d array with 1 on diagonal and 0 on others
>>> diag=np.eye(3)
>>> print(diag)
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
>>> #diag starts at index 1
>>> diag = np.eye(4,k=1)
>>> print(diag)
[[0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]
 [0. 0. 0. 0.]]
>>> #Create an array with random values
>>> rand = np.random.random((2,2))
>>> print(rand)
[[0.62658334 0.16655746]
 [0.47962176 0.64296603]]
>>> #Aray Indexing
>>> arr = np.arange(10)
>>> print(arr[0:8:2])
[0 2 4 6]
>>> #create rank 2 with shape (3,4) array
>>> arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
>>> print(arr[:2,:2])
[[1 2]
 [5 6]]
>>> #Integer Indexing
>>> arr=np.array([[1,2],[3,4],[5,6]])
>>> print(arr[[0,1,2],[0,1,1]])
[1 4 6]
>>> arr=np.arrange(9)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    arr=np.arrange(9)
  File "C:\Users\jaiso\AppData\Local\Programs\Python\Python38-32\lib\site-packages\numpy\__init__.py", line 214, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'arrange'
>>> arr=np.arange(9)
>>> reshape_arr = arr.reshape(3,3)
>>> print(reshape_arr)
[[0 1 2]
 [3 4 5]
 [6 7 8]]
>>> arr= np.arange(8).reshape(2,4)
>>> print(arr.flat[4])
4
>>> arr = np.arange(8).reshape(2,4)
>>> print(arr.flatten())
[0 1 2 3 4 5 6 7]
>>> arr=np.arange(8).reshape(2,4)
>>> print(arr.transpose())
[[0 4]
 [1 5]
 [2 6]
 [3 7]]
>>> 