# Excercise 8-15
import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

# Just double-check that the unprinted_designs list is empty
print(f'Unprinted designs: {unprinted_designs}')