str1 = "he's "
str2 = "probably "
str3 = "pining "
str4 = "for the "
str5 = "fjords "

print(str1 + str2 + str3 + str4 + str5)
print()
print("hello " * 5)     # The string("hello ") can be rewritten in the same line 5 times
# This is called string multiplication.
#                  0          1          2          3          4
comp_parts = ("computer", "monitor", "keyboard", "mouse", "mouse mat")
#             012345678   01234567   012345678   012345   0123456789
# Every separate word here is a sequence with a index number
# And Ever character in each sequence has their own separate index numbers.
print(comp_parts[1])        # index number 1 --> monitor
print(comp_parts[1][0])     # Calls the item(index) number [1] and the sub index [0] --> which is "m"
print(comp_parts[4])        # index number 4 --> Mouse mat
print(comp_parts[4][7])     # calls item(index) number [4] and the sub index [7] --> which is "a"
# Not all sequence types can be multiplied or concatenated.
# OPERATOR PRECEDENCE is APPLIED always
print("help me " * (5 + 4))       # operator Precedence is applied here. which is why "( )"
# statements in the "( )" are first completed because of operator precedence
print("help " * 5 + "4")          # here "4" is a string value as it is only being printed
# so string printing will take place.
# there is also an operator to check if ONE STRING IS THE SUB-STRING OF ANOTHER
# To do this we check if one thing is in another.
print()
today = "sunday"
print("sun" in today)       # True
print("day" in today)       # true
print("suda" in today)      # False --> the whole sentence should be in a sequence.
print("thu" in today)       # False
print("fri" in today)       # False
print()
