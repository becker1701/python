import roman1
import unittest, re

class KnownValues(unittest.TestCase):

    known_values = ( (1, 'I'),
                     (2, 'II'),
                     (3, 'III'),
                     (4, 'IV'),
                     (5, 'V'),
                     (6, 'VI'),
                     (7, 'VII'),
                     (8, 'VIII'),
                     (9, 'IX'),
                     (10, 'X'),
                     (50, 'L'),
                     (100, 'C'),
                     (500, 'D'),
                     (1000, 'M'),
                     (31, 'XXXI'),
                     (148, 'CXLVIII'),
                     (294, 'CCXCIV'),
                     (312, 'CCCXII'),
                     (421, 'CDXXI'),
                     (528, 'DXXVIII'),
                     (621, 'DCXXI'),
                     (782, 'DCCLXXXII'),
                     (870, 'DCCCLXX'),
                     (941, 'CMXLI'),
                     (1043, 'MXLIII'),
                     (1110, 'MCX'),
                     (1226, 'MCCXXVI'),
                     (1301, 'MCCCI'),
                     (1485, 'MCDLXXXV'),
                     (1509, 'MDIX'),
                     (1607, 'MDCVII'),
                     (1754, 'MDCCLIV'),
                     (1832, 'MDCCCXXXII'),
                     (1993, 'MCMXCIII'),
                     (2074, 'MMLXXIV'),
                     (2152, 'MMCLII'),
                     (2212, 'MMCCXII'),
                     (2343, 'MMCCCXLIII'),
                     (2499, 'MMCDXCIX'),
                     (2574, 'MMDLXXIV'),
                     (2646, 'MMDCXLVI'),
                     (2723, 'MMDCCXXIII'),
                     (2892, 'MMDCCCXCII'),
                     (2975, 'MMCMLXXV'),
                     (3051, 'MMMLI'),
                     (3185, 'MMMCLXXXV'),
                     (3250, 'MMMCCL'),
                     (3313, 'MMMCCCXIII'),
                     (3408, 'MMMCDVIII'),
                     (3501, 'MMMDI'),
                     (3610, 'MMMDCX'),
                     (3743, 'MMMDCCXLIII'),
                     (3844, 'MMMDCCCXLIV'),
                     (3888, 'MMMDCCCLXXXVIII'),
                     (3940, 'MMMCMXL'),
                     (3999, 'MMMCMXCIX'))  


    def test_to_roman_known_values(self):
        '''to_roman should return valid numeral with a valid input'''
        for number, numeral in self.known_values:
            result = roman1.to_roman(number)
            self.assertEqual(numeral, result)

    def test_to_number_known_values(self):
        '''to_nmber should return an integer based on valid roman numeral input'''
        for number, numeral in self.known_values:
            result = roman1.from_roman(numeral)
            self.assertEqual(number, result)

    def test_round_trip(self):
        '''should return valid roman numeral from integer, and then back to integer'''
        # for number, numeral in self.known_values:
        for integer in range(1, 4000):
            roman = roman1.to_roman(integer)
            round_trip_number = roman1.from_roman(roman)
            self.assertEqual(integer, round_trip_number)


class FromRomanInput(unittest.TestCase):
    '''Test good input to from_roman method'''

    def test_from_roman_known_values(self):
        '''should pass with valid roman numerals'''
        for num, roman in KnownValues.known_values:
            result = re.search(roman1.roman_rules, roman, re.VERBOSE)
            self.assertTrue(result)
    

class FromRomanBadInput(unittest.TestCase):
    '''test bad input to from_roman'''

    def test_from_roman_too_many_characters(self):
        '''should fail if roman numeral length is < 1 or > 15.
        Longest roman numeral = MMMDCCCLXXXVIII = 3888'''
        test_rn = 'MMMDCCCLXXXVIIII'
        self.assertRaises(roman1.InvalidRomanNumeralError, roman1.from_roman, test_rn)


    def test_from_roman_too_many_repeating_chars(self):
        '''should fail if roman numeral has too many repeating charaters'''
        test_list = ['IIII','XXXXI','DDCCLXXXII','DCCCCLXX','MMCCCXLLIII','MMMDCCCLXXXXVIII']

        for bad_rn in test_list:
            self.assertRaises(roman1.InvalidRomanNumeralError, roman1.from_roman, bad_rn)


    def test_from_roman_repeating_characters(self):
        '''should fail if non repeating charaters are present in roman numereal input'''
        test_list = ['IVIV', 'XLXL', 'XCXC', 'VV', 'LL', 'DD', 'DCDC']

        for bad_rn in test_list:
            self.assertRaises(roman1.InvalidRomanNumeralError, roman1.from_roman, bad_rn)


    def test_from_roman_charaters_out_of_order(self):
        '''should fail if roman numerals are out of order'''
        test_list = ['IIIV','XIXX','DCDXXI','MXILII','MCLDXXXV','LMMXCIII','MMXCCII','MMIVDLXX','MMMCXDVIII']

        for bad_rn in test_list:
            self.assertRaises(roman1.InvalidRomanNumeralError, roman1.from_roman, bad_rn)

    def test_from_roman_bad_characters(self):
        self.assertRaises(roman1.InvalidRomanNumeralError, roman1.from_roman, "asdxc")


class ToRomanBadInput(unittest.TestCase):

    def test_to_roman_too_large(self):
        '''to_roman should fail if the number is too large > 3999'''
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 4000)

    def test_to_roman_lt_0(self):
        '''to_roman should fail if the number is less than 0'''
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, -1)

    def test_to_roman_eq_0(self):
        '''to_roman should fail if the number is less than 0'''
        self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 0)

    def test_to_roman_not_an_integer(self):
        '''should fail if number is not an integer'''
        self.assertRaises(roman1.NoIntegerError, roman1.to_roman, 0.5)
        self.assertRaises(roman1.NoIntegerError, roman1.to_roman, 1.0)





if __name__ == "__main__":
    unittest.main()