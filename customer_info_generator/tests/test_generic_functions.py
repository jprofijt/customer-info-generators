#!/usr/bin/env python

import unittest

from customer_info_generator.generator_module import generic_functions as functions


class TestGenericFunctions(unittest.TestCase):
    def test_random_number_lenght(self):
        self.assertEqual(len(functions.generate_random_number_as_specified(10)), 10)

    def test_throw_error_at_zero(self):
        try:
            functions.generate_random_number_as_specified(0)
        except ValueError:
            pass
        except Exception:
            self.fail('Unexpected exception raised')
        else:
            self.fail("Exception 'ValueError' not raised")

    def test_throw_error_at_negative(self):
        try:
            functions.generate_random_number_as_specified(-1)
        except ValueError:
            pass
        except Exception:
            self.fail('Unexpected exception raised')
        else:
            self.fail("Exception 'ValueError' not raised")




if __name__ == "__main__": 
    unittest.main(exit=False)
