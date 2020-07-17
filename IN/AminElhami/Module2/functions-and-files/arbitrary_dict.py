def menu(itme, quan, **restaurant):
    restaurant['Item'] = itme
    restaurant['Quantity'] = quan
    return restaurant

restaurant = menu('soup', '1', Location='seattle', Zipcode = '98109')
print(restaurant)