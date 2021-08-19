# a = b = c = d = e = f = 42
# print(c)
#
# x, y, z = 1, 2, 76         #### this is called unpacking a tuple
# print(x)
# print(y)
# print(z)
# # this is very useful in all sorts of situations.
# print()
# print("unpacking a tuple")
# data = 1,2,76              #### data represents a tuple
# x, y, z = data      # data is bound to a tuple
# # these three (x,y,z) are variables. that each get a value from a the data tuple.
# print(x)
# print(y)
# print(z)

# print("unpacking a list")
# data_list = [12,13,14]
# p,q,r = data_list
# print(p)
# print(q)
# print(r)
#
# # data_list = [12,13,14]
# # data_list.append(15)          # error: --- too many values to unpack, expected 3.
# ## if we'd use a tuple instead of a list, that(appending) couldnt happen.
# ## and the reason for that is tuples are immutable and you cant append items to a tuple.
#
# # p,q,r = data_list
# # print(p)
# # print(q)
# # print(r)
# ##  so we can unpack the values from any sequence type.
# # but lists are mutable so if anything changes the list, our code will break.
# # you might create a list in one part of your code and then attempt to unpack it in another part.
# # if you append another item to the list before then, the code will crash.
#
# print()
                        ###### Practical uses for Unpacking TUPLES

# enumerate is a very useful function, when you need the index positions while iterating over a sequence.
