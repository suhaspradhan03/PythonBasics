flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

# for flower in flowers:                  # what we did here is iterated over a list and printed each item.
#     print(flower)

# The JOIN method takes care of iterating for us
# we give it an iterable and it joins all the items in that iterable.
# it uses the string we call it on as the separator.

# separator = " | "                           # we called the string separators for it to be clear how join is used.
# output = separator.join(flowers)
# print(output)

# join is a string method and we start with a string (" | ")
# join is a method of the "str" class and the separator is a string.
# in the output, each of the flowers has been joined into a single string with " | " (space-bar-space) between each flpwer.

##      JOIN METHOD ---->   It creates a string from a list, and separates each item with the string that its called on.
# print(", ".join(flowers))
###     ALL THE ITEMS IN THE ITERABLE MUST BE STRING IF WE WANT TO JOIN THEM.
###     Join cannot join "ints" to the string that it produces.
separator = " | "
output = separator.join(flowers)
print(output)

print(", ".join(flowers))       # using a string literals.