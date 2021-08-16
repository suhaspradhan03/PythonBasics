print("1)  'Basics of slicing'  ")
#                   1
#         012345678901234
parrot = "Norwegian Blue"
print()
print(parrot[0:6])      # norweg (upto but not including 6)
print(parrot[3:5])      # we (upto but not including number 5)
print(parrot[0:9])      # Norwegian (upto but not including 9)
# there is also another way to write the above code.
print(parrot[:9])       # Norwegian (upto but not including 9)
# In this above statement the start value is not given because the python knows that it should start at
# The first index number which is why we dont have to put a specific start value the " : " is sufficient.
print()
print("basic 'in video mini-mini challenge' -- print word 'blue'.")
print(parrot[10:14])
print(parrot[10:])
# In this code we leave off the "final" value as python will stop when it reaches that final value.
print()
print("""Most important - "If we do not put a ':' in the middle while slicing numbers then the
slicing process becomes an indexing process".""")
print()
print(parrot[:6])
print(parrot[6:])
print()
print(parrot[:6] + parrot[6:])      # The value starts at [:n] and ends at [n:]
# which means these values will have a proper n value
print(parrot[:])                    # means the whole sting value will be give.
print()
print()
print("2) SLICING WITH NEGATIVE NUMBERS")
print()
print(parrot[:])
print(parrot[-14:-8])               # Norweg
# Here the string prints the statement from -14 to -8 (upto -8 but not including -8)
print(parrot[-11])
print(parrot[-10])
print(parrot[9])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
# This is how negative index's can be written
print()
print("Example to understand negative indexing better")
egg = "cats and dogs"
print(egg[-8:-5])
print(egg[-4:-1])
print(egg[-13:-9])
print(egg[-13:14])       # This is how we can add the last letter in the negative index as well.
# print("test")
# print(egg[0:8])
# print(egg[-8:-1])
print()
print("3) USING A STEP IN SLICE ")
#                   1
#           012345678901234     [POSITIVE INDEX]
# parrot = "Norwegian Blue"
#       (-) 43210987654321 (-)  [NEGATIVE INDEX]
#            (-)1
print()
print(parrot[0:6:2])        # Nre
# Starts from INDEX 0, i.e, N. Extracting all values upto but not including Index 6, i.e, i. In steps of 2.
print(parrot[0:6:3])        # Nw
# Starts from INDEX 0, i.e, N. Extracting all values upto but not including Index 6, i.e, i. In steps of 3.
print()
#number = "9,223,372,036,854,775,807"
#print(number[1::4])
# The above illustrates using a step in slices.
# It starts at position 1, i.e, the first " , " and its slicing every 4th character.
# The list extends all the wayto the end of the string because we have omited the stop value.
number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)
print()
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
# 7 values that have been extracted from the string and now are bound to the number variable .
# THESE ARE STILL NOT TAUGHT, SO I CAN UNDERSTAND THIS LINE LATER.
print()
print("4) SLICING BACKWARDS")
print()
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
# The index starts at 25, stop value at 0 and a step of -1
# Here the value is upto 0 but does not include 0
print(backwards)
# OR
backwards = letters[25::-1]     # start value 25, stop value isnt specified which means
# \ it will go on till the end of the string, step value -1.
print(backwards)
# OR
# backwards = letters[::-1]
# print(backwards)
print("mini challenge -- produce qpo , edcba , \
slice sting to produce last 8 \
characters in reverse")
print(letters[-10:-13:-1])  # Start value -10, stop value -13 and the slice(step) value is -1.
print(letters[-22::-1])     # start value -22, stop value isnt specified and the slice(step) is -1.
print(letters[-1:-9:-1])    # start value -1, stop value -9 and the slice(step) value is -1.
# Step(slice) value -1 means the whole string is counted in the sequence of -1.
print(letters[-11:-19:-1])
# The starting number should always start with the highest value --> -1 is the highest value in negative index.
print(letters[16:13:-1])
print(letters[4::-1])   # Easiest way to include the beginning of the string is to omit the stop value
print(letters[25:17:-1])
print()
print(" ---- The End for SLICING ---- ")