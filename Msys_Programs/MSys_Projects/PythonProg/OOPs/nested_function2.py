from random import choice
def make_laugh_func():
    def get_laugh():
        l = choice(("HAHAHAH", "LOL", "TEHEHE"))
        return l
    
    return get_laugh

laugh = make_laugh_func()
print(laugh())