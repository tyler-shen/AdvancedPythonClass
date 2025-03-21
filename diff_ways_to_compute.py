def diffWaysToCompute(expression):
    result = []

    # base case
    if expression.isdigit():
        result.append(int(expression))
        return result

    for i in range(len(expression)):
        # divide the case
        oper = expression[i]
        if oper == '+' or oper == '-' or oper == '*':
            left = expression[0:i]
            right = expression[i+1:]
            left_result = diffWaysToCompute(left)
            right_result = diffWaysToCompute(right)

            # combine the case
            for j in left_result:
                for k in right_result:
                    if oper == "+":
                        result.append(j + k)
                    elif oper == "-":
                        result.append(j - k)
                    elif oper == "*":
                        result.append(j * k)

    return result


expression = "2*3-4*5"
print(diffWaysToCompute(expression))
