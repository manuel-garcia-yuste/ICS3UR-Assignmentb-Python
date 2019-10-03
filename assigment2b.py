#!/usr/bin/env python3

# Created by: Manuel Garcia
# Created on: September 2019
# This program calculates the surface area of the cube


def main():
    length = int(input("Enter the length of the cube: "))

    # process
    surface_area = 6*length**2

    # output
    print("")
    print("The surface area of the cube is {:.2f} cm^2".format(surface_area))


if __name__ == "__main__":
    main()
