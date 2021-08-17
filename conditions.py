# name = input("enter your name")     ## ALL CONDITIONS --  of OR & AND are written in the book
# age = int(input(f"how old are you {name}? "))
# # good = "how good?"
# # bad = "why bad?"
#
# if age >= 16 and age <= 65:
#     print("how was your day at work?")
    # input()
    # if input(good):
    #     print("what all did you do today?")
    #     input()
    # elif input(bad):
    #     print("what happened? did anyone say anything?")
    #     input()
# else:
#     print("please relax at home, you cannot work")

## SIMPLIFYING CHAINED COMPARISON

age = int(input("how old are you? "))
# if age >= 16 and age <= 65:
if 16 <= age <=65:
    print("have a good day at work")
else:
    print("enjoy your free time")
print()
print("-" * 80)
print()
# This is for " OR " Format

if age < 16 or age > 65:
    print("enjoy your free time")
else:
    print("have a good day at work")