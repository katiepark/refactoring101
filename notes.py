# Defining a class
class Dog(object):
    pass

# Instantiating a class
fido = Dog()

# Adding properties
fido.name = 'Fido'
fido.age = 4

# Adding a method to a class
class Cat(object):
    def sound(self):
        print 'meow'

fuzzy = Cat()
fuzzy.sound() # prints meow