class Empty(Exception):
    pass
class arraystack:
    def __init__(self):
        self._data=[]
    def len(self):
        return len(self._data)
    def isempty(self):
        return len(self._data)==0
    def push(self,e):
        self._data.append(e)
    def top(self):
        if self.isempty():
            raise Empty('stack is empty')
        return self._data[-1]
    def pop(self):
        if self.isempty():
            raise Empty('stack is empty')
        return self._data.pop()
    def __str__(self):
        return ''.join(str(self._data))+'>'







def findPositionandDistance(P):#p is a string
    s=arraystack() # this stack is used to store variables 
    s_2=arraystack() # this stack is used to store int value once one open braket start
    a=0
    ct=0 # varible use to count braket
    d=0 # used to store value of int after open braket start
    for i in range(len(P)): # travelling string 
        if(P[i].isdigit()): # to find is str is a digit or not
            if(ct==0): # this mean we havnt pass any open braket or pass open braket but also pass close braket
                c=str(a)+P[i] # this is for...if int is more then one digit
                a=int(c)
            elif(ct!=0): # if we pass any open braket
                if d!=0: 
                    a=a//d
                d=int(str(d)+(P[i])) #to store number after passing one open braket
                if(s_2.isempty()!=True): # if our stack_2 is not empty then
                    s_2.pop() #then pop first 
                s_2.push(d) # append new d
                a=(d*a) # update a
        elif(P[i]=="("): #if we cross an open braket then ct+1 and update d
            ct=ct+1
            d=0
        elif(P[i]==")"):#if we cross a close braket then ct-1 and update d
            d=0
            ct=ct-1
            if( s_2.isempty()==False):
                if (s_2.top()!=0):
                    a=a//s_2.top() # update a 
                    s_2.pop()
            if(ct==0):# if all braket (open and close ) are equal then update a=0
                a=0
        elif(P[i]=="+" or P[i]=="-"): # if we find + or - then store the varible in a stack with corresponding a
            if(a==0): # if a=0 then treat a=1
                s.push(P[i+1]) # first push varible then 'a' then + or - sign
                s.push(1)
                s.push(P[i])
            else:
                s.push(P[i+1])
                s.push((a))
                s.push(P[i])
    a=0 # varible num to store x displacement 
    b=0 # varible num to store y displacement 
    c=0 #varible num to store z displacement 
    d=0 #varible num to store distance travl 
    while not(s.isempty()): # secound loop for stack 1 we have made to simplify it
        if s.top()=="+": # if we got + sign then we have to add then check the varible corresponding to that varible
            s.pop() # pop the sign 
            f=s.top() # assing f as the int val
            d=d+f # add it to dis
            s.pop() # again pop (pop the int val)
            if s.top()=="X": # then check is there sign X or Y or Z correspond to that add num in there corresponding varible assing above 
                s.pop()
                a=a+f
            elif s.top()=="Y":
                s.pop()
                b=b+f
            elif s.top()=="Z":
                s.pop()
                c=c+f
        elif s.top()=="-": # lly case as above but little diff that instead of adding just sub. it
            s.pop()
            f=s.top()
            d=d+f
            s.pop()
            if s.top()=="X":
                s.pop()
                a=a-f
            elif s.top()=="Y":
                s.pop()
                b=b-f
            elif s.top()=="Z":
                s.pop()
                c=c-f
               
    return [a,b,c,d]


