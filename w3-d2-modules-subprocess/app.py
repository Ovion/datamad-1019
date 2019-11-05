
import sys
#print(sys.path)

from fn.calculadora import calcula, Operators
from fn.ops import suma

if __name__=="__main__":
    print("Script principal")
    print(calcula(Operators.SUMA,5,5))
    print(suma(5,5))