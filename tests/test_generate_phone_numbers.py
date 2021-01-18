#!/usr/bin/env python


import unittest
import re

from customer_info_generator.generator_module import generate_phone_numbers as generator


class TestGenerateMobileNumber(unittest.TestCase):

    def test_number_starts_with(self):
        mobile_number = generator.generate_mobile_number()
        pattern = re.compile(r'06[12345]\d+')
        self.assertTrue(pattern.match(mobile_number))
    
    def test_number_length(self):
        mobile_number = generator.generate_mobile_number()
        self.assertTrue(len(mobile_number) == 10) # length of 9 for number without '0' in front

 
if __name__ == "__main__":
    unittest.main()
