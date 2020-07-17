def order(number, *lists):
    print(f"\nNumber of dishes: {number}, the dishes are: ")
    for list in lists:
        print(f"- {list}")