# classes are blueprints for creating objects
# we can put objects or methods inside

class Vehicle:
    # creating object
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self): # method
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car = Vehicle("Tesla", "Model 3!")

# now we can retrieve values from the object created
print(my_car.make) # Tesla
print(my_car.model) # Model 3

my_car.moves() # Moves along...
my_car.get_make_model() # I'm a Tesla Model 3!



# class inheritance - we can pass classes as arguments into other classes
# при цьому ми отримуємо доступ до методів цих класів які передали як аргументи

class Airplane(Vehicle):
    def moves(self):
        print("Flies along...")

class Truck(Vehicle):
    def moves(self):
        print("Rumbling along...")

class GolfCart(Vehicle):
    pass

cessna = Airplane("Cessna", "Skyhawk")
ford = Truck("Ford", "150")
golfwagon = GolfCart("Yamaha", "GC100")

cessna.get_make_model()
cessna.moves()
ford.get_make_model()
ford.moves()
golfwagon.get_make_model()
golfwagon.moves()

