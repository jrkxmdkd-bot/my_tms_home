from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Гав-гав"


class Cat(Animal):
    def speak(self):
        return "Мяу"


class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError("Неизвестный тип животного")


if __name__ == "__main__":
    factory = AnimalFactory()
    animal = factory.create_animal(input("Введите тип животного (dog/cat): "))
    print(animal.speak())
