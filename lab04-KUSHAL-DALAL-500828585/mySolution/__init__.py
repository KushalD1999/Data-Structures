import math
import turtle
import random

#Excercise 1
branchLenRandom = random.randint(5,30)

def tree(branchLen,t):
    
    rightRandom = random.randint(15,45)
    leftRandom = rightRandom *2
    t.pensize(branchLen // 10)
    if branchLen > 5:
        if(branchLen == branchLenRandom):
            t.color("green")                     
            
        t.forward(branchLen)
        t.right(rightRandom)
        tree(branchLen-branchLenRandom,t)
        t.left(leftRandom)
        tree(branchLen-branchLenRandom,t)
        t.right(rightRandom)
        t.backward(branchLen)
        t.color("brown")                                                             

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(branchLenRandom*5,t)
    myWin.exitonclick()

#main()

#Excercise 2

def power(x, n, acc):
    if (n == 0):
        return 1*acc
    if (n == 1):
        return acc*x
    else:
        return (power(x, n-1, 2*acc))

def powerH(x,n):
    if (n == 0):
        return 1
    elif (n == 1):
        return x
    elif (n%2 == 0):
        n = n//2
        return (x*powerH(x,n-1) * x*powerH(x,n-1))
    else:
        n = n//2        
        return (x*powerH(x,n-1) * x*powerH(x,n-1) * x)        

def C(n,k):
    if(k == 0):
        return 1
    if (n == k):
        return 1
    else:
        return C(n-1, k) + C(n-1, k-1)

#def C(n,k):
    #nFactorial = math.factorial(n)
    #denFactorial = math.factorial(n-k)*math.factorial(k)
    #return nFactorial//denFactorial