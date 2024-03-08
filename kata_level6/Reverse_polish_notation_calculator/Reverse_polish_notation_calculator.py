def calc(expr):
    res= []
    if len(expr) < 1:
        return 0
    else:
        if len(expr.split(' ')) == 1:
            return float(expr)

        else:
            for i in expr.split(' '):
                if i in "+-*/":
                    i = str(res.pop(-2)) + i + str(res.pop())
                res.append(eval(i))

        return res[0]