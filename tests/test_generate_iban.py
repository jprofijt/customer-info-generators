import unittest

import customer_info_generator.generator_module.generate_iban as generator


class TestIbanFormat(unittest.TestCase):
    def test_control_number(self):
        self.assertEqual(generator.calculate_control_number('NL', 'INGB', '9082037890'), 41)

    def test_formatting(self):
        self.assertRegex(generator.get_random_iban(), r'[A-Z]{2}\d{2}[A-Z]{4}\d{10}')


if __name__ == '__main__':
    unittest.main()
