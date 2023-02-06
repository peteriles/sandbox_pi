# Exercises 4-1 .. 4-9

# 4-1
pizzas = ['hawaiian','combination','pepperoni','plain' ]

for pizza in pizzas:
    print(f'Pizza name is: {pizza}.')

print("I love pizza!")

# 4-2
animals = ['dog','cat','mouse','deer']

for animal in animals:
    print(f'I just saw a {animal} today!')

print('All of these animals have legs.')
print('\n')

# 4-3
for number in range(1,21):
    print(number)

# 4-4
#for number in range(1,1_000_001):
#    print(number)

# 4-5
numbers = []
for number in range(1,1_000_001):
    numbers.append(number)

min_number = min(numbers)
print(f'Min number is {min_number}')
max_number = max(numbers)
print(f'Max number is {max_number}')
numbers_sum = sum(numbers)
print(f'Sum is {numbers_sum}')

# 4-6
odd_numbers = range(1,21,2)
for odd_number in odd_numbers:
    print(odd_number)

# 4-7 
mults_of_3_numbers = range(3,31,3)
for mults_of_3_number in mults_of_3_numbers:
    print(mults_of_3_number)

# 4-8
print('First 10 cubes')
cubes = []
for number in range(1,11):
    cubes.append(number**3)
    print(cubes[number-1])

# 4-9
print('List of cubes')
cubes = [number**3 for number in range(1,11)]
print(cubes)
