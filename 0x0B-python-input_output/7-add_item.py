#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import importlib


if __name__ == "__main__":
    save_to_json_file = importlib.import_module(
        '5-save_to_json_file').save_to_json_file
    load_from_json_file = importlib.import_module(
        '6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
