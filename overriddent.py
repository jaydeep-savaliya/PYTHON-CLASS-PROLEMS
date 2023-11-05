class Bird:
    def intro(self):
        print("birds")
    def fly(self):
        print("birds are fly")
class ostrich(Bird):
    def fly(self):
        print("ostrich cannot fly")
class sperrrow(Bird):
    def fly(self):
        print("sperrow can fly")
obj1 = Bird()
obj2 = ostrich()
obj3 = sperrrow()
obj1.intro()
obj1.fly()
obj2.intro()
obj2.fly()
obj3.intro()
obj3.fly()