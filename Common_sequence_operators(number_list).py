# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# # using min and max
#
# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# # using len
# print()
# print(len(even))
# print(len(odd))
# print()
#
# # using .count
#
# print("Mississippi".count("s"))

# 28/06/2021

## common sequence operators

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# # print(id(even))
# #using min and max
# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
# #len returns the no. of items in the sequence
# # for a string, that would be the number of characters in the string.
# # for a list, its the number of items.
# print()
# print(len(even))
# print(len(odd))
#
# print()
# print("mississippi".count("iss"))
# the sting 'iss' will appear twice in mississippi


## # when we call a method we tell it which object its called on
## even.append(10)
## # s.append(x) --> 's' here is the list(even), .append is the method, 'x' is the value that we use to append to the list.
## # even is the variable in which we append the value 10(object).
## print(id(even))


                        ## sorting lists

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# even.extend(odd)        # this is used to combine two lists
# print(id(even))             # we send odd through the list even using the extend method
# print(even)
# another_even = even
# print(another_even)
# print(id(another_even))
# # even.sort()             # this is used to sort items in the list
# # print(even)
#
# even.sort(reverse=True)     # this is used to reverse the sorted list
# print(id(even))
# print(even)
# print(another_even)
# print(id(another_even))

                                                ### CREATING LISTS

empty_list = []     # we can create a list using list literal
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
# creating a list by concatenating existing lists

# numbers = even + odd
# print(numbers)
# # print("trying enumarate function with value and range")
# # for value, range in enumerate(numbers):
# #     value += 1
# #     print(value,range)
# print()
# sorted_numbers = sorted(numbers)        #(numbers,reverse=True) in order to get values in decending order.
# print(sorted_numbers)               # this consists of a sequence of ints
# print(numbers)
#
# #this consists a sequence of characters
# digits = sorted("432985617")        # the digits lists contains strings
# print(digits)                       # all the digits return as strings in the list
# # digits list that is produced consists of a sequence of strings in the list.
# # print()
# # print("printing value and range for a list containing a string of numbers")
# # for v , r in enumerate(digits):
# #     v += 1
# #     print(v, r)
# print()
# # using list
# digit = list("432985617")       # list is a class initializer but we are using it as a function for now
# print(digit)
#
# # more_numbers = list(numbers)      # copying list using "list" function
# # more_numbers = numbers[:]         # copying list using "slice" method
# more_numbers = numbers.copy()        # copying list using "copy" method\
# # this time we use parentheses to call the method.
# print(more_numbers)
# print(id(numbers))
# print(id(more_numbers))
# print(numbers is more_numbers)      # givens a boolean value as a result.(False here) used for checking if characters/numbers are same list or not.
# # but its a new list here so it tells us that the lists are different but the items within the lists are the same.
# print(numbers == more_numbers)      # The value is True because they both contain the same items/objects in the same order.

                                    ### NESTED LIST AND CODE STYLE

# empty_list = []
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even, odd]       # two separate lists will be created, inside another list.
# print(numbers)
# # this example uses a for loop to print each list, then an inner for loop to print the contents of the inner lists.
#
# for number_list in numbers:             # in the outer loop we iterate over numbers
#     print(number_list)
# # the numbers_list is a var and the numbers(list) is a iterator.
#     for value in number_list:
#         print(value)
# the value is bound to each of the even numbers, first time around the loop, then to each of the odd numbers.
# this is an IMPORTANT CONCEPT

# another example -- this will show how to create a nested list using a literal.

empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]       # two separate lists will be created, inside another list.
print(numbers)
# this example uses a for loop to print each list, then an inner for loop to print the contents of the inner lists.

for number_list in numbers:             # in the outer loop we iterate over numbers
    print(number_list)
    # the numbers_list is a var and the numbers(list) is a iterator.
    for value in number_list:
        print(value)
