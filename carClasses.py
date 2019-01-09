import random
import string
import csv
import collections


class Car:
    """
    A Car represents car in the list
    """
    def __init__(self, catalog_num, manufacturer, model, year, color, plate_num, price):
        """
        Initializes a car with the 7 string attributes from our file:
        catalog_num: string of ints, lowercase letters and '-'
        manufacturer: str, of letters
        model: str, of letters
        year: str, of ints > 0
        color: str, of letters
        plate_number: str, of ints and uppercase letters
        price: int > 0
        """
        self.catalog = catalog_num
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.color = color
        self.plate = plate_num
        self.price = price

    def __str__(self):
        """
        return a string describing all the details (7 attributes) of a car instance
        """
        return ("The plate number is: " + self.plate + "\nThe catalog num is:" + self.catalog +
                "\nThe Car Manufacturer is:" + self.manufacturer + "\nThe car model is: " + self.model +
                "\nThe year is: " + self.year + "\nThe color is: " + self.color + "\nPrice is: " + self.price)


class CarDict:
    """
    CarDict represents all the cars the agency own.
    """
    def __init__(self):
        """
        Initializes a car list with one attribute:
        cars: empty Ordereddict, will be a list where keys are plate numbers and values are Car instances
        """
        self.cars = collections.OrderedDict()

    def add_car(self, plate_number):
        """
        Adding a new car to the end of the cars ordered dictionary, if the car is not in the dict an error message will
        be printed. The new car will be identical to the Car object corresponding to the inserted plate number, except
        it will have a new random plate number. after adding the car the function will print the details of the new car
        to the user, using the str method of Car.
        input: str, plate number
        return: None
        """
        if plate_number in self.cars.keys():
            temp = self.cars[plate_number]
            new_car = Car(temp.catalog, temp.manufacturer, temp.model, temp.year, temp.color,
                          ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(17)),
                          temp.price)
            self.cars[new_car.plate] = new_car
            print("\nA new car was added:\n" + str(new_car))
        else:
            print("\nKeyError:\nThe plate number haven't been found in the system, try again\n")

    def del_car(self, plate_number):
        """
        del_car delete the key/plate number that was provided out of the orderedDict cars, than it prints the details of
        the car which was deleted  using the Car str method, if the car is not in the dict it will print an error
        message.
        param plate_number: str, plate number of a car
        return: None
        """
        if plate_number in self.cars.keys():
            del self.cars[plate_number]
            print("\nthe car with the plate number: " + plate_number + " was deleted")
        else:
            print("\nKeyError:\nThe plate number haven't been found in the system, try again\n")

    def search(self, plate_number):
        """
        Looks for the plate_number/ key in the cars, if the car is there it will print the details of the car using the
        str method of Car, if not it will print error message.
        param: plate number: str, plate number of a car
        return: None
        """
        if self.cars.get(plate_number, 0):
            print('For the inserted plate number\n' + str(self.cars[plate_number]))
        else:
            print("\nKeyError:\nThe plate number haven't been found in the system, try again\n")

    def manufacturer_summary(self, manufacturer):
        """
        Makes a summary of all the cars corresponding to a manufacturer.
        It iterates through the self.cars dict and makes a dict in which the keys are the strings indicating the models
        of the manufacturer, and the values are dicts in which the keys are strings of the colors, and values are ints
        indicating how many cars, of the particular model and color, are there.
        Using this dict the method prints a summary as follows:

        <manufacturer name> Summary:
            1. <model number 1's name>:
                -  <color 1>: int
                -  <color 2>: int
                ...
            2. <model number 2's name>:
                -  <color 1>: int
                -  <color 2>: int
             .
             .
             .

        param manufacturer: str, the name of the manufacturer, can be in upper/lower case letters
        return: None
        """
        man_dict = {}
        for car in self.cars.values():
            # if its the car of the right manufacturer
            if car.manufacturer.lower() == manufacturer.lower():
                # if the model and color are already in the dict add 1
                if man_dict.get(car.model, {}).get(car.color, 0):
                    man_dict[car.model][car.color] += 1
                # if the model is in the dict but this is the first car with this color let it be the first one
                elif man_dict.get(car.model, 0):
                    man_dict[car.model][car.color] = 1
                # if the model isn't in the dict yet put it in with 1 in the value of the particular color
                else:
                    man_dict[car.model] = {}
                    man_dict[car.model][car.color] = 1

        if man_dict:
            # prints the headline
            print(manufacturer.title() + " Summary:")
            for c, model in enumerate(man_dict):
                # prints the model headline
                print(str(c+1) + ". " + model+":")
                for color in man_dict[model]:
                    # prints the  model's colors and number of cars
                    print("-  " + color + ": " + str(man_dict[model][color]))
        # for when there are no cars corresponding to the manufacturer
        else:
            print("The agency do not posses cars of this manufacturer")
