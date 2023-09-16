'''
conversion.py
v1.0.1
nail_
'''

conversion_values = {
    "-": 1,
    "f": (10 ** -15),
    "p": (10 ** -12),
    "n": (10 ** -9),
    "u": (10 ** -6),
    "m": (10 ** -3),
    "c": (10 ** -2),
    "d": (10 ** -1),
    "da": (10 ** 1),
    "h": (10 ** 2),
    "k": (10 ** 3),
    "M": (10 ** 6),
    "G": (10 ** 6),
    "T": (10 ** 12),
    "P": (10 ** 15),
}

def calculation(origin, final, input_value):
    result = origin * (input_value / final)
    return result

def truncate(number):
    number_str = format(number, '.16g')  
    if 'e' in number_str:
        num, exp = number_str.split('e')
        exp = int(exp)
        return '{}e{}'.format(num, exp)
    return number_str

def common():
    input_value = float(input("Insert input value (as decimal!) "))
    print("1. nano (n)")
    print("2. micro (u)")
    print("3. milli (m)")
    print("4. centi (c)")
    print("5. kilo (k)")
    print("6. (-) No prefix")
    
    user_Input = input("Choose original unit ")
    origin = 0
    while origin == 0:
        if user_Input == "1":
            origin = conversion_values["n"]
        elif user_Input == "2":
            origin = conversion_values["u"]
        elif user_Input == "3":
            origin = conversion_values["m"]
        elif user_Input == "4":
            origin = conversion_values["c"]
        elif user_Input == "5":
            origin = conversion_values["k"]
        elif user_Input == "6":
            origin = conversion_values["-"]
        else:
            print("Invalid input")

    print("1. nano (n)")
    print("2. micro (u)")
    print("3. milli (m)")
    print("4. centi (c)")
    print("5. kilo (k)")
    print("6. (-) No prefix")
    user_Input = input("Choose final unit ")
    final = 0
    while final == 0:
        if user_Input == "1":
            final = conversion_values["n"]
        elif user_Input == "2":
            final = conversion_values["u"]
        elif user_Input == "3":
            final = conversion_values["m"]
        elif user_Input == "4":
            final = conversion_values["c"]
        elif user_Input == "5":
            final = conversion_values["k"]
        elif user_Input == "6":
            final = conversion_values["-"]
        else:
            print("Invalid input")
    print(truncate(calculation(origin, final, input_value)))

def extended():
    input_value = float(input("Insert input value (as decimal!) "))
    print("1. femto (f)")
    print("2. pico (p)")
    print("3. nano (n)")
    print("4. micro (u)")
    print("5. milli (m)")
    print("6. centi (c)")
    print("7. deci (d)")
    print("8. deca (da)")
    print("9. hecto (h)")
    print("10. kilo (k)")
    print("11. Mega (M)")
    print("12. Giga (G)")
    print("13. Tera (T)")
    print("14. Peta (P)")
    print("15. (-) No prefix")
    
    user_Input = input("Choose original unit ")
    origin = 0
    while origin == 0:
        if user_Input == "1":
            origin = conversion_values["f"]
        elif user_Input == "2":
            origin = conversion_values["p"]
        elif user_Input == "3":
            origin = conversion_values["n"]
        elif user_Input == "4":
            origin = conversion_values["u"]
        elif user_Input == "5":
            origin = conversion_values["m"]
        elif user_Input == "6":
            origin = conversion_values["c"]
        elif user_Input == "7":
            origin = conversion_values["d"]
        elif user_Input == "8":
            origin = conversion_values["da"]
        elif user_Input == "9":
            origin = conversion_values["h"]
        elif user_Input == "10":
            origin = conversion_values["k"]
        elif user_Input == "11":
            origin = conversion_values["M"]
        elif user_Input == "12":
            origin = conversion_values["G"]
        elif user_Input == "13":
            origin = conversion_values["T"]
        elif user_Input == "14":
            origin = conversion_values["P"]
        elif user_Input == "15":
            origin = conversion_values["-"]
        else:
            print("Invalid input")

    print("1. femto (f)")
    print("2. pico (p)")
    print("3. nano (n)")
    print("4. micro (u)")
    print("5. milli (m)")
    print("6. centi (c)")
    print("7. deci (d)")
    print("8. deca (da)")
    print("9. hecto (h)")
    print("10. kilo (k)")
    print("11. Mega (M)")
    print("12. Giga (G)")
    print("13. Tera (T)")
    print("14. Peta (P)")
    print("15. (-) No prefix")
    
    user_Input = input("Choose final unit ")
    final = 0
    while final == 0:
        if user_Input == "1":
            final = conversion_values["f"]
        elif user_Input == "2":
            final = conversion_values["p"]
        elif user_Input == "3":
            final = conversion_values["n"]
        elif user_Input == "4":
            final = conversion_values["u"]
        elif user_Input == "5":
            final = conversion_values["m"]
        elif user_Input == "6":
            final = conversion_values["c"]
        elif user_Input == "7":
            final = conversion_values["d"]
        elif user_Input == "8":
            final = conversion_values["da"]
        elif user_Input == "9":
            final = conversion_values["h"]
        elif user_Input == "10":
            final = conversion_values["k"]
        elif user_Input == "11":
            final = conversion_values["M"]
        elif user_Input == "12":
            final = conversion_values["G"]
        elif user_Input == "13":
            final = conversion_values["T"]
        elif user_Input == "14":
            final = conversion_values["P"]
        elif user_Input == "15":
            final = conversion_values["-"]
        else:
            print("Invalid input")

    print(truncate(calculation(origin, final, input_value)))

def main():
    user_Input = "0"
    while user_Input == "0":
        print("Select Menu")
        print("1. Common Inputs - Short list of commonly asked values in questions")
        print("2. All IB Inputs - All values listed for IB under the curriculum")
        print("0. Will always exit")
        user_Input = input()
        if user_Input == "1":
            common()
        elif user_Input == "2":
            extended()

if __name__ == "__main__":
    main()

