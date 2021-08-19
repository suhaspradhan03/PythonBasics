# the_list = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# for i in range(1,100):
#     if i % 3 == 0:
#         print(i)
#     if i % 5 == 0:
#         print(i)
# print()
# for value, index in enumerate(the_list):
#     int(value)
#     value += 1
#     print(value, index)

# total = 0
# j = 1
# while j < 5:
#     total += j
#     j += 1
# print(total)
# most inmprtant situation for while loop
# when we dont know the number of loops that has to be conducted or completed

# given_list = [5, 4, 4, 3, 1]
# total2 = 0
# total3 = 0
# i = 0
# while i < len(given_list) and given_list[i] > 0:
#     total2 += given_list[i]
#     i += 1
# print(total2)

# given_list = [5, 4, 4, 3, 1, -2, -3, -5]
# # total = 0
# # for element in given_list:
# #     if element <= 0:
# #         break
# #     total += element
# # print(total)
# total = 0
# i = 0
# while True:
#     total += given_list[i]
#     i += 1
#     if given_list[i] <= 0:
#         break
# print(total)

# given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
# total = 0
# i = -1
# while given_list[i]:
#     total += given_list[i]
#     i -= 1
#     if given_list[i] >= 0:
#         break
# print(total)

                    ## sorting.py

pangram = "The quick brown fox jumps over the lazy dog"
# here we passed a variable(pangram) through sorted
letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key = str.casefold)
            #we are telling the sorted function the name of another function it should use
            # when comparing the values.
# s is missing
# we passed a string literal to sorted.
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]

names.sort()
print(names)