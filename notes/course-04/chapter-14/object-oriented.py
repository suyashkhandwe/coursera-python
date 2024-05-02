"""Module for Object-Oriented Definitions and Terminology"""


class PartyAnimal:
    
    # Constructor
    # The `self` here is a syntax which allows to do `obj.method` calls.
    def __init__(self):
        self.x = 0
    
    # A sample method
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
    
    # Destructor
    def __del__(self):
        print("Destroy")

an = PartyAnimal()
an.party()
an.party()
an.party()

# This `dir` lists all the fields of the class of object `an`. This can be used for any types such as string etc.
print(dir(an))

an = 42

# Constructors with additional objects

class GuestCount:
    def __init__(self, name) -> None:
        self.guests = 0
        self.name = name
        print(self.name, "constructor")
    
    def guestCount(self, guests):
        self.guests = self.guests + guests
        print(self.name,"guests:", self.guests)

john = GuestCount("John Doe")
john.guestCount(2)
jane = GuestCount("Jane Dow")
jane.guestCount(3)

print("--------")
# Inheritance
class GuestCountWithChildren(GuestCount):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.childCount = 0
    
    def totalGuestCount(self, guests, children):
        self.childCount = self.childCount + children
        self.guestCount(guests)
        print(self.name,"guests", guests, "children", children)

john = GuestCountWithChildren("John Dow")
jane = GuestCountWithChildren("Jane Doe")
john.totalGuestCount(3,2)
jane.totalGuestCount(5,2)