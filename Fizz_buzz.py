def fizz_buzz(n: int) -> str:

    """
        play FIZZ BUZZ

    if the number is divisible by `3`, you say `fizz`
    if the number is divisible by `5`, you say `buzz`
    if it's divisible by both `3` and `5`, you say `fizz buzz`

    :param n: n (int) which is then converted to strings
    :return: numbers in the string format

    """

    if n % 15 == 0:
        return "fb".casefold()
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


input("play Fizz Buzz. Press enter to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("players turn: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, You reached {}".format(next_number))


# print(fizz_buzz.__doc__)
# for i in range(1, 101):
# print(fizz_buzz(i))
