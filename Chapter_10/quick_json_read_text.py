# Part of Exercise 10-11
from pathlib import Path
import json

file_object_instance = Path('json_data.txt')
fave_number = file_object_instance.read_text();

print("I know your favourite number, it's: ", fave_number)