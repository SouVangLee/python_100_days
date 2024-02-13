# Class Inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale.")

# class <Name>(<inherit_class_name>):        
class Dog(Animal):
    def __init__(self):
        #Add super().__init__()
        super().__init__()
    
    def bark(sekf):
        print("Woof! Woof!")
     
    # You can do extra functionalities by adding to the method
    def breathe(self):
        super().breathe()
        print("Running out of breath!")

daisy = Dog()
daisy.bark()
daisy.breathe()