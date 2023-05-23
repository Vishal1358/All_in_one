def extract_digits(string):
    digits = []
    for char in string:
        if char.isdigit():
            digits.append(char)
    digits = sorted(digits)
    return ''.join(digits)
def extract_special_chars(string):
    special_chars = []
    for char in string:
        if not char.isalnum():
            special_chars.append(char)
    special_chars.reverse()
    return ''.join(special_chars)
def extract_vowels(string):
    vowels = []
    for char in string:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(char)
    vowels.reverse()
    return ''.join(vowels)

string = "abcd123byEaIO099@#$8"     #abcdbyEaIO-aEaIo-OIaEa
digits = extract_digits(string)
special_chars = extract_special_chars(string)
vowels = extract_vowels(string)

print(f"digits - {digits}")
print(f"special character - {special_chars}")
print(f"vowels - {vowels}")
