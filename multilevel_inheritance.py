class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal):
    def give_birth(self):
        print("Mammal gives birth")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")


my_dog = Dog()


my_dog.speak()
my_dog.give_birth()
my_dog.bark()
