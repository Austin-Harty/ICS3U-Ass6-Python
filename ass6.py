#!/usr/bin/env python3

# Created by: Austin-Harty
# Created on: Dec 2019
# This program finds the area of a square


def square_calc(base, height):
    # This calculates area based on the base and height parameters
    # process
    area = (base * height)
    return area


def main():
    while True:
        try:
            # Input
            base = int(input("Input the base of your square: "))
            height = int(input("Input the height of your square: "))

            # Calls area function
            area = square_calc(base, height)

            # output
            print("The area of your square is " + str(area)
                  + " units squared.")
            break
        except Exception:
            print("Please input only proper numbers, try again")


if __name__ == "__main__":
    main()
