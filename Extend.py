# List extend list
singers = ["Agnes Monica", "Ariel Noah", "Arman"]
new_singers = ["Rizal Armada", "Ivan Seventeen"]

singers.extend(new_singers)
print(singers)

# List extend set
fish = ["Salmon", "Clownfish", "Tuna"]
other_fish = {"Catfish", "Snapper", "Anchovy"}
fish.extend(other_fish)
print(fish)

# List extend Tuple
numbers = [11, 22, 33, 44]
hundreds_numbers = (121, 212, 232, 323)
numbers.extend(hundreds_numbers)
print(numbers)
