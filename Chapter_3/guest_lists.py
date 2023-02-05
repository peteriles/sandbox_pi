# Exercises 3-4 .. 3-7

# Print invitation to each guest
def print_invites(list_guestList):

  for guest in list_guestList:
    print(f'{guest.title()}, you are cordially invited to dinner.')



#3-4 Guest list
list_guests = ['einstein','queen elizabeth','David Bowie','Trent Reznor']
print_invites(list_guests)
print('\n')

#3-5 Changing guest list
print(f"Unfortunately, {list_guests[2].title()} can't make it tonight")
print('\n')
new_guest = 'Kevin Costner'
del list_guests[2]
list_guests.insert(2,new_guest)
print_invites(list_guests)
print('\n')

# 3-6 More guests
print('We found a bigger table!')
new_guest = 'Dave Dooby'
list_guests.insert(0,new_guest)
new_guest = 'Katherine Jimmy'
list_guests.insert(2,new_guest)
new_guest = 'Gord jackie'
list_guests.append(new_guest)

print_invites(list_guests)
print('\n')

# 3-7 Shrinking guest list
print("The new table didn't arrive! I can only host 2 people..")

max_num_invites = 2
while 1:
  list_length = len(list_guests)
  print(f'There are currently {list_length} guests on the list.')
  if list_length > max_num_invites:
    removed_guest = list_guests.pop()
    message = f'Sorry, {removed_guest.title()}, you cannot come any more.'
    print(message)
  else:
    print('We have the right number of guests, now.')
    break

print_invites(list_guests)

for i in range(0,len(list_guests)):
  del list_guests[0]

print(list_guests)