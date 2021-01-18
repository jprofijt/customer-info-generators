#!/usr/bin/env python

"""file to store generic functions"""

import random
import math


def generate_random_number_as_specified(length):
    """Generates a random number which is the desired length.

    gets a random number between 1 and (10^length - 1), then adds zero's in front to keep the specified lenght.
    """

    if length <= 0:
        raise ValueError("Input variable 'length' is zero or negative")

    max_number = int(math.pow(10, length)) - 1

    random.seed()
    number = random.randint(1, max_number)

    number_string = str(number)

    number_string = "0" * (length - len(number_string)) + number_string

    return number_string
