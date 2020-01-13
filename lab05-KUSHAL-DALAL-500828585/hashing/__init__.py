class HashTable():
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self._loadFactor = 0
    
    
    def reSize(self):
        nextPrime = self.findNextPrime(self.size+1, 1000)
        newLength = nextPrime - self.size
        self.size = self.size + newLength

        self._numberOfElement = 0
        tempSlot = []
        tempData = []
        
        for x in range(len(self.slots)):
            if(self.slots[x] != None and self.data[x] != None):
                tempSlot.append(self.slots[x])
                tempData.append(self.data[x])
                
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
        for x in range(len(tempSlot)):
            self.put(tempSlot[x], tempData[x])
    
    def put(self,key,data):        
        
        countElements = 0
        for x in range(len(self.slots)):
            if(self.slots[x] != None):
                countElements+=1
                
        # Check LoadFactor
        self._loadfactor =(countElements /self.size)
        if(self._loadfactor > 0.9):
            self._loadfactor = 0
            self.reSize()
       

        hashvalue = self.hashfunction(key,len(self.slots))        

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  #replace
            else:
                nextslot = self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data #replace
                            
    def hashfunction(self,key,size):
        return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
    
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))
    
        data = None
        stop = False
        found = False
        
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
                #self._numberOfElement-=1                
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True  
        return data
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)


    def findNextPrime(self, a, b):
        for p in range(a, b):
            for i in range(2, p):
                if p % i == 0:
                    break
            else:
                return p
        return None





H=HashTable()
H[54]="1"
H[26]="2"
H[93]="3"
H[17]="4"
H[77]="5"
H[31]="6"
H[44]="7"
H[55]="8"
H[20]="9"
H[200]="10"
H[201]="11"
H[202]="12"
H[203]="13"


print(H.slots)
print(H.data)

print(H.get(77))

print(H[20])

print(H[17])
H[20]='duck'
print(H[20])
print(H[99])
