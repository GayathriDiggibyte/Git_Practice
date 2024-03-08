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


animal1 = Animal("pet")
lab = Dog("Labrador")

#
print(animal1.typeofanimal)
animal1.make_sound()

print(lab.typeofanimal)
print(lab.breed)
lab.make_sound()
