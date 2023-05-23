import pickle
dct = {111: "Eric", 112: "Kyle", 113: "Butters"}

with open('test.txt', 'wb') as f:
    pickle.dump(dct, f)
with open('test.txt', 'rb') as f:
    dct2 = pickle.load(f)

print(dct2[112])
