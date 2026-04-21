def get_expression():
    return input("> ").strip()

def show_result(result):
    print(f"{result}")

def show_help():
    print("""
NAME
    calculator - simple interactive arithmetic calculator

SYNOPSIS
    <number> <operator> <number>
    <operation> <number> [additional arguments]

DESCRIPTION
    A simple terminal-based calculator supporting basic arithmetic
    operations and selected mathematical functions.

OPERATIONS
    +       addition
    -       subtraction
    *       multiplication
    /       division
    ^       exponentiation

    sqrt    square root
    log     logarithm (default base 10)

SYNTAX
    Binary operations:
        <a> <operator> <b>

    Unary operations:
        sqrt <a>
        log <a> [base]

EXAMPLES
    2 + 3
    10 / 2
    2 ^ 8
    sqrt 16
    log 100
    log 8 2

COMMANDS
    help    display this help message
    exit    quit the program
""")