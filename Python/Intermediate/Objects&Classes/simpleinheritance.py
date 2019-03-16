class SchoolMember():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initializing a School Member!!")

    def tell(self):
        print(f"Name is {self.name}, Age is {self.age}, ", end = "")

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary= salary
        print("Initializing a Teacher!!")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Salary is {self.salary}.")

class Student(SchoolMember):
    def __init__(self, name, age, mark):
        SchoolMember.__init__(self, name, age)
        self.mark = mark
        print("Initializing a Student!!")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Avg mark is {self.mark}")


MrBrown = Teacher("John", 40, "62000")
Smith = Student("David", 17, 10)


MrBrown.tell()
Smith.tell()

