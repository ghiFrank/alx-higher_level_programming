#!/usr/bin/python3
"""load_from_json_file module"""


if __name__ == "__main__":
    import sys
    from 5-save_to_json_file import save_to_json_file
    from 6-load_from_json_file import load_from_json_file
    
    items = load_from_json_file("add_item.json")

    # Add arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, "add_item.json")
