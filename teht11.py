from classes import Publication, Book, Magazine, Car, ElectricCar, GasolineCar

newBook = Publication(Book("NEWBOOK!", "Rosa Liksom", 192))
newMagazine = Publication(Magazine("Donald Duck", "Aki Hyyppä"))

newBook.print_information()
newMagazine.print_information()

CarElectric = ElectricCar("ABC-15", 180, 52.5)
CarGas = GasolineCar("ACD-123", 165, 32.3)
CarElectric.accelerate(30)
CarGas.accelerate(30)
CarElectric.drive(3)
CarGas.drive(3)


print(CarElectric.travelled_distance, CarGas.travelled_distance)
