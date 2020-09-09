def menu(item, quan, **restaurant):
    restaurant['item'] = item
    restaurant['quantity'] = quan
    return restaurant

restaurant = menu('soup', 1, location = 'seattle', zipcode = '98109')
print(restaurant)