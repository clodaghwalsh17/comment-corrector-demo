class Person:
    """
    A class used to represent a Person
    """
    id_prefix = 19

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def over_18(self):
        return self.age >= 18

# Create instance of person
p = Person("Mary", 25)
print(p.over_18())