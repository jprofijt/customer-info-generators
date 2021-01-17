#!/usr/bin/env python

"""file to store generic functions"""

import random, math

def generate_random_number_as_specified(lenght):
    """Generates a random number which is the desired lenght.

    gets a random number between 1 and (10^lenght - 1), then adds zero's in front to keep the specified lenght.
    """

    if (lenght <= 0):
        raise ValueError("Input variable 'lenght' is zero or negative")
    
    max_number = math.pow(10, lenght) - 1

    random.seed()
    number = random.randint(1, max_number)

    number_string = str(number)

    number_string = "0" * (lenght - len(number_string)) + number_string

    return number_string