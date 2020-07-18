Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def menu(item,quan,**restaurant):
	restaurant['Item']=item
	restaurant['Quantity'] = quan
	return restaurant

>>> restaurant = menu('soup','1',Location='seattle',Zipcode='98109')
>>> print(restaurant)
{'Location': 'seattle', 'Zipcode': '98109', 'Item': 'soup', 'Quantity': '1'}
>>> 