# result = True       # here we have two variables, both of them are bound to the
# another_result = result     # value True.
# print(id(result))       # We have printed out the ID of those variables
# print(id(another_result))
# # so if bool values could be changed, then changing the values should mean that the
# # ID doesnt change. so lets see if thats the case.
# result = False
# print(id(result))
# we got a different id for a result with the code that we have just added.
# Because bools are immutable, we werent able to change the value of True.
# so what pythons done instead, is rebound the result to a new value - False.

# result = "correct"
# another_result = result
# print(id(result))
# print(id(another_result))
#
# # Now we can use Augmented assignment to concatenate more characters to the end
# result += "ish"
# print(result)
# print(id(result))
# print(id(another_result))
# so if we could mutate(concatenate) the string, then the value is bound to
# would change. the ID should remain the same if that happened. and its NOT.
# as you can see, result now has a different id.
# notice that the id of the result has change, but another_result still has the same id that it had.


## Because strings are IMMUTABLE, Python couldnt change the string correct.
## what it did instead was create a new string and bind the name result to
## this new string.


# 27/06/2021

# result = True
# another_result = result
# print(id(result))
# print(id(another_result))       # both variables have the same id,bound to the same values
#
# result = False
# print(id(result))   #we get a different id. # Coz bools are immutable we were not able to change the value of true
# what python has done instead is rebound the result to a new value - False.

# result = "correct"
# another_result = result     # variables both have the same id
# print(id(result))
# print(id(another_result))
# # using Augmented assignment
# result += "ish"             # here id of the result has changed but another_result is still the same
# print(id(result))
# print(id(another_result))
# # this means that only the result will change its memory location(kind off)
# # but the memory location of another_result will be the same
