'''
conversion.py
v1.0.0
nail_
'''

class Conversion():
    def __init__(self):
        self.origin = 0
        self.final = 0
        self.input = 0
        self.conversion_values = {
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

    def calculation(self):
        result = self.origin * (self.input / self.final)
        return result

    def truncate(self, number):
        number_str = format(number, '.16g')  
        if 'e' in number_str:
            num, exp = number_str.split('e')
            exp = int(exp)
            return f'{num}e{exp}'
        return number_str

    def common(self):
        self.input = float(input("Insert input value (as decimal!) "))
        print("1. nano (n)")
        print("2. micro (u)")
        print("3. milli (m)")
        print("4. centi (c)")
        print("5. kilo (k)")
        print("6. (-) No prefix")
        user_Input = input("Choose original unit ")
        while self.origin == 0:
            if user_Input == "1":
                self.origin = self.conversion_values["n"]
            elif user_Input == "2":
                self.origin = self.conversion_values["u"]
            elif user_Input == "3":
                self.origin = self.conversion_values["m"]
            elif user_Input == "4":
                self.origin = self.conversion_values["c"]
            elif user_Input == "5":
                self.origin = self.conversion_values["k"]
            elif user_Input == "6":
                self.origin = self.conversion_values["-"]

        print("1. nano (n)")
        print("2. micro (u)")
        print("3. milli (m)")
        print("4. centi (c)")
        print("5. kilo (k)")
        print("6. (-) No prefix")
        user_Input = input("Choose final unit ")
        while self.final == 0:
            if user_Input == "1":
                self.final = self.conversion_values["n"]
            elif user_Input == "2":
                self.final = self.conversion_values["u"]
            elif user_Input == "3":
                self.final = self.conversion_values["m"]
            elif user_Input == "4":
                self.final = self.conversion_values["c"]
            elif user_Input == "5":
                self.final = self.conversion_values["k"]
            elif user_Input == "6":
                self.final = self.conversion_values["-"]
            else:
                print("Invalid input")
        print(self.truncate(self.calculation()))

    def extended(self):
        self.input = float(input("Insert input value (as decimal!) "))
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
        while self.origin == 0:
            if user_Input == "1":
                self.origin = self.conversion_values["f"]
            elif user_Input == "2":
                self.origin = self.conversion_values["p"]
            elif user_Input == "3":
                self.origin = self.conversion_values["n"]
            elif user_Input == "4":
                self.origin = self.conversion_values["u"]
            elif user_Input == "5":
                self.origin = self.conversion_values["m"]
            elif user_Input == "6":
                self.origin = self.conversion_values["c"]
            elif user_Input == "7":
                self.origin = self.conversion_values["d"]
            elif user_Input == "8":
                self.origin = self.conversion_values["da"]
            elif user_Input == "9":
                self.origin = self.conversion_values["h"]
            elif user_Input == "10":
                self.origin = self.conversion_values["k"]
            elif user_Input == "11":
                self.origin = self.conversion_values["M"]
            elif user_Input == "12":
                self.origin = self.conversion_values["G"]
            elif user_Input == "13":
                self.origin = self.conversion_values["T"]
            elif user_Input == "14":
                self.origin = self.conversion_values["P"]
            elif user_Input == "15":
                self.origin = self.conversion_values["-"]
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
        while self.final == 0:
            if user_Input == "1":
                self.final = self.conversion_values["f"]
            elif user_Input == "2":
                self.final = self.conversion_values["p"]
            elif user_Input == "3":
                self.final = self.conversion_values["n"]
            elif user_Input == "4":
                self.final = self.conversion_values["u"]
            elif user_Input == "5":
                self.final = self.conversion_values["m"]
            elif user_Input == "6":
                self.final = self.conversion_values["c"]
            elif user_Input == "7":
                self.final = self.conversion_values["d"]
            elif user_Input == "8":
                self.final = self.conversion_values["da"]
            elif user_Input == "9":
                self.final = self.conversion_values["h"]
            elif user_Input == "10":
                self.final = self.conversion_values["k"]
            elif user_Input == "11":
                self.final = self.conversion_values["M"]
            elif user_Input == "12":
                self.final = self.conversion_values["G"]
            elif user_Input == "13":
                self.final = self.conversion_values["T"]
            elif user_Input == "14":
                self.final = self.conversion_values["P"]
            elif user_Input == "15":
                self.final = self.conversion_values["-"]
            else:
                print("Invalid input")

        print(self.truncate(self.calculation()))
   
    def main(self):
        user_Input = "0"
        while user_Input == "0":
            print("Select Menu")
            print("1. Common Inputs - Short list of commmonly asked values in questions")
            print("2. All IB Inputs - All values listed for IB under the curriculum")
            print("0. Will always exit")
            user_Input = input()
            if user_Input == "1":
                self.common()
            elif user_Input == "2":
                self.extended()

c = Conversion()
if __name__ == "__main__":
    c.main()
