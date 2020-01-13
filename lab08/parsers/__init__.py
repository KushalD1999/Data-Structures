def precedence(oper):
    if oper in ['+', '-']:
        return 1
    elif oper in ['*', '/']:
        return 2
    else:
        return 3

def operatorp(x):
    return x in ['+', '-', '/', '*', '!']

def numberp(x):
    return not operatorp(x)


def parse(expr):
    return parseHelper(expr, [], [])

#x=['3','/','6','-', '9']
def parseHelper(expr, operators, operands):
    if expr == []:
        if operators == []:
            return operands[0]
        else:
            return handleOp([], operators, operands)
        
    if ((type(expr[0]) == type([])) and len(expr[0]) != 0):
        new = parseHelper(expr[0], [], [])
        return parseHelper(expr[1:], operators, [new]+operands)
    
    elif (expr[0] == "!"):
        return parseHelper(expr[1:], operators, [[expr[0], operands[0], []]]+operands[1:])    
        
    # for numbers
    if numberp(expr[0]):
        return parseHelper(expr[1:], operators, [[expr[0], [], []]]+operands)
    
    # for operators with precendence
    elif operators == [] or precedence(expr[0]) > precedence(operators[0]):
        return parseHelper(expr[1:], [expr[0]]+operators, operands)
    
    else:
        return handleOp(expr, operators, operands)

def handleOp(expr, operators, operands):
    return parseHelper(expr, operators[1:], [[operators[0], operands[1], operands[0]]]+operands[2:])


#x=['3','/','6','-', '9']
#print(parse(x))
#print(parse([['4', '+', '3'], '*', '7']))
#print(parse([['4', '+', '3'], '*', '7']) == ['*', ['+', ['4', [], []], ['3', [], []]], ['7', [], []]])
#print(parse(['2', '!']))
#print(parse(['4', '+', ['3', '!']]) == ['+', ['4', [], []], ['!', ['3', [], []], []]])
#print(parse(['4', '+', [['3', '+', '1'], '!']]) == ['+', ['4', [], []], ['!', ['+', ['3', [], []], ['1', [], []]], []]])
#print(parse(['3','/',['6', '!'],'-', '9']) == ['-', ['/', ['3', [], []], ['!', ['6', [], []], []]], ['9', [], []]])

#print (parse([['2','!'],'/','2','!']))

#x=['4', '+', '3', '*', '7']
#x=[['4'], '+', ['3'], '+', '6']
#x="( 4 + 3 * 7 - 5 / ( 3 + 4 ) + 6 )"