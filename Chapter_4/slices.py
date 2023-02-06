# Exercises 4-10 .. 4-12

# 4-10
games = ['dominion','carcassonne','codenames','wingspan','monopoly']

print(f'The first three items in the list are {games[0:3]}')
print(f'Three items from the middle of the list are {games[1:4]}')
print(f'The last three items in the list are {games[-3:]}')

# 4-11
friend_games = games[:]
games.append('stratego')
friend_games.append('darts')
print('My favourite games are:')
print(games)
#for game in games:
#    print(game)

print("My friend's favourite games are:")
print(friend_games)
#for game in friend_games:
#    print(game)
