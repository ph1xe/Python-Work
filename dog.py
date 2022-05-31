class Dog:

    species = "Canis familiaris"

    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed

    def getInfo(self):
        return "{} is a(n) {} {}.".format(self.name, self.color, self.breed)

    def speak(self, sound):
        return "{} {}s".format(self.name, sound)

dog1 = Dog("Izzy", "orange", "Golden Retriever")
dog2 = Dog("Molly", "black", "Cockapoo")

print(dog1.getInfo())
print(dog1.speak("bark"))

print(dog2.getInfo())
print(dog2.speak("woof"))