# panagram = "the quick brown fox jumps over the lazy dog"
##          split method --> splits the string up into words.
# words = panagram.split()        # we leave the () to call the method.
# print(words)
## the result we get is a list of words that are seperated by commas and everything is a string value.
# we get a list containing all the words in the string.
# we didnt provide any arguments to split so it splits to whitespace.

# whitespace includes things like tabs and newlines, as well as a few other characters, including the space.


# panagram = """the quick brown
# fox jumps\tover
# the lazy dog"""
#
# words = panagram.split()
# print(words)
#
# numbers = "9, 223, 372, 036, 854, 775, 807"
# print(numbers.split(","))       # we got a list here containing each of the numbers from our numbers string.


# panagram = "the quick brown fox jumps over the lazy dog"
# words = panagram.split()    # leaving the parantheses in so we are calling the method
# print(words)
#
# print()
#
# panagram2 = """the quick brown
# fox jumps\tover
# the lazy dog"""
#
# words2 = panagram2.split()
# print(words2)

# use a for loop to replace all the strings in that list with integer values

numbers = "9, 223, 372, 036, 854, 775, 807"
# print(numbers.split(","))       # we got a list here containing each of the numbers from our numbers string.
print(numbers)
print(id(numbers))
print(type(numbers))

splitting_numbers = numbers.split(",")
print(splitting_numbers)
print(id(splitting_numbers))
print(type(splitting_numbers))

replace = []
for token in splitting_numbers:
    replace.append(int(token))
print(replace)
print(id(replace))
print(type(replace))

a,b,c,d,e,f,g = replace
result = a+b+c+d+e
print(result)
result2 = result - f - g
print(result2)

print(result2,"<-- this is the final result, --> ", f, g, "Are the values that should be subtracted", "Here we use the sep keyword arg in print --> '|'.",sep=" | ")

