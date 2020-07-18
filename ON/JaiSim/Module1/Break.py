Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("For-Break")
For-Break
>>> for letter == 'h':
	
SyntaxError: invalid syntax
>>> for letter in 'Python':
	if letter == 'h':
		break
	print('Current Letter :', letter)
	print("\nWhile-Break")
	var=10
	while var > 0:
		print ('Current variable value : ' , var)
		var=var - 1
		if var ==5:
			break
		print("Good bye")

		
Current Letter : P

While-Break
Current variable value :  10
Good bye
Current variable value :  9
Good bye
Current variable value :  8
Good bye
Current variable value :  7
Good bye
Current variable value :  6
Current Letter : y

While-Break
Current variable value :  10
Good bye
Current variable value :  9
Good bye
Current variable value :  8
Good bye
Current variable value :  7
Good bye
Current variable value :  6
Current Letter : t

While-Break
Current variable value :  10
Good bye
Current variable value :  9
Good bye
Current variable value :  8
Good bye
Current variable value :  7
Good bye
Current variable value :  6
>>> 