# int -> full numbers
# float -> .5 number
# char -> single symbol
# string -> text or numbers taken as a text
# boolean -> true(1) or false(0)
# array -> list with a number in specific order; rock (0), jazz (1), blues (2), pop (3)
# defs: print() type()
# arithmetic +-* 
# % - modulo; the rest
# / true division; always float
# // division; always int
# print(min(arg1,arg2,arg3,argn)); print(max(arg1,arg2,arg3,argn)); print(abs(absolute number; -32 = 32))
# int/float can be called as functions and display respectively their numbers full/.5
#help(insert function)
#Functions: 
#weee
def least_difference(a, b, c):
    """This is an example of a docstring
    Return Return the smallest difference between any two numbers
    among a, b and c.
    Here you can put an example how the function works
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
print(
    least_difference(1, 10, 100),
    least_difference(5, 6, 7),
    least_difference(1, 2, 3),
    sep=' = '
)
#help(least_difference)
def greet(who=""):
    print("Hello,", who)
greet("frank")