class a: 
    def __init__(self):
        print("a")
    def display(self):
        print("a")

class b(a):
    def __init__(self):
        super().__init__()
        print("b")
    def display(self):
        print("b")


class c(a,b):
    def __init__(self):
        super().__init__()
        print("c")
    def display(self):
        print("c")
        
boj=c()
