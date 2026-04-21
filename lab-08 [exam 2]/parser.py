import backend

def parse_expression(expr: str):
    tokens = expr.split()

    if not tokens:
        raise ValueError("Empty input")

    if tokens[0] == "sqrt":
        if len(tokens) != 2:
            raise ValueError("Usage: sqrt <number>")
        a = float(tokens[1])
        result = backend.sqrt(a)
        return f"√{a} = {result}", result

    if tokens[0] == "log":
        if len(tokens) == 2:
            a = float(tokens[1])
            result = backend.logarithm(a)
            return f"log({a}) = {result}", result
        elif len(tokens) == 3:
            a = float(tokens[1])
            base = float(tokens[2])
            result = backend.logarithm(a, base)
            return f"log_{base}({a}) = {result}", result
        else:
            raise ValueError("Usage: log <number> [base]")

    if len(tokens) != 3:
        raise ValueError("Invalid expression format")

    a = float(tokens[0])
    op = tokens[1]
    b = float(tokens[2])

    operations = {
        "+": backend.add,
        "-": backend.subtract,
        "*": backend.multiply,
        "/": backend.divide,
        "^": backend.power,
    }

    if op not in operations:
        raise ValueError("Unknown operator")

    result = operations[op](a, b)

    return f"{a} {op} {b} = {result}", result
