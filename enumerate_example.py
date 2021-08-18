# for index, character in enumerate("abcdefgh"):
#     print(index, character)
    #if we want the indexing of the characters to start from index no. 1 then
    # print(index + 1, character)
# index --> gets the index position
# character --> gets each character from the string.
# for index, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
    # print(index, char)


                            ##Adding items to a list -- Challenge

# data = [
#     "Andromeda - Shrub",
#     "Bellflower - Flower",
#     "China Pink - Flower",
#     "Daffodil - Flower",
#     "Evening Primrose - Flower",
#     "French Marigold - Flower",
#     "Hydrangea - Shrub",
#     "Iris - Flower",
#     "Japanese Camellia - Shrub",
#     "Lavender - Shrub",
#     "Lilac - Shrub",
#     "Magnolia - Shrub",
#     "Peony - Shrub",
#     "Queen Anne's Lace - Flower",
#     "Red Hot Poker - Flower",
#     "Snapdragon - Flower",
#     "Sunflower - Flower",
#     "Tiger Lily - Flower",
#     "Witch Hazel - Shrub",
# ]
#
# flowers = []
# shrubs = []
#
# for plant in data:
#     if "Flower" in plant:
#         flowers.append(plant)
#     else:
#         shrubs.append(plant)
# print(flowers)
# print(shrubs)
print()
                        ##### LETs see how tuples are being unpacked in this code.
#
# for index, character in enumerate("abcdefgh"):
#     print(index, character)
######### --->>> each time aroung the loop, index and character are unpacked from the tuple that enumerate creates.
# each time through the loop --> index gets the index position and character gets the character from the string.
print()
for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)
    ## now here we unpack the tuple to the two variables index and character.

# t will get the value of whatever the next value of enumerate is, as it iterates.
# now we got 8 tuples in the result.
# Each tuple has that index position and a character at that index position.
#### unpacking tuples is a very valuable technique.
index, character = (0, 'a')
print(index)
print(character)

## each time aroung the loop, index and character are unpacked from the tuple that enumerate creates.
## so the first code is a shorthand version of the second code.
# instead of stroing each tuple in t, we unpack it as we are iterating.