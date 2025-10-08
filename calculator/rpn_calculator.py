import typing
from typing import Union, Callable, TypeVar
import math
import inspect as inspect
from typing import Union, TypeVar
UnaryIntFunc = Callable[[int], int]
BinaryIntFunc = Callable[[int, int], int]
RPNToken = Union[int, BinaryIntFunc]

N = TypeVar('N', int, float) # A numeric type allowed to be either an int or a float

def add(a: N, b: N) -> N:
    """
    A generic function that takes either two ints or two floats, and returns the sum.

    The return type will be the same as the call type. Mixing the argument types should
    be rejected by a type checker, but mypy will actually allow an int in place of a float.
    """
    return a+b

def sub(a:int,b:int)->int:
    return a-b

def mul(a,b): return a*b;

def div(a: int, b: int) -> float:
    return a / b

def intdiv(a, b) -> int: return a//b

def pow(a,b):
    r=a**b
    return(r)

def gcd(a: int, b: int):
    """
    Calculates the greatest common divisor of two integers a and b.
    """
    while b:
        a,b=b,a%b
    return abs(a)

def lcm(a, b):
    """
    Calculates the least common multiple of two integers a and b.
    """
    # FIXME: why not just math.lcm?
    if ((a == 0) or (b == 0)):
        return 0  # LCM of any number and 0 is 0.

    return abs(a * b) // gcd(a, b)

def fact(a: int) -> int:
    return math.factorial(a)


def rpn(tokens: list[RPNToken]) -> int:
    """
    Interprets a list of tokens in Reverse Polish Notation.

    Tokens can either be integers or callable functions.
    """
    # The stack of integers yet to be used
    stack = []

    # For each token in our list of RPN tokens
    for token in tokens:
        # If the token is a function (or any callable)
        if callable(token):
            # Determine how many arguments the function needs
            num_args = len(inspect.getfullargspec(token).args)
            # If there are too few remaining items on the stack, raise an error
            if len(stack) < num_args:
                raise ValueError(f"Not enough operands for function '{token.__name__}'")

            # Pop the required number of function arguments from the stack, which will collect them reverse order, and then reverse the list
            args = [stack.pop() for token in range(num_args)][::-1]

            # Call function, push the result back onto the stack
            stack.append(token(*args))
        else:
            stack.append(token)

    # We need a single output value, so after looping there should only be one element in the stack
    if len(stack) != 1:
        raise ValueError("Malformed RPN expression!")

    return stack[0]

token_map: dict[str, RPNToken] = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "//": intdiv,
    "**": pow,
    "gcd":gcd,"lcm":lcm,
    "!": fact,
}

def rpn_interpreter(input_str) -> int:
    token_strs: [str] = input_str.split(" ")
    tokens: list[RPNToken] = [token_map[t] if t in token_map else int(t) for t in token_strs]
    return rpn(tokens)


def main() -> None:
    rpn_str: str = None
    while rpn_str != "exit":
        rpn_str = input("Enter RPN calculation to compute: ")
        try:
            print(f"  {rpn_str} = {rpn_interpreter(rpn_str)}", "\n")
        except ValueError:
            print("Invalid RPN input!")
if __name__=="__main__":
    main()
