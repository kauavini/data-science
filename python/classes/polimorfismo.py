class Veichle:
  def __init__(self, brand, model):
        self.brand = brand
        self.model = model
  def move(self):
        print("Movimentando!")

class Car(Veichle):

  def move(self):
    print("Drive!")

class Boat(Veichle):

  def move(self):
    print("Sail!")

class Plane(Veichle):
  pass


plane = Plane("AirBus", "1234")
car = Car("Amarok", "1234")
boat = Boat("Barco", "1234")


plane.move()
car.move()
boat.move()
