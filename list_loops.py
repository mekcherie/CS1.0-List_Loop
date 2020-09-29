# The list we created above is called songs.
songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[1])
print(songs[0])
print(songs[2])

# will print ROCKSTAR and Do It
print(songs[0:2])
# will print out Do it and For The Night
print(songs[1:3])

# update the last element
songs[2] = "Nobody But You"
print(songs)

# adds an element to the end of the list
songs.append("Godly Man")
# adds a list to end of a list
songs.extend(["Happy"])
# adds element at specific index followed by item
songs.insert(2, "Grateful")
print(songs)

# removes element from list
songs.remove("Nobody But You")
# removes and returns element at specific index
songs.pop(1)
# removes all elements from a list
songs.clear()
#delete the 3rd element
del songs[0:2]
(print(songs))
# print(songs)
for song in songs:
    print(song)

