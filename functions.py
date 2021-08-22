# def multiply(x, y):
#     # function names follow the same rules as variable names.
#     # they are written in lower case and must not start with a digit.
#     # after the function name we have opening and closing parentheses.
#     result = x * y
#     return result
#
#
# def is_palindrome(string):
#     # backwards = string[::-1]        # slice on the string
#     # return backwards == string      # this will evauate to true or flase and thats the answer that this function will return
#     return string[::-1].casefold() == string.casefold()
#
# #
# # def palindrome_sentence(string):
# #     return string[::-1].isalpha() == string.isalpha()
#
#
# def palindrome_sentence(sentence):
#     string = ""
#     for char in sentence:
#         if char.isalnum():
#             string += char
#     print(string)
#     # return string[::-1].casefold() == string.casefold()
#     return is_palindrome(string)
#
#
# #
# # answer = multiply(10.5, 4)
# # print(answer)
# #
# # # STRUCTURE of this function -->
# #
# # # starts with the python keyword def(-->define)
# # # thats followed by the name of the function(multiply())
# # # all function definitions have () after the function name.
# # # we can also define parameters inside the ().
# # # A function definition starts a new block, so we have to indent the body of the function.
# # # the style convention is to have 2 blank lines after calling a function
# # forty_two = multiply(6, 7)
# # print(forty_two)
# #
# # print()
# # for val in range(1, 5):
# #     two_times = multiply(2, val)
# #     print(two_times)
#
# # Palindrome is a word that reads the same backwards as forwards
# # word = input("please enter a word to check: ")
# # if is_palindrome(word):
# #     print("'{}' is a palindrome".format(word))
# # else:
# #     print("'{}' is not a palindrome".format(word))
#
# sentence = input("please enter a sentence to check: ")
# if palindrome_sentence(sentence):
#     print("'{}' is a palindrome sentence".format(sentence))
# else:
#     print("'{}' is not a palindrome sentence".format(sentence))
print()

### 07/07/2021 --
# 10/07/2021


def multiply(x: float, y: float) -> float:
    """
    for multiplying two values inside '()' . get the type `int`
    :param x: First number(integer) given in the parentheses
    :param y: second number(integer) given in the parentheses
    :return: the multiply the integers within the parentheses
    """
    result = x * y
    return result


def divide(x: float, y: float) -> float:
    result = x // y
    return result


def is_palindrome(string: str) -> bool:
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    string = ""     #empty string
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the `n` th fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))          # control + J


# # word = input("please enter a word to check: ")
# # if palindrome_sentence(word):
# #     print("'{}' is a plaindrome".format(word))
# # else:
# #     print("'{}' is not a plaindrome".format(word))
# print(multiply.__doc__)
# answer = multiply(18, 3)
# print(answer)

# p = palindrome_sentence()
