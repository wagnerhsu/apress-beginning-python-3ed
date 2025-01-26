# Use str() when you need a human-readable representation, such as printing a user-friendly message or displaying information in a UI.
# Use repr() when you need a detailed and precise representation, such as logging, debugging, or generating output that can be evaluated back into the original object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

# Creating an instance of Person
person = Person("Alice", 30)

print("Using str():", str(person))  # Output: Alice, 30 years old
print("Using repr():", repr(person))  # Output: Person(name='Alice', age=30)