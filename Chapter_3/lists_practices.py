# 3-1
list_names = ['brian','mark','joe','john']
print(list_names[0])
print(list_names[1])
print(list_names[2])
print(list_names[3])

# 3-2
text_start = "Hi there, "
text_end   = "!"

for i in range(0,len(list_names)):
  print(f"Hi there, {list_names[i].title()}!")

# 3-3
list_transport = ['GT','bicycle','shoes', 'cross country skis']
print(f'I like to travel by {list_transport[0].upper()}')
print(f'I find using a {list_transport[1]} really slow.')
print(f'How about we take my {list_transport[2]} to school?')
print(f'Yo, my {list_transport[3]} just got smooshed.')