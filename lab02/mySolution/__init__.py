import matplotlib.pyplot as plt 
import timeit
import random

getList = []
updateList = []
commonList1 = []
commonList2 = []

for i in range(10000,1000001,20000):
    
    getTime = timeit.Timer("dictA.get(random.randrange(%d))" %i, 
                           "from __main__ import random, dictA")
    dictA = {key:key for key in range(i)}
    
    getResult = getTime.timeit(number=10000)
    commonList1.append(i)    
    getList.append(getResult)
    #print(i, getResult)

dictB = {}
for i in range(10000,1000001,20000):
    dictB = {key:None for key in range(i)}    
    updateDict = {random.randrange(i):"updated"}
    updateTime = timeit.Timer("dictB.update(updateDict)",
                              "from __main__ import random, dictB, updateDict")
    updateResult = updateTime.timeit(number=10000)
    commonList2.append(i)        
    updateList.append(updateResult)
    #print(i, updateResult)
    
getItem = plt.plot(commonList1,getList, "ro", label='get item')
updateItem = plt.plot(commonList2,updateList, "g^", label='update item')
plt.legend()
plt.show()
    
delDict = []
delList = []
commonList3 = []
commonList4 = []

for i in range(10000,1000001,20000):
    dictC = {key:None for key in range(i)}  
    delDictTime = timeit.Timer("del dictC[random.randrange(%d)]"%i, 
                           "from __main__ import random, dictC")    
    delDictResult = delDictTime.timeit(number=10)
    commonList3.append(i)            
    delDict.append(delDictResult)   
    #print(i, delDictResult)
    

for i in range(10000,1000001,20000):
    listD = [key for key in range(i)]    
    delListTime = timeit.Timer("del listD[random.randrange(%d)]"%i, 
                           "from __main__ import random, listD")
    
    delListResult = delListTime.timeit(number=10)
    commonList4.append(i)        
    delList.append(delListResult)       
    #print(i, delListResult)

plt.plot(commonList3,delDict, "r^", label='del Dict item')
plt.plot(commonList4,delList, "go", label='del List item')
plt.legend()
plt.show()