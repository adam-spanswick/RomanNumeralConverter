# Adam Spanswick
# This program takes a Roman numeral as a string and converts it to it's corresponding integer value.
from typing import Dict

romanNumeralVals: Dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class RomanNumeralLookup:

    @staticmethod
    def lookup(numeral):
        if numeral in romanNumeralVals:
            return romanNumeralVals.get(numeral)

    def convert(self, numeral):
        number: int = 0

        if len(numeral) == 1:
            number = self.lookup(numeral[0])
            return number

        for c in numeral:
            if numeral[-1] is not "I" and numeral[-2] is "I":
                number -= 1
                print("Here2: " + str(number))
            number += self.lookup(c)
            print("Here: " + str(number))

        return number


class Main:
    numLookup = RomanNumeralLookup()
    exitMsg = "exit"
    print("This program takes a Roman numeral as a string and converts it to it's corresponding integer value.\n"
          "Usage:\n"
          "      When prompted enter a roman numeral, capital or lower case. To exit program enter: exit\n"
          "Roman Numeral Values:\n"
          "      I = 1\n"
          "      V = 5\n"
          "      X = 10\n"
          "      L = 50\n"
          "      C = 100\n"
          "      D = 500\n"
          "      M = 1000\n")
    while True:
        romanNumeralToConvert = input("Input a Roman numeral: ")
        romanNumeralToConvert.upper()
        if romanNumeralToConvert.lower() == exitMsg:
            break

        individualNumerals = list(romanNumeralToConvert)

        for char in individualNumerals:
            if char in romanNumeralVals:
                continue
            else:
                print("Input is not a roman numeral, see usage and re-enter a roman numeral.")
                break
        print(numLookup.convert(individualNumerals))