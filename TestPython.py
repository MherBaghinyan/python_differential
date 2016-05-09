from sympy import *

t = Symbol('t')
formula = "2*t + t**3 + 1"

import re
def mysplit(mystr):
    return re.split("([+-])", mystr.replace(" ", ""))

def processExpression(expr):
    if "**" in expr:
        return calculateDegreeImage(expr)

def calculateK(value, degree):
    return 

def calculateDegreeImage(expr):
    values = re.split("([**])")
    degree = values[1]
    val = values[0]
    final = 0
    for l in range(1, 5):
            final += calculateK(val, l) * calculateK(val, 5 - l)

parsedForm = mysplit(formula)

print(parsedForm)
