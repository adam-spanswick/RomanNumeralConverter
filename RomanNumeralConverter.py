# Adam Spanswick
# This program takes a Roman numeral as a string and converts it to it's corresponding integer value.
from typing import Dict
from tkinter import *
from PIL import Image, ImageTk

roman_numeral_values: Dict[str, int] = {
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
    def lookup(roman_numeral):
        if roman_numeral in roman_numeral_values:
            return roman_numeral_values.get(roman_numeral)

    def convert(self, roman_numeral):
        integer_number: int = 0

        if len(roman_numeral) == 1:
            integer_number = self.lookup(roman_numeral[0])
            return integer_number

        for c in roman_numeral:
            integer_number += self.lookup(c)

        if roman_numeral[-2] == 'I' and roman_numeral[-1] != 'I':
            integer_number -= 2

        return integer_number


window: Tk = Tk()
window.geometry("400x450")
window.title("Roman Numeral Converter")
window.configure(background='dark olive green')
numeral = StringVar()
integer_value = StringVar()


def get_numeral():
    global input_numeral, integer_val
    roman_numeral_to_convert = input_numeral.get()
    exit_message = "exit"

    while True:
        if roman_numeral_to_convert.lower() == exit_message:
            break

        individual_numerals = list(roman_numeral_to_convert)
        individual_numerals = [element.upper() for element in individual_numerals]

        if len(individual_numerals) == 0:
            integer_val = 0
            return

        for char in individual_numerals:
            if char in roman_numeral_values:
                continue
            else:
                print("Input is not a roman numeral, see usage and re-enter a roman numeral.")
                break
        integer_val = number_lookup.convert(individual_numerals)
        break
    font = ('times', 12, 'bold')
    L4 = Label(window, background="dark olive green", text=integer_val, font=font)
    L4.grid(row=2, column=1, pady=(15, 15))
    return integer_val


def show_usage():
    popup = Toplevel(window)
    popup.configure(background='dark olive green')
    popup.title("Usage")
    usage_message = ("This program takes a Roman numeral as a string and converts it to it's corresponding "
                     "integer value.\n"
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
    # print(usage_message)
    L3 = Label(popup, background="dark olive green", text=usage_message)
    L3.grid(row=2, column=1, pady=(15, 15))


number_lookup = RomanNumeralLookup()

L1 = Label(window, text="Roman Numeral: ")
L1.configure(background='dark olive green')
L2 = Label(window, text="Integer Value: ")
L2.configure(background='dark olive green')
input_numeral = Entry(window, bd=5, bg="white", textvariable=numeral, relief=FLAT)
input_numeral.configure(background='white')
input_numeral.focus_set()
get_text = Button(window, text="Submit", relief=FLAT, command=get_numeral)
show_usage = Button(window, text="Usage", relief=FLAT, command=show_usage)
# integer_label = Label(window, bg="dark olive green", text=display_integer)
img = ImageTk.PhotoImage(Image.open("romanNumerals.png"))
pic = Label(window, image=img)

L1.grid(row=0, column=0, pady=(15, 15))
input_numeral.grid(row=0, column=1, pady=(15, 15))
L2.grid(row=2, column=0, pady=(15, 15))
# integer_label.grid(row=2, column=1, pady=(15, 15))
pic.grid(row=6, column=1, pady=(15, 15))
get_text.grid(row=3, column=1, pady=(15, 15))
show_usage.grid(row=4, column=1, pady=(15, 15))

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
