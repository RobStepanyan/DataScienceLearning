class Person():
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        print(f"Hi, We're glad to see you, {self.name}")

p1 = Person("Dambul")
p1.sayhi()