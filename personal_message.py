name = "Peter Iles"
message = f"Hello {name}, how are you today?"
print(message)

print(name.lower())
print(name.upper())
print(name.title())

print("Bruce Campbell once said 'This is my boomstick.'")
famous_person = "Bruce Campbell"
message = f"{famous_person} once said 'This is my boomstick.'"
print(message)

famous_person2 = "\tDave Doobs\n"
print(famous_person2)
print(famous_person2.rstrip())
print(famous_person2.lstrip())
print(famous_person2.strip())

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))