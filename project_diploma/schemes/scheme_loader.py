import json
import os


def load_scheme(filename: str):
    schema_path = os.path.join((os.path.dirname((os.path.abspath(__file__)))), filename)

    with open(schema_path) as file:
        scheme = json.load(file)
        return scheme
