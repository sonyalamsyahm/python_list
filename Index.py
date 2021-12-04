# find index of item from list
# example

motorcycle_brands = ["Honda", "Suzuki", "Kawasaki", "BMW"]
index = motorcycle_brands.index("Kawasaki")
print(index)    # 2


# What if an item not in list ?
ps_games = ["Horizon Zero Dawn", "Downhill Domination", "GTA V"]
# if i looking for index of "Cities Skylines" it will return error because
# that not present in the list, so what should i do is:
try:
    ps_games.index("Cities Skylines")
except ValueError:
    print("Item isn't in the list")


# index of list inside list
world_chess_players = ["Magnus", ["Kasparov", "Anand"], "Bobby Fisher"]
index = world_chess_players.index(["Kasparov", "Anand"])
print(index)    # 1


# index of dict inside list
football_players = [{"name": "Virgil Van D", "position": "DF"}, {"name": "Mo. Salah", "position": "CF"}]
index = football_players.index({"name": "Mo. Salah", "position": "CF"})
print(index) # 1
