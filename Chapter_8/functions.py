# Exercises 8-1 .. 8-5

# Stuff from the text
def greet_user():
    """ Display a simple greeting."""
    print("hey there!")

greet_user()
print('\n')


# Exercise 8-1
print("Exercise 8-1")

def display_message():
    """Prints a message about what I'm learning"""
    print("I am learning about functions.")

display_message()
print('\n')


# Exercise 8-2
print("Exercise 8-2")

def favourite_book(title):
    print(f'I love the book {title}!')

favourite_book('Lord of the Rings')
favourite_book('1984')
print('\n')

# Exercises 8-3 and 8-4
print("Exercise 8-3 and 8-4")
def make_shirt(shirt_size = 'large', shirt_message = 'I love Python'):
    """Makes a shirt with a specified size and message on it"""
    print(f'The shirt size is {shirt_size}.')
    print(f'The message is: {shirt_message}.\n')

# Call make_shirt w/ diff types of arguments
make_shirt('medium', 'I love potatoes')
make_shirt(shirt_size='small', shirt_message='Do you hear me?')
make_shirt(shirt_message='This is weird', shirt_size='large')

# Make a large shirt w/ default message
make_shirt()

# Make a medium shirt w/ default message (two ways)
make_shirt('medium')
make_shirt(shirt_size='medium')

# Make a shirt of any size w/ a diff message
make_shirt('small', 'hey ho there')
print('\n')

# Exercise 8-5
print('Exercise 8-5')
def describe_city(name, country='Canada'):
    """Prints a message describing a city with a given name and country"""
    print(f'{name.title()} is in {country.title()}.\n')

describe_city('ottawa')
describe_city('boston','usa')
describe_city(country="Finland", name="Helsinki")
print('\n')

# Exercise 8-6
print('Exercise 8-6')

def city_country(city, country):
    return f'{city.title()}, {country.title()}'

string_1 = city_country('Sault Ste. Marie', 'Canada')
string_2 = city_country('Toronto', 'canada')
string_3 = city_country('Miami', 'USA')

print(string_1)
print(string_2)
print(string_3)

print('\n')


# Exercises 8-7 and 8-8
print('Exercise 8-7')

def make_album(artist_name, album_title, number_of_songs=''):
    """Builds a dictionary describing a music album"""

    return_dict = {
        'artist' : artist_name,
        'album' : album_title,
        }

    if number_of_songs:
        return_dict['num_songs'] = number_of_songs

    return return_dict

album_1 = make_album('Prince', 'Purple Rain')
album_2 = make_album('Gwar', 'Ragnarok')
album_3 = make_album('KMFDM', 'Nihil')
album_4 = make_album('Geezers', 'This is the life', 12)
print(album_1)
print(album_2)
print(album_3)
print(album_4)

while True:
    name = input("Please enter the artist's name ('q' to quit): ")

    if name == 'q':
        break

    album_title = input("Please enter the album title ('q' to quit): ")

    if album_title == 'q':
        break

    album = make_album(name, album_title)
    print(album)
