
class Person:
    def __init__(self, name_value, birth_year):
        self.name = name_value
        self.birth_year = birth_year
        self.friends = []
        self.fav_books = []

    def age(self):
            return 2017-self.birth_year

    def printP(self):
        print self.str()

    def str(self):
        print self.name + ":" + str(self.age()) + str(self.fav_books)

    def add_friend(self,p):
        self.friends.append(p)

    def books(self,b):
        self.fav_books.append(b)


p1 = Person("Alexa", 22)
p1.books("Google")
p1.printP()

p2 = Person("Thomas", 46)
p2.books(" ")
p2.printP()

p3 = Person("Jeremie",18)
p3.books("A thousand splendid suns")
p3.printP()

print p1.friends
