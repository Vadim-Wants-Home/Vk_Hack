import json


def get_json_data(file):
    with open(file) as dbjson_file:
        data = json.loads("\n".join(dbjson_file.readlines()))
        return data