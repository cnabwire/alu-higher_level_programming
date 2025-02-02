#!/usr/bin/python3


"""This module defines a `MyList` class that inherits from the built-in `list`.

The `MyList` class provides a `print_sorted` method that prints a sorted copy
without modifying the original list.

Additionally, it overrides the `__str__` method to provide a string repre..
"""


class MyList(list):
    """
    A class that inherits from the `list` class.
    """

    def print_sorted(self):
        """Prints a sorted copy of the list without modifying the org. list."""
        sorted_list = sorted(self)
        print(sorted_list)
