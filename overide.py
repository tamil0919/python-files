class animal():
    
    def sound(self):
        print("animal make a sound")

class dog(animal):
    def sound(self):
        print("dog barks")
        
class bird(animal):
    def sound(self):
        print("bird singing")

a2=bird()
a2.sound()
