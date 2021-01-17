#!/usr/bin/env python

"""Python script to generate mobile phone number."""

# TODO: land line phone numbers.
import random
import customer_info_generator.generator_module.generic_functions as gen


def generate_mobile_number():
    """Generates a random number which is 10 character long in total.

    Number format: 06CBBBBBBB
    C: has to be between 1 - 5.
    B: Random number
    
    """

    random_number = gen.generate_random_number_as_specified(7)
    random_pre_number = str(random.randint(1, 5))

    return "06" + random_pre_number + random_number


def main():
    print(generate_mobile_number())


if __name__ == "__main__":
    main()
