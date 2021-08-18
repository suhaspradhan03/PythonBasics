# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
                           #13   14   15   16    17(index numbers)
# imagining a scenario where our caliberation equipment
# for first two values and last two values are faulty.
# del data[:2]        # upto but not including 2
# print(data)         # first two values are deleted
# # del data[16:]       # no end specified so till the end of the list
# # The index value of the list changes so,
# del data[14:]       # this is the new value of the list
# print(data)
# this is the code we can use if we delete the code manually
# When we automate this code that is when the problem starts.

# assume we already analyzed the data and
# the min and max should be in between
# 100 & 200 respectively

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
#
# min_valid = 100
# max_valid = 200
# when we use a for loop to remove the outlying values
# and that's when we will get a problem
# and the cause isnt obvious until we have seen it.
# for index, value in enumerate(data):
#     # print(index, value)
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
# print(data)

                            ## safely removing values from a list

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]                # test case -> outlying values at both high and low cases
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]                          # test case -> outlying values at only low end
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]                # test case -> outlying values at only high end
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]                          # test case -> no outlying values
# data = [4, 5, 1104, 1105, 1110, 1120, 1130, 1130, 1150,
#         1160, 1170, 1183, 1185, 1187, 1188, 1191, 1350, 1360]       # test case --> only outlying values
# data = []                                                           # test case --> empty data set
# an empty list is correct, thats only with realted to our code
# when performing a statistical analysis and removed all or most values from your data, then somethings obviously not right.
# outlying values are one that deviate from the norm by an unacceptable amount.
# if most of the values are outlying then you havent identified outlying values correctly.
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]
min_valid = 100
max_valid = 200

# process the low values in the list

stop = 0            # we initialize stop to 0
for index, value in enumerate(data):
    if value >= min_valid:              # inside the loop we keep incrementing the stop value,
        # until we find a value that shouldnt be deleted
        stop = index
        break

print(stop)         # debugging purposes
del data[:stop]     # we delete the slice from the beginning of the list, upto but not including stop.
# remember the slice extends up to but not including the stop value.
# the value we stopped at wont be deleted
print(data)

                                        ## process the high values in the list

start = 0

# now we need a for loop and we want to work backwards,
# which means that we will start the
# index position 1 less than the length of the list --> len(data) - 1; (2 becomes 1, 1 becomes 0)
for index in range(len(data) - 1, -1, -1):          # we cannot use 0, last value in a range or slice isnt included.
    # if we find a value that is within the valid range -- value >= 200(max_valid) --> we can break the loop.
    if data[index] <= max_valid:                    # this gives us the start value of the position of the last item that we want to keep.
        # we have the index of the last item to keep.
        # set 'start' to the position of the first
        # item to delete, which is 1 after 'index'
        start = index + 1
        break
# so if we use 0 here the first item in the list wont be included.
# -1 will be the stop value in this part of the code
# to work backwards, we use a step of -1. we will be iterating backwards, that is, 15 to 0.
### if we find a value that is within the valid range -- value >= 200(max_valid) --> we can break the loop.
print(start)        # for debugging
del data[start:]        # slice includes everything from the start value to the end of the list.
print(data)             # this includes the value 191 and that isnt what we want
# we need the data to start deleting values at position 14 and not from the position 13.
# which means that -->              del data[start + 1:]     (or)    start = index + 1
# the purpose of our for loop is to identify the first item that the code must delete.
# it sets start to the position to start deleting from, rather than from the position of the last item we want to keep.
# cleaner to have the correct start position when the loop terminates, having to alter start after the loop is a bit clumsy
# and it is something that is easy to forget
