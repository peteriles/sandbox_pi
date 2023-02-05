# Exercise 3-8, 3-9, 3-10

# 3-8

list_locations = ['big island','tucson','toronto','bermuda','tahiti']
print("Original list:")
print(list_locations)

# Temporarily sort the list
print("Sorted list:")
print(sorted(list_locations))

# Print original list again
print('Original list:')
print(list_locations)

# Print list in reverse order
print('List in reverse order:')
list_locations.reverse()
print(list_locations)

# Print list in original order
print('List in original order:')
list_locations.reverse()
print(list_locations)

# Print list in alphabetical order (permanent change)
print('Sorted alphabetically, permanently:')
list_locations.sort()
print(list_locations)

# Print list in reverse-AB order (permanent change)
print('Sorted reverse-alphabetically')
list_locations.sort(reverse=True)
print(list_locations)

# 3-9
num_locations = len(list_locations)
print(f'There are {num_locations} locations in the list.')
print('\n')

# 3-10
list_rivers = ['amazon', 'st. lawrence', 'colorado', 'yukon', 'barron']
print(list_rivers)
print(f'The number of rivers in the list is {len(list_rivers)}')
print(f'The first river is {list_rivers[0].title()}.')
print(f'The last river is {list_rivers[-1].title()}')
new_river = 'ottawa'
list_rivers.append(new_river)
print(list_rivers)
del list_rivers[1]
print(list_rivers)
list_rivers.insert(2,'yoho')
print(list_rivers)
list_rivers.remove('barron')
print(list_rivers)
popped_river = list_rivers.pop()
print(f'The popped rover is {popped_river.title()}.')
print(list_rivers)
popped_river = list_rivers.pop(2)
print(f'The popped rover is {popped_river.title()}.')
print(list_rivers)
list_rivers.insert(0,'zagreb')
print(list_rivers)
print(sorted(list_rivers))
print(list_rivers)
list_rivers.sort()
print(list_rivers)
list_rivers.sort(reverse=True)
print(list_rivers)
list_rivers[1]='calvin'
print(list_rivers)
list_rivers.reverse()
print(list_rivers)