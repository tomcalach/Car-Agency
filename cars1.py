import csv
import random
import sys
import carClasses
from carClasses import Car
from carClasses import CarDict
import argparse


def extract_file_to_list(file_directory):
    """
    Opens a file in the file_directory and returns a list of lists. in each nested list the items will be strings.
    To separate each line in the text by commas, ans separate each line to a different list the function use the
    csv.reader method.
    input: str, directory
    return: list of lists of str
    """
    with open(file_directory, 'r') as file:
        file_list = []
        file_reader = csv.reader(file)
        file_list.extend(file_reader)
        return file_list


def turn_list_to_car_dict(file_list):
    """
    gets a list of lists of 7 strings. it iterates through the super list and adds each nested list (list represents a
    car/line in the file), as a Car object to car_dict.cars. It returns car_dict --> a CarDict instance with
    car_dict.cars containing all the details from the file_list.
    param file_list: list of lists of 7 strings
    return: CarDict of all the Cars objects in file_list
    """
    car_dict = CarDict()
    for line in file_list:
        catalog, manufacturer, model, year, color, plate, price = line
        car_dict.cars[plate] = Car(catalog, manufacturer, model, year, color, plate, price)
    return car_dict


def save_car_dict_in_file(car_dict, file_directory):
    """
    save_car_dict_in_file is saving the information of all the cars (after the changes that wes made or not by the
    user), which are in car_dict, in a file (if the file name exist it is going to overwrite it). it iterates through
    all the values/Car objects in car_dict and saves them in file_directory.
    param car_dict: CarDict object
    param file_directory: str, file directory
    return: None
    """
    with open(file_directory, 'w', newline='') as file:
        file_writer = csv.writer(file, delimiter=',')
        for car in car_dict.cars.values():
            file_writer.writerow([car.catalog, car.manufacturer, car.model, car.year, car.color, car.plate,
                                 car.price])


def interactive_loop(car_dict):
    """
    Lets the user decide which action he would like to make: 1 - to search for a car info (if the search was chosen the
    user will be able to search as many cars as he wants without heading out to the main menu), 2- to add new car with
    the info of one of the cars in the file, or 3- to delete one of the cars in the file. The function will be
    terminated only when the user types the word exit, and after every step it will let the user to head back to the
    main menu when typing EXIT.
    input: CarList
    output: CarList, after all the changes
    """
    count = 0
    while count < 1:

        director = input("\nType the desired action:\n\
                         \nTo search a car type 1\nTo add a car type 2\nTo delete a car type 3\
                         \nTo exit type exit\n")
        if director == 'exit':
            break

        if director == '1':
            while 1:
                plate_number = input("\nPut the plate number to be searched here \nto exit type exit\n"
                                     "to go back to the main menu insert EXIT\n")
                if plate_number == 'exit':
                    count += 1
                    break
                elif plate_number == 'EXIT':
                    break
                car_dict.search(plate_number)

        elif director == '2':
            plate_number = input("to add another identical car with different plate number\n"
                                 "Put the wanted plate number here\ntype exit to exit\n"
                                 "to go back to the main menu insert EXIT\n")
            if plate_number == "exit":
                break
            if plate_number == "EXIT":
                continue
            car_dict.add_car(plate_number)

        elif director == '3':
            plate_number = input("to delete a car Put the wanted plate number here\n"
                                 "type exit to exit\nto go back to the main menu insert EXIT\n")
            if plate_number == "exit":
                break
            elif plate_number == "EXIT":
                continue
            car_dict.del_car(plate_number)

        else:
            print("Typing Error\nTry again")

    return car_dict


def main(file_directory):
    """
    If the user was specifying a desired action of --search or --summary as an addition argument the main() will run
    automatically; to search for a car (by plate number as an additional argument), or to summarize all the cars of a
    manufacturer (by manufacturer name as an additional argument), after that the program will finish
    If none additional arguments were given the program will send the user into the interactive loop, to enable him/her
    search for/add /delete a car as many times as he/she wish for.
    param: file_directory, the file to be used and changed
    return: none
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--search', '-s', help='search a car corresponding to a plate num')
    parser.add_argument('--summary', help='get manufacturer summary')
    parsed_args = parser.parse_args()

    # we are making a CarDict instance, containing all the cars of the file
    car_dict = turn_list_to_car_dict(extract_file_to_list(file_directory))

    if parsed_args.search:
        searched_plate = parsed_args.search
        car_dict.search(searched_plate)

    elif parsed_args.summary:
        manufacturer = parsed_args.summary
        car_dict.manufacturer_summary(manufacturer)

    else:
        car_dict = interactive_loop(car_dict)
        save_car_dict_in_file(car_dict, file_directory)


if __name__ == '__main__':
    main('C:\\python ex\\cars.csv')

