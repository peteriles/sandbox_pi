# Function in support of Exercise 8-16
def print_sandwich_items(*items):
    """Print arbitrary number of items on a sandwich"""
    print(f'Tuple of items is: {items}')
    
    print('Individual items are:')
    for item in items:
        print(f'    {item}')