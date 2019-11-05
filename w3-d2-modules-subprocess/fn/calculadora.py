
from .ops import suma, resta

class Operators():
    SUMA="suma"
    RESTA="resta"

def calcula(op, left, right):
    if op == "suma":
        return suma(left,right)
    elif op == "resta":
        return resta(left,right)
    else:
        raise ValueError("Cannot operate with operator: {}".format(op))

print("Soy el",__name__)