def describe_pet(animal_type, pet_name, color="brown"):
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}. Its color is {color}.")

describe_pet(animal_type='hamster', pet_name='harry')
