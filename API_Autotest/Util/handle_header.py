import os
import json

from Util.handle_json import read_json

base_path = os.path.dirname(os.getcwd())


def get_header():
    data = read_json("/Config/header.json")
    return data

print(get_header())