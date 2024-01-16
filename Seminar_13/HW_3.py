class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidIdError(Exception):
    pass

class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        if not last_name or not first_name or not middle_name:
            raise InvalidNameError("Invalid name: . Name should be a non-empty string.")
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f"Invalid age: {age}. Age should be a positive integer.")
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    def birthday(self):
        self.age += 1
    def get_age(self):
        return self.age

class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, employee_id):
        super().__init__(last_name, first_name, middle_name, age)
        if not isinstance(employee_id, int) or employee_id < 100000 or employee_id > 999999:
            raise InvalidIdError(f"Invalid id: {employee_id}. Id should be a 6-digit positive integer between 100000 and 999999.")
        self.employee_id = employee_id

    def get_level(self):
        return sum(int(digit) for digit in str(self.employee_id)) % 7

