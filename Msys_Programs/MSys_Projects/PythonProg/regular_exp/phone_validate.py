import re

def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

# print(extract_phone("my number is 432 567-8904"))
# print(extract_phone("my number is 432 567-890422"))
# print(extract_phone("432 567-8904 fdyhfhgfjyt"))
# print(extract_phone("432 567-890422"))

def extract_all_phones(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    return phone_regex.findall(input)

# print(extract_all_phones("my number is 432 567-8904 or call me at 345 666-7899"))
# print(extract_all_phones("my number is 432 56"))

# def is_valid_phone(input):
#     phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
#     match = phone_regex.search(input)
#     if match:
#         return True
#     return False

def is_valid_phone(input):
    phone_regex = re.compile(r"\d{3} \d{3}-\d{4}")
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False

print(is_valid_phone("432 567-8904"))
print(is_valid_phone("432 567-8904 ads"))
print(is_valid_phone("432 567-8904 d"))
