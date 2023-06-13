from abc import ABC, abstractmethod


class Rider(ABC):
    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def riders(self):
        pass


class Bicycle(Rider):
    def ride(self):
        return "Human powered, not enclosed"

    def riders(self):
        return "1 or 2 if tandem or a daredevil"


class Motorcycle(Rider):
    def ride(self):
        return "Engine powered, not enclosed"

    def riders(self):
        return "1 or 2"


class Car(Rider):
    def ride(self):
        return "Engine powered, enclosed"

    def riders(self):
        return "1 plus comfortably"


if __name__ == "__main__":
    bike = Bicycle()
    motorcycle = Motorcycle()
    car = Car()

    print(bike.ride())
    print(bike.riders())
    print()
    print(motorcycle.ride())
    print(motorcycle.riders())
    print()
    print(car.ride())
    print(car.riders())