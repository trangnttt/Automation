class Person:
    def __init__(self, name, age, genner):
        self.name = name
        self.age = age
        self.genner = genner
    
    def greet_person(self):
        print("Hello",self.name)

pers1 = Person("Phero", 30, "Male")
pers1.greet_person()

print(pers1.genner)