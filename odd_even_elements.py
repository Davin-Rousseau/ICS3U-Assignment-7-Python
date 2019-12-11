#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on: December 2019
# This program uses arrays
# To display elements in odd positions

import math


def odd_elements(list_of_elements):
    # calculate surface area
    odd_element = []
    counter = 0
    # process
    for counter in range(len(list_of_elements)):
        if counter % 2 != 0:
            odd_element.append(list_of_elements[counter])

    # output
    return odd_element


def main():
    # This checks if input is an integer then
    # prints element in odd positions then
    # keeps going even if user inputs invalid info
    list_of_elements = []
    # Input
    input_1 = input("Enter number of elements you want in array: ")
    print("")
    # process
    while True:
        try:
            number_of_elements = int(input_1)
            for counter in range(0, number_of_elements):
                try:
                    input_2 = input("Enter element(numerical): ")
                    print("")
                    element_number = int(input_2)
                    list_of_elements.append(element_number)
                except ValueError:
                    # keep going
                    input_2 = input("Please try again: ")
                    continue
            get_odd_element = odd_elements(list_of_elements)
            break
        except ValueError:
            # keep going
            print("Invalid input.")
            input_1 = input("Please try again: ")
            continue
    print("The elements in odd positions are(in order):")
    print(get_odd_element)


if __name__ == "__main__":
    main()
