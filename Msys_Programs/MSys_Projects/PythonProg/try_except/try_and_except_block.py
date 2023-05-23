def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
d = {"name":"vishal"}
print(get(d, "city"))
# d["city"]
