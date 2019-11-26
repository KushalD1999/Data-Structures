import random
import matplotlib.pyplot as plotGraph         

def monkeyTypist():
    targetString = "methinks it is like a weasel"
    target = list("methinks it is like a weasel")
    lenTarget = len(target)
    
    alphabets = list("abcdefghijklmnopqrstuvwxyz ")
    lenAlphabet = len(alphabets)
    
    currString = generate(len(target), len(alphabets), alphabets)
    currScore = calcScore(currString, targetString)
    print(" "*10 + "String" +" "*19 +"Iteration" +" "*18+"Score")    
    
    newString = ""
    count = 0
    plotListXaxis = []
    plotListYaxis = []
        
    while(currString != targetString):
        
        count = count+1
        
        if (count%100 == 0):
            print (currString + " "*10+ str(count) + " "*15+ str(calcScore(currString, targetString)))
            
        for x in range(len(newString),len(targetString)):
            if(currString[x] == targetString[x]):
                newString = newString + currString[x]
                plotListXaxis.append(count)
                plotListYaxis.append(calcScore(currString, targetString))
            else:
                break
        
        if(len(newString) != 0):
            tempTargetLength = len(target) - len(newString)
            tempString = generate(tempTargetLength, lenAlphabet, alphabets)
            currString = newString + tempString
        else:
            currString = generate(len(target), lenAlphabet, alphabets)
        
        if (currString == targetString):
            print (currString + " "*10+ str(count) + " "*15+ str(calcScore(currString, targetString)))
            plotListXaxis.append(count)
            plotListYaxis.append(calcScore(currString, targetString))

    plotGraph.xlabel('Iteration')
    plotGraph.ylabel('Scores of Best Strings')            
    plotGraph.plot(plotListXaxis, plotListYaxis, "r+")       
    plotGraph.show()


def generate(lenTarget, lenAlphabet, alphabets):
    if(lenTarget < 0):
        return ""
    else:
        string = ""
        for x in range(lenTarget):
            string = string + random.choice(alphabets)
        return string

def calcScore(bestStr, target):
    count = 0
    if(bestStr == target):
        return (28/28)*100
    else:
        while(bestStr[count] == target[count]):
            count = count+1
        return (count/28)*100
        

monkeyTypist()