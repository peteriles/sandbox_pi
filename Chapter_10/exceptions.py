# Exercises 10-6 ..

# Exercise 10-6 and 10-7
print ("Exercise 10-6 and 10-7")

print('This is a program to add two numbers.')
active_flag = True

while active_flag == True:
    number_1 = input("Please enter the first integer:  ")
    number_2 = input("Please enter the second integer: ")

    try:
        number_1 = int(number_1)
        number_2 = int(number_2 )
    except ValueError:
        print('Either or both entries were not an integer. Try again')
    else:
        total = number_1 + number_2
        print("The total is: ", total)
        active_flag = False


print("The program is complete.")
print('\n')


# Exercise 10-7
print ("Exercise 10-7")
