# for i in range(1, 13):
#    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
# In the above statement we are using replacement field and .format
# In range of 1 to 13(not including 13)
# The cubed part has a digit width of 4
## VERY Important --> We can use Shift + tab to get the statement indented.
## Once the block of code is completed we have to remove the indentation by pressing backspace
## so that the block of code ends.
# print("*" * 80) # here this is not part of the block which is why we get the result in the end of the code.
#    print("*" * 80)
# Here the print statement is a part of the block code because it is indented. which means that the result is different.
## So what happens is since this is a part of the block. the whole for loop runs 12 times and prints this * along with it.
print()
print(" IF & ELIF & ELSE Statements")
print()
name = input("enter your name")
# age = input("how old are you, {0}? ".format(name))
# print(age)
# print(type(age))
age1 = int(input("how old are you, {0}? ".format(name)))    # In the code you can find the difference
print(age1)     # We changed the data type of age from <class 'str'> to <class 'int'>
# print(type(age1))   # we did this by putting int in front of input to change the data type of the
# string from str to int.
print()
# print("Using if and else statements")
# print()
if age1 > 21:
    print("Using IF statement")
    print("you are old enough to vote {0}".format(name))
    print("please put an X in the box")
elif age1 == 21:
    print("Using ELIF statement")
    print("you just got the right to vote {0},so make sure you know who your voting for at this age \n'{0}',\n'{1}'".format(name, age1))
# We us the KEYWORD "if" followed by the condition, in this case, age1 >= 21.
# we use replacement field and .format in this statement for easier result
else:
    print("using ELSE statement")
    print("""You are not old enough to vote.
    please come back in {0} years""".format(21 - age1))
# We use the KEYWORD "else" followed by the condition, keyword "if" condition does
# not apply then it comes to the KEYWORD "else".
# Here "ELSE" cannot be a part of the "IF" indentation.(there will be an error if it is a part)
# we use replacement field and .format. In dot format we put another condition saying that
# (21 - age1) this is a condition within the .format to give an answer which is appropriate.
# In Mac --> Command and forward slash ' / ' to make a few lines into comments
print()
## Doing this same above code in the other way around
## It doesnt matter which way the code is written.
# if age1 < 21:
#     print("""You are not old enough to vote.
#     please come back in {0} years""".format(21 - age1))
# elif age1 == 21:
#     print("you just got the right to vote {0},so make sure you know who your voting for at this age '{1}'".format(name, age1))
# # here im using the elif statement, cannot be used after the else statement.
# # should always be used in between the if and else statements.
# # in this ELIF statement, i used 2 replacement fields and .format in order to understand the useage of all these things better.
# # In .format i added name and age1 separately.
# # The whole point of this (debugger)ELIF statement is to understand how to use code blocks, if, else and elif statements.
# else:
#     print("you are old enough to vote {0}".format(name))
#     print("please put an X in the box")
# all the above are the actual statements that can be used.
