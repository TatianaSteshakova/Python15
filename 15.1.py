class Transport:

   def __init__(self, name, max_speed, mileage):

    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

   def print_info(self):
    print("Название автомобиля:", self.name, "Скорость:", self.max_speed, "Пробег:", self.mileage)

class Autobus(Transport):
   pass


a = Autobus("Renault Logan", 50, 12)
a.print_info()
