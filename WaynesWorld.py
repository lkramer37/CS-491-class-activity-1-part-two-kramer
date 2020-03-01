# Assignment 1: Implement a simple car class for Wayne’s ford pinto and a bicycle class for Garth’s BMX bike. Create
# constructors for each class. Use a file with a main method to instantiate/test each class.

# Assignment 2: Think of a set of useful properties (color? name?) for each class. Should these properties be private
# or public? implement getters and setter when appropriate.

# Assignment 3: Think of a set of useful methods (start()? pedal()?) for each class.

class VehicleClass:
    def __init__(self, color, make, model, wheels):
        self.color = color
        self.make = make
        self.model = model
        self.wheels = wheels

class CarClass(VehicleClass):
    def __init__(self, name, color, make, model, wheels):
        self.name = name
        super().__init__(color, make, model, wheels)

    def startCar(self):
        print("Car Started")


class BikeClass(VehicleClass):
    def __init__(self, color, make, model, wheels):
        super().__init__(color, make, model, wheels)

    def startPedal(self):
        print("Start Pedaling")


def main():
    print("This is the main function")

    carWayne = CarClass("Mirth Mobile", "pink", "Ford", "Pinto", "wheels")
    print("Car Name: " + carWayne.name +
          "Car Color: " + carWayne.color +
          "Car Make: " + carWayne.make +
          "Car Model: " + carWayne.model)
    carWayne.startCar()

    bikeGarth = BikeClass("green", "BMX", "bike", "wheels")
    print(bikeGarth.color, bikeGarth.make, bikeGarth.model)


if __name__ == "__main__":
    main()




# Assignment 4: Sometimes classes are composed with entities that are not expressible using Python data type (e.g.
# integer, string). For example, a car and bike both have wheels or a car has an engine. Create classes for each
# entity and use composition to add them to your car or bicycle class. You may use the same wheel class for cars and
# bikes.

# Assignment 5: Abstract both classes into a vehicle class. Should this class be abstract or not? Figure out what
# methods and properties should go in the vehicle class and what should stay in the car and bicycle class.
