""" Weight Converter

convert Pounds to Kilograms and vice versa.
"""


def covert():
    weight = int(input("Enter your weight: "))
    unit = input("(L)bs or (K)g: ")
    if unit.upper() == "L":
        converted = weight * 0.45
        print(f"Your weight is  {converted} Kilos")
    else:
        converted = weight / 0.45
        print(f"Your weight is  {converted} Pounds")


if __name__ == "__main__":
    covert()
