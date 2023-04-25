# this code will help me in my math homework to find all the factors of a givin number
# please don't tell my teacher:)
# 25.04.2023
y = int(input("please enter a number to factor ?\n"))  # this is the user input integer and it is a variable.
factors = []  # we create an empty list
for i in range(1, y + 1):
    if y % i == 0:
        factors.append(i)
print(factors)
# end of code
