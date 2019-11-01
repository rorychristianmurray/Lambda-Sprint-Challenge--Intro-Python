# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle --> GroundVehicle --> Car/Motorcycle set-up
# Vehicle is base class


class Vehicle:
    def __init__(self, name):  # constructor
        self.name = name

    def __str__(self):
        return f"Name: {self.name}\n"


class GroundVehicle(Vehicle):
    def __init__(self, name):  # constructor
        self.name = name
        super().__init__(name)

    def __str__(self):
        return f"Name: {self.name}\n"


class Car(GroundVehicle):
    def __init__(self, name):  # constructor
        self.name = name
        super().__init__(name)

    def __str__(self):
        return f"Name: {self.name}\n"


class Motorcycle(GroundVehicle):
    def __init__(self, name):  # constructor
        self.name = name
        super().__init__(name)

    def __str__(self):
        return f"Name: {self.name}\n"

# create vehicles


v = Vehicle("Vehicle v")
g = GroundVehicle("GroundVehicle g")
c = Car("Car c")
m = Motorcycle("Motorcycle m")

print("Vehicle: ", v)
print("GroundVehicle: ", g)
print("Car: ", c)
print("Motorcycle: ", m)


# Vehicle --> FlightVehicle --> Starship
# Vehicle is the base class

class FlightVehicle(Vehicle):
    def __init__(self, name):  # constructor
        self.name = name
        super().__init__(name)

    def __str__(self):
        return f"Name: {self.name}\n"


class Starship(FlightVehicle):
    def __init__(self, name):  # constructor
        self.name = name
        super().__init__(name)

    def __str__(self):
        return f"Name: {self.name}\n"


fv = FlightVehicle("FlightVehicle fv")
s = Starship("Starship s")


print("FlightVehicle: ", fv)
print("Starship: ", s)


# FLightVehicle --> Airplane set-up
# FlightVehicle is the base class

class Airplane(FlightVehicle):
    def __init__(self, name):  # constructor
        self.name = name
        super().__init__(name)

    def __str__(self):
        return f"Name: {self.name}\n"


a = Airplane("Airplane a")

print("Airplane: ", a)
