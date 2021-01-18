#!/usr/bin/env python
"""Python script to generate a IBAN number. Only dutch accounts for now."""

import random
import customer_info_generator.generator_module.generic_functions as gen


def generate_bank_number():
    """Generates a random number which is 10 character long.

    gets a random number between 1 and 999999999, then adds zero's in front to keep a length of 10.
    """
    return gen.generate_random_number_as_specified(10)


def calculate_control_number(land_code, bank_code, bank_number):
    """Calculates the control number as specified for dutch the dutch IBAN 

    Keyword arguments:
    land_code -- the land code for the generated IBAN. Is 2 characters long.
    bank_code -- the bank code for the generated IBAN. Is 4 characters long.
    bank_number -- the bank account number used in the IBAN. Is 10 characters long.
    """

    control_string = convert_letter_combination(bank_code) + bank_number + convert_letter_combination(land_code) + "00"

    control_number = int(control_string)

    result = 98 - (control_number % 97)

    return result


def get_alphabet_position(letter):
    """gets the letter position in the latin alphabet

    Keyword arguments:
    letter -- the letter to use.
    """

    if len(letter) > 1:
        raise ValueError("input value {0} is not a single character".format(letter))

    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

    return alphabet.index(letter.upper()) + 1


def convert_letter(letter):
    """converts the letter to a number.

    Position in the latin alphabet + 9

    Keyword arguments:
    letter -- the letter to convert.
    """
    position = get_alphabet_position(letter)

    return str(position + 9)


def convert_letter_combination(string):
    """converts a string of characters to the converted letters.

    Keyword arguments:
    string -- the string of characters to convert to numbers.
    """

    combined_string = ""
    for letter in string:
        combined_string = combined_string + convert_letter(letter.upper())

    return combined_string


def construct_iban(land_code, bank_code, bank_number):
    """Constructs the random IBAN from the components.

    Keyword arguments:
    land_code -- the land code for the generated IBAN. Is 2 characters long.
    bank_code -- the bank code for the generated IBAN. Is 4 characters long.
    bank_number -- the bank account numbe used in the IBAN. Is 10 characters long.
    """
    control_number = str(calculate_control_number(land_code, bank_code, bank_number))

    return land_code + control_number + bank_code + bank_number


def get_land_code(default=None):
    """gets a random land code if default is not filled.

    Keyword arguments:
    default -- if filled is used instead of random.
    """
    land_code_list = ["NL"]  # TODO: add more land codes

    if default is None:
        return random.choice(land_code_list)

    return default


def get_bank_code(default=None):
    """gets a random dutch bank code if default is not filled.

    Keyword arguments:
    default -- if filled is used instead of random.
    """
    bank_code_list = ["ABNA", "AEGO", "AKBK", "ANDL", "AOLB",
                      "ARBN", "ARSN", "ARTE", "ASRB", "ATBA",
                      "BBRU", "BCIT", "BGCC", "BKMG", "BNGH",
                      "BNPA", "BOFA", "BOFS", "BOTK", "BOUW",
                      "CITC", "CITI", "COBA", "DEUT", "DEUT",
                      "DHBN", "DLBK", "DNIB", "DSSB", "FBHL",
                      "FLOR", "FRBK", "FRGH", "FTSB", "FVLB",
                      "GILL", "HAND", "HSBC", "INGB", "INKB",
                      "INSI", "ISBK", "KABA", "KASA", "KNAB",
                      "KOEX", "KRED", "LOCY", "LOYD", "LPLN",
                      "MHCB", "NWAB", "RABO", "RBOS", "RBRB",
                      "RGRB", "SNSB", "SOGE", "STAL", "TEBU",
                      "TRIO", "UBSW", "UGBI", "VOWA", "VPVG"]

    if default is None:
        return random.choice(bank_code_list)

    return default


def get_random_iban():
    land_code = get_land_code("NL")
    bank_code = get_bank_code()
    bank_number = generate_bank_number()

    iban = construct_iban(land_code, bank_code, bank_number)
    return iban


def main():
    print(get_random_iban())


if __name__ == "__main__":
    main()
