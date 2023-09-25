#Vehicle is the base class
class Vehicle:

  def setVehicleMake(self, make):
    self.string_make = make

  def setVehicleModel(self, model):
    self.string_model = model

  def getVehicleMake(self):
    return self.string_make

  def getVehicleModel(self):
    return self.string_model

#Car class inherits from Vehicle
class Car(Vehicle):

  def setCarDoor(self, doors):
    self.string_door = doors

  def getCarDoor(self):
    return self.string_door

#Truck class inherits from vehicle
class Truck(Vehicle):

  def setBedLength(self, bedlength):
    self.string_bedlength = bedlength

  def getBedLength(self):
    return self.string_bedlength

#Main program function (Vehicle building)
print("Welcome to Champion's Virtual Garage")
option = 0
while int(option) < int(3):
  option = input("Enter 1 to create a Car, 2 to create a Truck or 3 to quit: ")
#Option 1 is for creating a car
  if (option == '1'):
    createCar = Car()
    string_make = input("Enter the car's make:")
    createCar.setVehicleMake(string_make)
    string_model = input("Enter the car model:")
    createCar.setVehicleModel(string_model)
    string_door = input("Enter the number of doors:")
    createCar.setCarDoor(string_door)
    print(f"The make is: {createCar.getVehicleMake()}")
    print(f"The model is: {createCar.getVehicleModel()}")
    print(f"The number of doors: {createCar.getCarDoor()}")
    print("This car has been added to the Champion Virtual Garage.")
#Option 2 is for creating a truck
  elif (option == '2'):
    createTruck = Truck()
    string_make = input("Enter the truck make:")
    createTruck.setVehicleMake(string_make)
    string_model = input("Enter the truck model:")
    createTruck.setVehicleModel(string_model)
    string_bedlength = input("Enter the bed length in feet:")
    createTruck.setBedLength(string_bedlength)
    print(f"The make is: {createTruck.getVehicleMake()}")
    print(f"The model is: {createTruck.getVehicleModel()}")
    print(f"The bed length is: {createTruck.getBedLength()} feet")
    print("This car has been added to the Champion Virtual Garage.")
#Option 3 is for ending the program
  else:
   print("Thank you for using Champion's Virtual Garage")
