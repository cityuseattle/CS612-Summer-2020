def menu(item, quan, **restaurant):
    restaurant["item"] = item
    restaurant["Quantity"] = quan
    return restaurant
restaurant = menu("soup", "1", Location="Seattle", Zipcode="98109")
print(restaurant)