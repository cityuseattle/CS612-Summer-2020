Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def first(n):
	return n[0]
	def sort_list_first(tuples):
		return sorted (tuples, key=first)
	print(sort_list_first([(5,2),(2,1),(4,4),(3,2),(1,2)]))

	
>>> 