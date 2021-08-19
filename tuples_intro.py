# t = ("a", "b", "c")       # the output looks very much like a list but its in parentheses instead of square brackets
# print(t)                  # its always better to use parentheses when dealing with tuples
# this is how we tell the difference between a tuple and a list
# the program also works without the parentheses(optional)
#
# welcome = "Welcome to my nightmare", "Alice cooper", 1975
# bad = "Bad company", "Bad company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)            # this prints out the Metallica tuple printed out
#
# #
# # # Tuples are sequence type, which means we can use indexing, to access the individual items in the tuple.
#
# print(metallica[0])                 # INDEXING in tuples
# print(metallica[1])
# print(metallica[2])         # when indexing anything always use the square brackets, even though your indexing a list,
# a string or tuple.
# Indexing a tuple works the same way as a list
# you provide the index position in square brackets.
# unlike a list, tuple is immutable. if you attempt to change an item in the tuple we will get an error

# metallica[0] = "Master of puppets"      # tuple object doesnt support item assignment

# main difference between tuple and list
# 1. tuples are immutable
# 2. tuples use less memory than lists. --> one reason why you might want to use a tuple.
#### both tuples and lists are pythons equivalent of class constructors.(object oriented programming part of the course)

## there are another couple of reasons for preferring a tuple over a list.
# both reasons are due to tuples being immutable.

# 1. The first reason is to protect the integrity of your data. --> we cannot change tuples.

#
# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master of puppets"
# print(metallica2)
# # the list function returns a list using the values in the iterable thats passed to it .
# # print(type(metallica2))
# # since we got a list now, we can change the items in this list.
#
# metallica2[0] = "Master of Puppets"             # master of puppets released in 1984
# print(metallica2)

### Advantages of tuples:


#### 1. using a tuple for things that shouldnt change, can help to prevent bugs in your programs.
# when we try to alter the tuple a few minutes ago, the program crashed. obviously thats not good,
# but its something that we'd spot when testing the code.

# when we used a list the program didnt crash and we ended up with incorrect data. that could be far worse than
# the program crashing
## if your code attempts to change one of the fields in a tuple, your code will fail,
# that will highlight something that your code shouldnt be doing.

### its important that the data in memory, matches the data in the database, and using an immutable tuple can guard against
# unintended changes.

##### 2. advantage of using a tuple.
## the second advantage of a tuple is that you can always unpack them successfully.
# because a tuple cant be changed, you would always know how many items are there to unpack.
# thats why this is described as unpacking a tuple, even though you can unpack any sequence type.

#
# welcome = "Welcome to my nightmare", "Alice cooper", 1975
# bad = "Bad company", "Bad company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# print()
# table = ("coffee table", 200, 100, 75, 35.50)
# print(table[1] * table[2])
#
# print()
# name, length, width, height, price = table      # here we are unpacking the tuple into variables
# print(length * width)

# we unpack the tuple into variables and then we are using those variable names in our code.
# this is very useful.


#### nested tuples and lists

## we have also seen that the items in a sequence, can be a sequence type themselves.
# albums = [("Welcome to my nightmare", "Alice cooper", 1975),
#           ("Bad company", "Bad company", 1974),
#           ("Nightflight", "Budgie", 1981),
#           ("More Mayhem", "Emilda May", 2011),
#           ("Ride the Lightning", "Metallica", 1984),                #  here this list contains tuples \\
#           ]                                                         ## contains tuples\ the list is homogeneous -->
# #                                                                     ## everything is in the same type(tuple)
#                                                                     ## the tuples are heterogeneous -->
                                                                               ## each one contains two strings and an int
# # to find out the length of the list
# print(len(albums))
# # after putting these items in parentheses --> result --> becomes 5, meaning 5 tuples are present.
#
# # to print out a catalog of our items
# # all we have to do is iterate over the list
# for name, artist, year in albums:
#     # print("Albums: {}, Artist: {}, Year: {}".format(album[0], album[1], album[2]))
      # print("Albums: {}, Artist: {}, Year: {}".format(name, artist, year))                    # i did it by myself(surprising)
# print()
# # two ways to do it --> i did it in the previous way.
# for album in albums:
#     name, artist, year = album
#     print("Albums: {}, Artist: {}, Year: {}".format(name, artist, year))


##### we have also seen that the items in a sequence, can be a sequence type themselves.

## two ways to decide whether to use a list or a tuple, the first way is homogeneous or heterogeneous (mentioned above)
## the other way to help you decide --> is whether you want to add new items to it or not.
# you cant append to a tuple because tuples are immutable.
# if your going to be adding new items then a list is more suitable that a tuple.

## its quite likely that we would want to add a new album to our albums list.
## our program could be reading the albums from a disk file, or asking a user to type them in.
# its less likely that wed want to add another item to each of those tuple, while the program is executing.
# which is a good thing, because we cant.

## sometimes -- initial design might be wrong and in this case we forgot ti add the songs to our album tuples.
# when that happens, its fine to modify your tuples in your code. you cant do it while the program is executing, of course, but you can change your program if
# it doesnt do exactly what you want.

albums = [
    ("Welcome to my nightmare", "Alice cooper", 1975),
    ("Bad company", "Bad company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]
# to print the length of the list(albums)
print(len(albums))

# albums list contains tuples and each of those tuples contain 3 items

# to print a catalog, iterate over the list

for name, artist, year in albums:
    # print("Album: {}, Artist: {}, Year: {}".format(album[0], album[1], album[2]))
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

print()
for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))
print()

                        #### Nesting further

# now we might want to store a list of songs on each item as well
# if we do this then, each item in the list would become a tuple holing the name artist year and list of songs.
### we might end up with a tuple, containing a list that also contains tuples.
### or a list containing tuples, that also contains a list.

# now we got all the songs as well, we have to decide on how we will store the data.. using tuple or list.
# which one you chose isnt as important as why you chose it.
# lets examine what we know and dont know.

# --- we know that once an album is realease, the tracks on it dont change.
# --- you may get a later release that contains bonus tracks, but thats not the same album.
# --- if the number of tracks arnt foing to change, we dont need to add or remove items from which ever structure we have chosen.
# --- A tuple will work fine here.

