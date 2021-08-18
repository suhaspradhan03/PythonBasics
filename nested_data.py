albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# for name, artist, year, songs in albums:
#     print("Album: {}, Artist: {}, Year: {}, Songs: {}".format(name, artist, year, songs))
# print()
# print()
# # this is to separate an album from the whole list of items.
# album = albums[2]
# print(album)
#
# # this is to print the list of songs inside the previous tuple
# songs = album[3]
# print(songs)
#
# # we can get any particular song by indexing into the list of songs.
# song = songs[1]
# print(song)
# # if we only want the title in this tuple then we can further index it
# print(song[1])
#
# # if an item we get is another list or tuple we can index into that.
# # if that is also a list or a tuple we can index into that again.
# print()
# print()
# album1 = albums[3]
# print(album1)
# b = album1[3]
# print(b)
# c = b[2]    # mayhem
# print(c[1]) # position 1
#
# # all in one go
# print()
# mayhem = albums[3][3][2][1]
# print(mayhem)
#
# # reaper = albums[2][3][2][1]
# # print(reaper)