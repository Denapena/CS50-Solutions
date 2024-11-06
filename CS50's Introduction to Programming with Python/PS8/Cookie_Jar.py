class Jar:
    def __init__(self,capacity):
        self.cookies = 0
        self.capacity = capacity

    def __str__(self):
        return "Cookies: " + self.cookies*'🍪'
    
    def deposit(self,n):
        if self.capacity - n >= self.cookies:
            self.cookies += n
        else:
            print("Not enough space in the cookie jar!")
    
    def withdraw(self,n):
        if self.cookies - n >= 0:
            self.cookies -= n
        else:
            print(f"There are only {self.cookies} cookies in the jar!")
        
    def show_capacity(self):
        print(f"Cookie jar capacity is {self.capacity} cookies!")
    
    def show_size(self):
        print(f"There are {self.cookies} cookies in the jar!")
    
first = Jar(30)
first.show_capacity()
first.show_size()
print(first)
first.deposit(35)
first.show_capacity()
first.show_size()
print(first)
first.withdraw(35)
first.show_capacity()
first.show_size()
print(first)
