


#inheritance
class Person:
    def __init__(self, name="AIMAN", lastname="ROCHD", age=18):
        if age >= 18:
            self._name = name
            self._lastname = lastname
            self._age = age
            
    def get_info(self):
        print(f"The data and functions are encapsulated, \n"
              f"My Name is: {self._name}, \n"
              f"My Last Name: {self._lastname}, \n"
              f"and I am {self._age} years old, \n")

print("=== Person Class ===")

person_ob1 = Person('MAHAMAWDA', 'BENNANI', 99)
person_ob1.get_info()

class Student(Person):
    def __init__(self, name, lastname, age, dob, adress):
        Person.__init__(self, name, lastname, age)
        self.dob = dob
        self.adress = adress
    def get_info(self):
        print(f"The data and functions are encapsulated, \n"
              f"My Name is: {self._name}, \n"
              f"My Last Name: {self._lastname}, \n"
              f"and I am {self._age} years old, \n"
              f"born at: {self.dob}, \n"
              f"that lives in: {self.adress}, \n")

print("=== Student Class ===")

student_obj1 = Student('HASSAN', '2', 20, '27/09/2007', 'Khouribga')
student_obj1.get_info()
