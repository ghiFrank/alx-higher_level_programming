#!/usr/bin/python3
"""task 7 module"""



import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

items = load_from_json_file("add_item.json")

items.extend(sys.argv[1:])

save_to_json_file(items, "add_item.json")
