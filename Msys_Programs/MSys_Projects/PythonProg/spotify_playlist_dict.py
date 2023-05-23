playlist = {
    "title":"jspider",
    "author":"keshav",
    "songs": [
        {'title':'hello', 'artist': ["blue"],'duration':2.5},
        {'title':'male', 'artist': ["kitty","djcat"],'duration':2.5},
        {'title':'munjane', 'artist': ["blue"],'duration':2.5}
    ]
}
total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
print(total_length)