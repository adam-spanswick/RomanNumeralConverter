# Adam Spanswick
# This program takes a Roman numeral as a string and converts it to it's corresponding integer value.
from typing import Dict
from tkinter import *
from PIL import Image, ImageTk

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
            number += self.lookup(c)

        if numeral[-1] is not "I" and numeral[-2] is "I":
            number -= 1

        return number


window = Tk()
window.geometry("400x400")
window.title("Roman Numeral Converter")
window.configure(background='gray')
numeral = StringVar()
integervalue = StringVar()

def get_numeral():
    global inputNumeral
    romanNumeralToConvert = inputNumeral.get()
    exitMsg = "exit"

    while True:
        if romanNumeralToConvert.lower() == exitMsg:
            break

        individualNumerals = list(romanNumeralToConvert)
        individualNumerals = [element.upper() for element in individualNumerals]
        print(individualNumerals)

        for char in individualNumerals:
            if char in romanNumeralVals:
                continue
            else:
                print("Input is not a roman numeral, see usage and re-enter a roman numeral.")
                break
        integerval = numLookup.convert(individualNumerals)
        print(integerval)
        break


numLookup = RomanNumeralLookup()

L1 = Label(window, text="Roman Numeral: ")
L1.configure(background='gray')
L2 = Label(window, text="Integer Value: ")
L2.configure(background='gray')
inputNumeral = Entry(window, bd=5, bg="white", textvariable=numeral, relief=FLAT)
inputNumeral.configure(background='white')
inputNumeral.focus_set()
getText = Button(window, text="Submit", relief=FLAT, command=get_numeral)
integerVal = Label(window, bg="gray", text=integervalue)
img = ImageTk.PhotoImage(Image.open("romanNumerals.png"))
pic = Label(window, image=img)

L1.grid(row=0, column=0, pady=(15,15))
inputNumeral.grid(row=0, column=1, pady=(15,15))
L2.grid(row=2, column=0, pady=(15,15))
integerVal.grid(row=2, column=1, pady=(15,15))
pic.grid(row=6, column=1, pady=(15,15))
getText.grid(row=4, column=1, pady=(15,15))

window.mainloop()

# numLookup = RomanNumeralLookup()
# exitMsg = "exit"
# print("This program takes a Roman numeral as a string and converts it to it's corresponding integer value.\n"
#       "Usage:\n"
#       "      When prompted enter a roman numeral, capital or lower case. To exit program enter: exit\n"
#       "Roman Numeral Values:\n"
#       "      I = 1\n"
#       "      V = 5\n"
#       "      X = 10\n"
#       "      L = 50\n"
#       "      C = 100\n"
#       "      D = 500\n"
#       "      M = 1000\n")
# while True:
#     romanNumeralToConvert = input("Input a Roman numeral: ")
#     if romanNumeralToConvert.lower() == exitMsg:
#         break
#
#     individualNumerals = list(romanNumeralToConvert)
#     individualNumerals = [element.upper() for element in individualNumerals]
#     print(individualNumerals)
#
#     for char in individualNumerals:
#         if char in romanNumeralVals:
#             continue
#         else:
#             print("Input is not a roman numeral, see usage and re-enter a roman numeral.")
#             break
#     print(numLookup.convert(individualNumerals))
