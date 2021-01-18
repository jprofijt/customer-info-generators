#!/usr/bin/env python

import random
import names
import generator_module.generate_phone_numbers as phone_generator
import generator_module.generate_iban as iban_generator


def get_list_order():
    return ['Gender', 'FirstName', 'LastName', 'Phone', 'e-mail', 'iban']


class Customer:
    def __init__(self):
        self.gender = random.choice(['male', 'female'])
        self.first_name = names.get_first_name(self.gender)
        self.last_name = names.get_last_name()
        self.mobile = phone_generator.generate_mobile_number()
        self.mail = "{0}.{1}@random-mail.com".format(self.first_name, self.last_name).lower()
        self.iban = iban_generator.get_random_iban()

    def __str__(self):
        return """
        Gender: {0}
        Name: {1} {2}
        phone: {3}
        e-mail: {4}
        iban: {5}
        """.format(self.gender, self.first_name, self.last_name, self.mobile, self.mail, self.iban)

    def get_customer_as_list(self):
        return [self.gender, self.first_name, self.last_name, self.mobile, self.mail, self.iban]


def main():
    random_customer = Customer()
    print(random_customer)


if __name__ == "__main__":
    main()
