def arithmetic_arranger(problems, show_results=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    for problem in problems:
        operands = problem.split()
        num1, operator, num2 = operands[0], operands[1], operands[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        line1 = num1.rjust(width)
        line2 = operator + num2.rjust(width - 1)
        dashes = "-" * width

        arranged_problems += f"{line1}    {' ' * 4} {line2}    {' ' * 4} {dashes}\n"

    if show_results:
        results = []
        for problem in problems:
            operands = problem.split()
            num1, operator, num2 = int(operands[0]), operands[1], int(operands[2])
            result = str(num1 + num2) if operator == '+' else str(num1 - num2)
            results.append(result.rjust(width))

        arranged_problems += f"{' ' * 4}    {' ' * 4} {' '.join(results)}"

    return arranged_problems.strip()



print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
