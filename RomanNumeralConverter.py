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


class Main:
    root = Tk()

    top = Frame(root)
    top.pack(side=LEFT)

    bottom = Frame(root)
    bottom.pack(side=BOTTOM)

    line1 = Frame(top)
    line1.pack()

    line2 = Frame(top)
    line2.pack()

    numeralChart = Frame(root)
    numeralChart.pack(side=RIGHT)

    img = Image.open("romanNumerals.jpg")
    render = ImageTk.PhotoImage(img)
    imgLabel = Label(numeralChart, image=render)
    imgLabel.pack()

    root.title("Roman Numeral to Integer Converter")
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = screenwidth/3.8
    y = screenheight/2.5
    root.geometry(str(int(x)) + "x" + str(int(y)))

    romanNumeralLabel = Label(line1, text="Enter a Roman Numeral:")
    romanNumeralLabel.pack(pady=15, side=TOP)
    romanNumeralIN = Entry(line1)
    romanNumeralIN.focus_set()
    romanNumeralIN.pack(pady=15, side=TOP)

    intLabel = Label(line2, text="Integer Value:")
    intLabel.pack(pady=15, side=TOP)
    IntOut = Entry(line2, text="Integer Value")
    IntOut.pack(pady=15, side=TOP)

    submitButton = Button(bottom, text="Submit", padx=15, command=getText)
    submitButton.pack(padx=5, pady=5)

    def getText(self):
        inputtxt = self.romanNumeralIN.get()
        return inputtxt

    root.mainloop()

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
        print(getText())
        if romanNumeralToConvert.lower() == exitMsg:
            break

        individualNumerals = list(romanNumeralToConvert.capitalize())

        for char in individualNumerals:
            if char in romanNumeralVals:
                continue
            else:
                print("Input is not a roman numeral, see usage and re-enter a roman numeral.")
                break
        print(numLookup.convert(individualNumerals))