# computer_parts = ["computer",
#                   "monitor",
#                   "keyboard",
#                   "mouse",
#                   "mouse mat"
#                   ]
# for part in computer_parts:
#     print(part)
# print()
# print(computer_parts[2])    # Indexing list --> 2nd item in the parts list.
# print()
# print(computer_parts[0:3])  # Slicing list --> printing parts from 0 to 3(not including)
# print()
# print(computer_parts[-1])   # Negative indexing list --> starts from the end of the list
# print()
# Its not surprising that indexing and slicing works the same with a list as it did with a string,
# because they are both SEQUENCE types.
# There is one big DIFFERENCE between STRINGS and LISTS:
# Strings are immutable --> meaning they cannot be changed
# Lists are mutable --> meaning you can change the contents of a list.

computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

print(computer_parts)

# computer_parts[3] = "trackball"
print(computer_parts[3:])
# basically we are printing out the value from position 3 till the end of the list
# computer_parts[3:] = "trackball"    # this prints out each letter in the trackball separately.
computer_parts[3:] = ["trackball"]    # this way it prints inside the list
print(computer_parts)

