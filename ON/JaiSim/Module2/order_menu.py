Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import Order_Module
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import Order_Module
ModuleNotFoundError: No module named 'Order_Module'
>>> Order_Module.order(1,"Pizza")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    Order_Module.order(1,"Pizza")
NameError: name 'Order_Module' is not defined
>>> order_module.order(3,"Soup","Pasta","Pizza")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    order_module.order(3,"Soup","Pasta","Pizza")
NameError: name 'order_module' is not defined
>>> 