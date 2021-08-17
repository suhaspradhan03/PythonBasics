age = 24            # integer
print("My age is " + str(age) + " years")
# Using the "str" string function helps us to basically coerce an integer into a string.
# ** Instead of using str function we use replacement fields and the dot format method **
print()
print("My age is {0} years".format(age))        # {0} --> this is the replacement field.
# " .format() --> decides what is to be placed in the replacement field
print("above statement is using 'replacement fields' and 'dot format'.")
print()
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(31, "jan", "mar", "may", "jul", "aug", "oct", "dec"))
print()
# The above statement can also be written in a different format
print("There are {0} days in jan, mar, may, jul, aug, oct, dec".format(31))
print("Above statement is written in a much more simple format")
# THE REPLACEMENT FIELDS CAN BE USED MORE THEN ONCE AND
# THEY DON'T HAVE TO BE IN THE SAME ORDER
print()
print("jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
# Here different replacement fields are put in different order.
# The . format decides which number goes to which replacement field. just like indexes.
print()
print("""jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30 , 31))
print('The above statement is written using """ quotes.')
print()
# print("test -- 24th May 2021")
# name = "abcdefghijklmnopqrstuvwxyz"
# print(name[18] + name[20] + name[7] + name[0] + name[18])
# print(name[9] + name[14] + name[18] + name[7] + name[20] + name[0])
# print("test successful --> can concatenate using indexing of random letters")
# print()
