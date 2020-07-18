Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> original = [8,20,-10,0,55,-777]
>>> for i in range(len(original)):
	if original[i]<0:
		original[i]=abs(original[i])
		print (original)

		
[8, 20, 10, 0, 55, -777]
[8, 20, 10, 0, 55, 777]
>>> 