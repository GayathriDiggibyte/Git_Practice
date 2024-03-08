class Animal:
    def __init__(self, typeofanimal):
        self.typeofanimal = typeofanimal

    def make_sound(self):
        print("animal sound")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark! Bark!")

class cat(Animal):
    def __init__(self,breed):
        super().__init__("Cat")
        self.breed="Persian"

    def make_sound(self):
        print("Meow! Meow!")


animal1 = Animal("pet")
lab = Dog("Labrador")

persian_cat=cat("Persian")
print(animal1.typeofanimal)
animal1.make_sound()

print(lab.typeofanimal)
print(lab.breed)
lab.make_sound()

print(persian_cat.typeofanimal)
print(persian_cat.breed)
persian_cat.make_sound()
