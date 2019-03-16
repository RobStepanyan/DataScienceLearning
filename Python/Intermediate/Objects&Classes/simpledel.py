class Robots():
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"{name} is initializing!")
        Robots.population += 1

    def howmany():
        print(f"There are {Robots.population} robots alive!!")

    def sayhi(self):
        print(f"Hello I am the robot, my name is {self.name}")

    def __del__(self):
        print(f"{self.name} is dying!!")
        Robots.population -= 1
        if Robots.population == 0:
            print(f"{self.name} was the last robot!")
        else:
            print(f"{Robots.population} robots remaining!")

droid1 = Robots("Qyal1")
droid1.sayhi()
Robots.howmany()

droid2 = Robots("Cogol2")
droid2.sayhi()
Robots.howmany()

print("\nThe work is in the progress!!")
print("The work is done, time to destruct the robots!!\n")

del droid1
del droid2
