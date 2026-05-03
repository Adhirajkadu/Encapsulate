class Revers:
    def __init__(self,):
        self.str = input("Enter a word :")
    def rev(self):
        return self.str[::-1]
a = Revers()
print("Revers string is ",a.rev())