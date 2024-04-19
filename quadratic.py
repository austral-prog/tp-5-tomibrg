# Replace the "ANSWER HERE" for your answer
import math
def roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant == 0:
        root_0 = (-b + discriminant)/(2*a)
        return f'({root_0})'
    elif discriminant > 0:
        root_11 = (-b + math.sqrt(discriminant))/(2*a)
        root_12 = (-b - math.sqrt(discriminant))/(2*a)
        return f'({root_11}, {root_12})'
    else:
        return '( )'

def value_y(a, b, c, x):
    y = a*x**2 + b*x + c
    return y


def to_string(a, b, c):
    if a == 0 and not b ==0 and not c ==0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0 and not c == 0 and not a == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif c == 0 and not b == 0 and not a == 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    elif a == 0 and b == 0 and not c == 0:
        return f"f(x) = {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    if a == 0:
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {2*a} * X"
    else:
        return f"f'(x) = {a * 2} * X + {b}"
    elif b == 0:
        return f"f'(x) = {2*a} * X"
    else:
        return f"f'(x) = {a * 2} * X + {b}"
