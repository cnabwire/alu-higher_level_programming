#!/usr/bin/python3
"""8-class_to_json.py
"""


def class_to_json(obj):
    """ retuns the dictionary description with simple data structure """

    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    return {}
