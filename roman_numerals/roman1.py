import re

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

roman_rules = '''
    ^                   # start of string
    M{0,3}              # 1000's: 0 - 3 instances
    (CM|CD|D?C{0,3})    # CM = 900, 0 to 1
                        # CD = 400, 0 to 1
                        # D (0 to 1) and C (0 to 3)
    (XC|XL|L?X{0,3})    # XC = 90, 0 to 1
                        # XL = 40, 0 to 1
                        # L (0 to 1) and X (0 to 3)
    (IX|IV|V?I{0,3})    # IX = 9, 0 to 1
                        # IV = 4 0 to 1
                        # V (0 to 1) and I (0 to 3)
    $                   # end of string
    '''


class OutOfRangeError(ValueError): pass
class NoIntegerError(ValueError): pass
class InvalidRomanNumeralError(ValueError): pass


def to_roman(number):
    '''Convert an integer to a roman numeral; returns string'''

    result = ''

    if not (0 < number < 4000):
        raise OutOfRangeError("number out of range (Must be between 1 to 3999).")

    elif not isinstance(number, int):
        raise NoIntegerError("number must be an integer value")


    for numeral, integer in roman_numeral_map:
        
        while number >= integer:
            result += numeral
            number -= integer

    return result


def from_roman(roman):
    '''Converts a roman nmeral to an integer; returns integer'''

    result = re.search(roman_rules, roman, re.VERBOSE)

    if result == None:
        raise InvalidRomanNumeralError('The Roman Numeral passed is not valid.')

    else:
        result = []
        counter = 0
        for numeral, integer in roman_numeral_map:
            while numeral == roman[counter:counter + len(numeral)]:
                result.append(integer)
                counter += len(numeral)
        
        return sum(result)


def run():
    repeat = True

    while repeat == True:
        choice = input("R to convert to roman, I to convert to number, X to exit: ").upper()

        if choice == 'R':
            num = int(input("Enter a number form 1 to 3999: "))
            print(to_roman(num))

        elif choice == 'I':
            rn = input("Enter a roman numeral to convert: ")
            print(from_roman(rn))
        elif choice == 'X':
            repeat = False
        else:
            print("That options was not recognized")

    print("Thanks!")


