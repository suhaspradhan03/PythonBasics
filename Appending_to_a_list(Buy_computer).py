# here we will allow the customers to choose which parts they need when buying a computer.
# we will just offer 5 items for sale.
# we saw how to write a simple menu and this is kind of the same.
# This program will start off very similar to that.

# Now we need a variable to store the customers choice and
# an empty list to add items to.

#current_choice is an empty list as the users inputs will be given from this.
# current_choice = "-"    # using while statement to get out of the code
# computer_parts = []     # creating an empty list - list to store the items
#
# while current_choice != '0':
#     if current_choice in "123456":
#         print("adding {}".format(current_choice))
#         if current_choice == '1':
#             computer_parts.append("computer")
#         elif current_choice == "2":
#             computer_parts.append("monitor")
#         elif current_choice == "3":
#             computer_parts.append("keyboard")
#         elif current_choice == "4":
#             computer_parts.append("mouse")
#         elif current_choice == '5':
#             computer_parts.append("mouse mat")
#         elif current_choice == "6":
#             computer_parts.append("hdmi cable")
#     else:
#         print("Please add options from the list below: ")
#         print("1: computer")
#         print("2: monitor")
#         print("3: keyboard")
#         print("4: mouse")
#         print("5: mouse mat")
#         print("6: hdmi cable")
#         print("0: to finish")
#
#     current_choice = input()
# print(computer_parts)

# available_parts = ["computer",
#                    "monitor",
#                    "keyboard",
#                    "mouse",
#                    "mouse mat",
#                    "hdmi cable"
#                    ]
# current_choice = "-"
# computer_parts = []
#
# while current_choice != '0':
#     if current_choice in "123456":
#         print("adding {}".format(current_choice))
#         if current_choice == '1':
#             computer_parts.append("computer")
#         elif current_choice == "2":
#             computer_parts.append("monitor")
#         elif current_choice == "3":
#             computer_parts.append("keyboard")
#         elif current_choice == "4":
#             computer_parts.append("mouse")
#         elif current_choice == '5':
#             computer_parts.append("mouse mat")
#         elif current_choice == "6":
#             computer_parts.append("hdmi cable")
#     else:
#         print("Please add options from the list below: ")
#         for part in available_parts:
#             print("{0}: {1}".format(available_parts.index(part) + 1, part))
# used string formating and replacement fields there, to display the index number and the part.
# adding one to the index and thats because indexs start at zero.

        # print("1: computer")    # we can replace this with a for loop
        # print("2: monitor")
        # print("3: keyboard")
        # print("4: mouse")
        # print("5: mouse mat")
        # print("6: hdmi cable")
        # print("0: to finish")

#     current_choice = input()
# print(computer_parts)

                        # ENUMERATE FUNCTION

#THI IS USED TO MAKE THE INDEXING OF THE CODE MORE EFFICIENT.
# available_parts = ["computer",
#                    "monitor",
#                    "keyboard",
#                    "mouse",
#                    "mouse mat",
#                    "hdmi cable"
#                    ]
# current_choice = "-"
# computer_parts = []
#
# while current_choice != '0':
#     if current_choice in "123456":
#         print("adding {}".format(current_choice))
#         if current_choice == '1':
#             computer_parts.append("computer")
#         elif current_choice == "2":
#             computer_parts.append("monitor")
#         elif current_choice == "3":
#             computer_parts.append("keyboard")
#         elif current_choice == "4":
#             computer_parts.append("mouse")
#         elif current_choice == '5':
#             computer_parts.append("mouse mat")
#         elif current_choice == "6":
#             computer_parts.append("hdmi cable")
#     else:
#         print("Please add options from the list below: ")
#         for number, part in enumerate(available_parts):
#             # Now we have two variables on the for loop
#             print("{0}: {1}".format(number + 1, part))
#             # we have completely replaced the previous code with number.
#
#     current_choice = input()
# print(computer_parts)

                # IMPROVING OUR CODE
#
# available_parts = ["computer",
#                    "monitor",
#                    "keyboard",
#                    "mouse",
#                    "mouse mat",
#                    "hdmi cable",
#                    "dvd drive"
#                    ]
# # valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
# valid_choices = []
# for i in range(1, len(available_parts) + 1):
#     valid_choices.append(str(i))
# print(valid_choices)
# print()
# current_choice = "-"
# computer_parts = []
#
# while current_choice != '0':
#     if current_choice in valid_choices:
#         print("adding {}".format(current_choice))
#         index = int(current_choice) - 1     # we can use anything other than index here
#         users_chosen_part = available_parts[index]    #we can use anything other then chosen parts here
#         computer_parts.append(users_chosen_part)
#         # THESE 3 LINES INSTEAD OF ALL THE LINES BELOW
#         # if current_choice == '1':
#         #     computer_parts.append("computer")
#         # elif current_choice == "2":
#         #     computer_parts.append("monitor")
#         # elif current_choice == "3":
#         #     computer_parts.append("keyboard")
#         # elif current_choice == "4":
#         #     computer_parts.append("mouse")
#         # elif current_choice == '5':
#         #     computer_parts.append("mouse mat")
#         # elif current_choice == "6":
#         #     computer_parts.append("hdmi cable")
#         # elif current_choice == "7":
#         #     computer_parts.append("dvd drive")
#     else:
#         print("Please add options from the list below: ")
#         for number, part in enumerate(available_parts):
#             # Now we have two variables on the for loop
#             print("{0}: {1}".format(number + 1, part))
#             # we have completely replaced the previous code with number.
#
#     current_choice = input()
# print(computer_parts)



# IMPROVED CODE

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"
                   ]                                  # till here we got a list of parts that are available
valid_choices = []                                    # from here to the next 3 lines
for i in range(1, len(available_parts) + 1):          # we create an empty list and then add
    valid_choices.append(str(i))                      # valid choices to it.
print(valid_choices)
print()

current_choice = "-"
computer_parts = []                                   # this defines another empty list computer_parts
                                                      # which will contain the parts that the customer wants to buy
                                                      # and we are appending their items.
while current_choice != '0':
    if current_choice in valid_choices:
        print("adding {}".format(current_choice))
        index = int(current_choice) - 1     # we can use anything other than index here
        users_chosen_part = available_parts[index]    #we can use anything other then chosen parts here
        computer_parts.append(users_chosen_part)      # ones that they have chose to buy, so that ultimately contains
                                                      # the list of items that they want to purchase.
    else:
        print("Please add options from the list below: ")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
    current_choice = input()
print()
print(computer_parts)