# number = "9,223;372:036 854,775;807"
# # separators = number[1::4]
# separators = ""         # this is equal to an empty string.
# for char in number:
#     if not char.isnumeric():        # String method -- .isnumeric():
# # .isnumeric will return true when the character is a number and false if otherwise.
# # we want to add things that arnt a digit which is why the condition becomes "if not char.isnumeric().
#         separators = separators + char
# print(separators)
#
#
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])         # These are way too advanced and we will learn about them later.

# print("FOR LOOPS EXTRACTING VALUES FROM USER INPUT")
# number = "9,223;372:036 854,775;807"
# # separators = ""        # if we dont define separators to anything then read below
# separators = ""         # this is equal to an empty string.
# # the reason we are binding separators to an empty string is because
# # First thing you'll notice is we have got warnings wherever the value of separators is used in the code.
# for char in number:
#     if not char.isnumeric():        # String method -- .isnumeric():
#         # .isnumeric will return true when the character is a number and false if otherwise.
#         # we want to add things that arnt a digit which is why the condition becomes "if not char.isnumeric().
#         separators = separators + char
# # so this is trying to take the current value of separators and append it to the char.
# # but it does not work since we have not defined the current value of separators.
# # that is because we have not bound the separators to any value.
# print(separators)
#
#
# values = "".join(char if char not in separators else " " for char in number).split()
# print([int(val) for val in values])

number = input("please enter a series of numbers using any separators you like ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

# print(separators)


values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))