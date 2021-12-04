# remove an item from a list by its name
super_cars = ["Ferrari SF90", "McLaren 720S", "Lamborghini", "Toyota Tundra"]
super_cars.remove("Toyota Tundra")
print(super_cars)


# what if i have duplicate item in list?
numbers = [10, 10, 11, 12, 13, 10]
numbers.remove(10)
print(numbers)  # [10, 11, 12, 13, 10]

# what happened ?? its only remove first found item


# what if no item in list ?
ps4_games = ["Horizon Zero Dawn", "Uncharted 4", "GTA V", "RDR 2"]
# if i do this
# ps4_games.remove("Age of Empires II") then it will show us the error result
# how to avoid it ??
try:
    ps4_games.remove("Age of empires II")
except ValueError:
    print("Item not present in the list")
