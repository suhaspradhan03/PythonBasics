numbers = [1, 45, 31, 12, 60]       # (i) List - enclosed in "[]"
                                    # (ii) Sequence type.
for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
# The above code works but it isnt so friendly
# so we use else
else:
    print("these numbers are okay")
