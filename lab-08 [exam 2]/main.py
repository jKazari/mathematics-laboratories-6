from datetime import datetime
import frontend
import utils
import parser

def main():
    start_time = datetime.now()
    history = []

    print("Simple calculator")
    print("Type 'help' for usage information, 'exit' to quit\n")

    while True:
        expr = frontend.get_expression()

        if expr.lower() == "exit":
            break

        if expr.lower() == "help":
            frontend.show_help()
            continue

        try:
            expression, result = parser.parse_expression(expr)
            frontend.show_result(result)
            history.append(expression)

        except Exception as e:
            print(f"Error: {e}")
            history.append(f"{expr} -> Error: {e}")

    filename = utils.generate_filename(start_time)
    utils.save_session(filename, history)

    print(f"Session saved to {filename}")

if __name__ == "__main__":
    main()
