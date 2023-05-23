def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("my name is Vishal")

@be_polite
def rage():
    print("I HATE YOU")

# we are decorating our function
#with politeness!
# greet = be_polite(greet)

# polite_rage = be_polite(rage)
# polite_rage()
greet()
rage()