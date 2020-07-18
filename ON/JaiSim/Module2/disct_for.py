Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> alien_0 = {'color': 'green', 'points': 5}
>>> alien_1 = {'color': 'yellow','points':10}
>>> aliens = [alien_0,alien_1]
>>> #accessing key, value
>>> for i in aliens:
	for key, value in i.items():
		print("KEY : " , "\t" , "VALUE: " , value)

		
KEY :  	 VALUE:  green
KEY :  	 VALUE:  5
KEY :  	 VALUE:  yellow
KEY :  	 VALUE:  10
>>> 