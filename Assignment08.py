# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Tim Shore, 12.07.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Tim Shore, 12.07.2020,Modified code to complete assignment 8
    """

    # -- Fields -- #

    # -- Constructor -- #
    def __init__(self, item='', price=0.00):
        # -- Attributes -- #
        self.__product_name, self.__product_price = item, price

    # -- Properties -- #

    @property
    # ProductName
    def product_name(self):  # getter or accessor
        return str(self.__product_name)  # product name converted to private string

    @product_name.setter
    def product_name(self, add_name):  # setter or mutator
        self.__product_name = add_name

    @property
    # ProductPrice
    def product_price(self):  # getter or accessor
        return str(self.__product_price)  # product price converted to private float

    @product_price.setter
    def product_price(self, add_price):  # setter or mutator
        self.__product_price = add_price

    def __str__(self):
        return self.product_name + ', ' + self.product_price

    # -- Methods -- #

#  End of Class
# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Tim Shore,12.07.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def add_data_to_file(product_name, product_price, list_of_objects):
        new_row = Product(product_name, product_price)
        list_of_objects.append(new_row)
        print('\n')
        return list_of_objects

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):  # write data to file
        text_file = open(file_name, 'a')
        for obj in list_of_rows:
            text_file.write(obj.product_name + ', ' + obj.product_price + '\n')
        text_file.close()

    # End of Class


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Contains the input and output tasks:

    Create a menu for the user
        1. Show Data in File
        2. Input Data for File
        3. Save Data in File
        4. Exit

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Tim Shore,12.07.2020,Modified code to complete assignment 8

        methods:
            print_menu_options  # prints the menu options for user
            input_menu_choice  # allows user to choose an option from menu
            show_data  # prints the data for the user
            add_data  # adds the dictionary items to the data list
    """

    @staticmethod
    def print_menu_options():
        print('''
        List of Products and their Prices
        
        Main Menu:
        1. Current List
        2. Add a Product and Price to the List
        3. Save Data to File
        4. Exit
        ''')

    @staticmethod
    def input_menu_choice():  # gets the menu input choice from user
        choice = str(input('Please enter 1, 2, 3, or 4 as your selection: ')).strip()
        return choice

    def show_file(self, file_name):
        with open(file_name, 'r') as file:
            return file.read()

    @staticmethod
    def input_data():
        while True:
            add_product = input('Enter a Product: ').strip()
            if not add_product.isnumeric():
                break
            else:
                print('The Product Name should only use letters')
        while True:
            try:
                add_price = float(input('What is the Price?: '))
                break
            except ValueError:
                print('The price must be in numbers or with a decimal only')
        return add_product, add_price
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
print('\nCurrent List of Products and Prices in File:')
f = IO()
print(f.show_file('products.txt'))

while True:  # Get user's menu option choice
    IO.print_menu_options()
    menu_choice = IO.input_menu_choice()
    print(menu_choice)

    if menu_choice.strip() == '1':  # Show user current data in the list of product objects
        f = IO()
        print(f.show_file('products.txt'))
        continue

    if menu_choice.strip() == '2':  # Let user add data to the list of product objects
        ProductName, ProductPrice = IO.input_data()
        FileProcessor.add_data_to_file(ProductName, ProductPrice, lstOfProductObjects)
        continue

    if menu_choice.strip() == '3':  # Let user save current data to file
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print('Data Saved!')
        continue

    if menu_choice.strip() == '4':  # Exit Program
        break

    else:
        print('Not a valid selection. Try again!')

# Main Body of Script  ---------------------------------------------------- #
