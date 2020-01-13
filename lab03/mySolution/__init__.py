import math 

class EmptyStackException(Exception):
    pass

class Stack():
    def __init__(self):
        self._listA = []
        self._size = 0
    
    def push(self, element):
        self._listA.append(element)
        self._size = self._size +1

    def pop(self):
        if self.is_empty(): 
            raise EmptyStackException ("This stack is empty")        
        self._size = self._size - 1
        return self._listA.pop()

    def is_empty(self):
        return (self._size == 0)

    def size(self):
        return self._size

    def peek(self):
        if (self.is_empty()):
            raise EmptyStackException("This Stack is Empty")
        return self._listA[len(self._listA) -1]
    
    def __str__(self):
        '''(Stack) ->str
        returns the elements stored in this stack'''
        result = ""
        for item in self._listA:
            result = result + str(item) + ", "
        return "[" + result[:-2] + "]"    

def infixToPostfixEval(string):
    precedence = {
        "!": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1, 
        ")": 1 
        
    }
    listA =  string.split()
    stackA = Stack()
    operandStack = Stack()    
    returnList = []
    
    for x in listA:
        #if (x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or x in "0123456789"):
        if (x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or x.isdigit()):        
            returnList.append(x)
        elif (x == '('):
            stackA.push(x)
        elif (x == ')'):
            token = stackA.pop()
            while(token != "("):
                returnList.append(token)
                token = stackA.pop()
        else:
            while (stackA.is_empty() != True) \
            and (precedence[stackA.peek()] >= precedence[x]):
                returnList.append(stackA.pop())
            stackA.push(x)
    
    while(stackA.size() != 0):
        returnList.append(stackA.pop())
    
    for y in returnList:
        #if y in "0123456789":
        if y.isdigit():        
            operandStack.push(int(y))
        elif(y == "!"):
            operand = operandStack.pop()
            result = math_Operation(y,operand)
            operandStack.push(result)            
            
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = math_Operation(y,operand1,operand2)
            operandStack.push(result)
    
    return (" ".join(returnList),operandStack.pop())


def math_Operation(op, op1, op2=None):
    if(op == "!"):
        return math.factorial(op1)       
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
