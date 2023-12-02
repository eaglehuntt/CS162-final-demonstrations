# Eagle Hunt - CS162 Final project
# Demonstrations of CS concepts not present in my project submisisons


import os

class Tutorial:
    def __init__(self) -> None:
        pass

    def user_io(self):
        """

        User input is very basic in Python. the default input() function prints a string and gets a value from a user. This is a string unless otherwise specified as an int().

        """

        name = input("What is your name? ")
        print(f"Hello, {name}")

    def input_validation(self):
        """
        
        Input validation is the process of checking the entered value is valid. The try and except blocks are used to catch errors. The 'try' attempts the code in the block and runs it if there are no errors. If there are errors, instead of crashing the program the except block handles those errors.

        """

        while True:
            try:
                age = int(input("What is your age? "))
                break
            except ValueError:
                print("Please enter a valid number.")
        print(f"Your age is {age}")

    def file_io(self):
        """

        It is possible to create files, read files, and write to files in python. This is accomplished with the function 'open', where we can open a file with an intent to either 'x' create a file, 'r' read a file, or 'w' write to a file.
        
        """

        file_name = "tutorial_file.txt"

        if not os.path.exists(file_name):
            file = open(file_name, 'x')
            file.close()

        with open(file_name, "w") as file:
            contents = input("Enter what you want written to file: ")
            file.write(contents)
            print(f"Wrote, '{contents}' to file")

    def recursion(self, arr, target):
        """

        Recursion is a method of solving a problem by breaking it down into smaller subproblems, and calling itself to solve them. The example below is a recursive binary search.

        """

        def example_recursive_binary_search(array, left, right, target):
            
            if left > right:
                return -1
            
            else:
            
                mid = left + (right - left) // 2
                
                if array[mid] == target:
                    return mid
                
                elif array[mid] > target:
                    return example_recursive_binary_search(array, left, right-1, target)
                else:
                    return example_recursive_binary_search(array, left+1, right, target)
        print(example_recursive_binary_search(arr, 0, len(arr) - 1, target))
        return example_recursive_binary_search(arr, 0, len(arr) - 1, target)





"""
Below demonstrates inheritance in python. Inheritance is the process of creating a class that inherits from another class. The example below is a vehicle class, which is exteded by car and motercycle. All methods available to vehicle are accessable to car and motercycle. This is a coding pattern used when you need two objects that have a lot in common but may differ in other ways.

"""

class Vehicle:
    def __init__(self, name, engine, year):
        self.name = name 
        self.engine = engine 
        self.year = year

    def start(self):
        print("Starting...")
    
    def drive(self):
        print("Driving my", self.name, "with a", self.engine, "engine")

class Car(Vehicle):
    def __init__(self, name, engine, year):
        super().__init__(name, engine, year)

    def saftey_first(self):
        # Another instance of recursion

        is_safe = input("Do you have your seatbelt on? (y/n)")
        if is_safe == "y":
            self.drive()

        else:
            print("You need to put on your seatbelt!")
            self.saftey_first()

    def start(self):
        self.saftey_first()
        super().start()
        super().drive()
    

class Motorcycle(Vehicle):
    def __init__(self, name, engine, year):
        super().__init__(name, engine, year)

    def saftey_first(self):

        is_safe = input("Do you have your helmet on? (y/n)")
        if is_safe == "y":
            self.drive()
        else:
            print("You need to put on your helmet!")
            self.saftey_first()

    def start(self):
        self.saftey_first()
        super().start()
        super().drive()
        



if __name__ == "__main__":
    tutorial = Tutorial()

    tutorial.user_io()
    tutorial.input_validation()
    tutorial.file_io()
    tutorial.recursion([1,3,3,3,3,4,5,6,7,20,34,53,62], 62)

    ford = Car("Car", "V8", "2020")
    moped = Motorcycle("Moped", "V8", "2020")

    ford.start()
    moped.start()