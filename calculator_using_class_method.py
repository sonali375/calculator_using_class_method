"""this is the calculator program"""


class Calculator():
    """this is the class for calculator"""

    def __init__(self, number1, number2):
        self.number_1 = number1
        self.number_2 = number2

    def add(self):
        """function for addition"""
        return self.number_1 + self.number_2

    def sub(self):
        """function for subtraction"""
        return self.number_1 - self.number_2

    def multiply(self):
        """function for multiplication"""
        return self.number_1 * self.number_2

    def divide(self):
        """function for division"""
        return self.number_1 / self.number_2


number_1 = int(input('Enter First number : '))
number_2 = int(input('Enter Second number : '))
obj = Calculator(number_1, number_2)
"""passing parameter to calculator"""

while True:
    def menu():
        """ function for showing the menu"""
        option = '1. Add \n2. Sub \n3. Multiply \n4. Divide \n5. Exit'
        print(option)
    menu()
    choice = int(input('Please select one of the following : '))
    if choice == 1:
        print("Result1: ", obj.add())
    elif choice == 2:
        print("Result2: ", obj.sub())
    elif choice == 3:
        print("Result3: ", obj.multiply())
    elif choice == 4:
        print("Result4: ", obj.divide())
    elif choice == 5:
        print('Thank You')
        break
    else:
        print('Invalid option')
        break
print()
