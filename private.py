class myclass:
    __pvar = 27
    def __privateMeth(self):
        print("I am inside myclass")
    def hello(self):
        print("Private variable value :",myclass.__pvar)
foo = myclass()
foo.hello()
foo.__privateMeth()