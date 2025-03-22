'''
Use the code below to finish the fullname function and make it a property. Also create a setter function for it. When user call the setter function with a full name, it will set the first name and last name to the object.

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullname(self):
        pass

Sample output:

p = Person("Tyler", "Shen")

# this is the getter function
print(p.fullname)   # Tyler Shen
print(p.firstname)   # Tyler

# now try the setter function. After you call it with a new full name, it will assign first name and last name separately to object's firstname and lastname

p.fullname = "Jimmy Lei"
print(p.fullname)  # Jimmy Lei
print(p.firstname)  # Jimmy

'''

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property    
    def fullname(self):
        return self.first + ' '+ self.last

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split()
        self.firstname = firstname
        self.lastname = lastname

p = Person("Tyler", "Shen")
print(p.fullname)
print(p.firstname)
p.fullname = "Jimmy Lei"
print(p.fullname)
print(p.firstname)
