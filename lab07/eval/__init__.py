def evalExpression(listA):
    if (len(listA) == 0):
        return ""   
    elif (listA[0] == []):
        return ""
    #elif (not isinstance(listA[0], list)):        
    elif (type(listA[0]) != type([])):
        return str(listA[0]) + evalExpression(listA[1:])
    #(type(listA[0]) == type([])):
    else:
        new = str(listA[0][0]) + evalExpression(listA[0][1:]) 
        return new + evalExpression(listA[1:])

def preToInf(prefixExpression):
    
    if (len(prefixExpression) == 0):
        return None
    elif (prefixExpression.isalnum()):
        return prefixExpression
    
    dictA = {'+': 1, '-': 1, '*': 2, '/': 2}
    setOfOperator = set(['+', '-', '*', '/', '(', ')'])
    
    Stack = []
    previousOperation = None
    prefixExpression = reversed(prefixExpression)

    for x in prefixExpression:
        if not x in setOfOperator:
            Stack.append(x)
        else:
            a = Stack.pop()
            b = Stack.pop()
            if previousOperation and dictA[previousOperation] < dictA[x]:
                exp = "("+ a + ")" + x + "(" + b + ")"
            else:
                exp = a+x+b
            previousOperation = x            
            Stack.append(exp)

    ret = Stack[-1]
    return ret

#[["a", 10], ["b", 20], ["c",30]]
#a+b*c
def evalEnvironment(stringA, listB):
    if (stringA == None):
        return None
    dictA = {}
    for x in range(len(listB)):
        if listB[x][0] in dictA:
            pass
        else:
            dictA[listB[x][0]] = listB[x][1]
    #Operand Case
    if stringA in dictA:
        return dictA[stringA]
    #Operator and Operand Case
    count=0
    retString = ""
    for x in stringA:
        if (x.isalpha()):
            if x in dictA:
                retString = retString + str(dictA[x])
            else:
                return None
        else:
            retString = retString + x

    # check for ZeroDivisionError
    try:     
        ret = (eval(retString))
    except:
        ret = None
    return ret
            

def evalTree(listA, listB):
    return1 = evalExpression(listA)
    if (return1.isdigit()):
        return int(return1)
    return2 = preToInf(return1)
    return3 = evalEnvironment(return2, listB)
    return (return3)
    


#print (evalTree([[], [], []], [["a", 10], ["b", 20], ["c",30]]))  
print (evalTree(["10", [], []], [["a", 10], ["b", 20], ["c",30]]))
print (evalTree(["x1", [], []], [["a", 10], ["x1", 22]]))
print (evalTree(["/", ["a", [], []], ["0", [], []]], [["a", 10], ["x1", 22]]))
print (evalTree(["*", ["b", [], []], ["c", [], []]], [["a", 10], ["b", 20], ["c",30]]))
print (evalTree(["+", ["a", [], []], ["*", ["b", [], []],["c", [], []]]],[["a", 10], ["b", 20], ["c",30]]))
print (evalTree(["+", ["a", [], []], ["*", ["b", [], []],["c", [], []]]], [["b", 20], ["c", 30]] ))