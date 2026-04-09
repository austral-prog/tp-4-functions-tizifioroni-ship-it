# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discrminante = b**2 - 4*a*c
    r1 = (-b + discrminante**0.5) / (2*a)
    r2 = (-b - discrminante**0.5) / (2*a)
    if discrminante < 0:
        return "( )"
    elif discrminante > 0:
        return f"({r1}, {r2})"
    else:
        return f"({r1})"

def value_y(a, b, c, x):
    valor_y = a*x**2 + b*x + c
    return valor_y


def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):
    if a == 0 and b == 0:
        return f"f'(x) = 0"
    elif a == 0: 
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {2*a} * X"
    else:
        return f"f'(x) = {2*a} * X + {b}"