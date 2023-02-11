# Exercise 5-11

# Create a list of integrers from 1 to 9
numbers = list(range(1,10))
#numbers = list(range(1,20))
print(numbers)

for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    elif number < 10:
        print(f'{number}th')
    else:
        print('Number is out of range!')