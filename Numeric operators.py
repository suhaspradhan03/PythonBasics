print("Basic python arithmetic operators")
a = 12                                  # strictly speaking both 12 and 3 are also expressions
b = 3                                   # strictly speaking both 12 and 3 are also expressions
# basic python arithmetic operators

print(a + b)      # 15                  # code like (a + b) is called an expression
print(a - b)      # 9                   # all these are expression
print(a * b)      # 36
print(a / b)      # 4.0 (float - with decimal point)
print(a // b)     # 4 (int - without decimal point)
# here '' // '' means Integer Division, Rounded down toward minus infinity
print(a % b)      # 0 modulo: The remainder after integer division.
print()
print()
for i in range(1, a // b):      # For loop should begin with a " : "
    # Here i is not an expression as it is being bound to the range(1, a // b):
    # Here " // " means integer division.
    # Here integer division is done[float cannot be used here.. only int should be used]
    print(i)
    print()
    # Here when the print is in for loop then the answer gets a change
# there is a line in between every range number.
for j in range(1, 11):
    print(j)
print()
# Here j is not an expression it is being bound to the range (1, 11):
# Here after the whole answer is done then a blank line will be left
for k in range(3, 9):
    print(k)
# THE MOST IMPORTANT PART -- YOU CANNOT USE A FLOAT (EX:- 4.0) IN PLACE OF AN INTEGER (EX:- 4).
# TEST
# Q1. You have a shop selling buns for $2.40 each. A customer comes in with 15$, and would like to buy as many buns as possible.
# complete the code to calculate how many buns the customer can afford.
print()
s = 2.40   # bun_price
j = 15     # money
print(j // s)   # integer dividing as we cannot do float divide(normal divide
#print(s % j)    # we need to find the reminder that should be given back to the customer.
#print(s * 6)    # to reconfirm
print()
print("New Unit --> Operator precedence")
print()
print(a + b / 3 - 4 * 12)
print(a +(b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b ) /3 - 4) * 12)

print()

print(a / (b * a) / b)
