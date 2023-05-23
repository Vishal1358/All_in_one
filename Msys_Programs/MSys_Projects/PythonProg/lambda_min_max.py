songs = [
    {"title":"barish","playcount":3.5},
    {"title":"Muskurana","playcount":3.49},
    {"title":"munjane","playcount":6},
    {"title":"onde","playcount":2.5},
    {"title":"kansugaran","playcount":2.49}
]

print(max(songs, key=lambda s: s["title"]))
print(min(songs, key=lambda s: s["title"]))


print(max(songs, key=lambda s: s["playcount"]))
print(min(songs, key=lambda s: s["playcount"])["title"])