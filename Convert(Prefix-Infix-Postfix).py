class STACK:
    def __init__(self):
        self.stack=[]
        self.maxsize=100
        self.top=-1
    
    # Check stack full    
    def isfull(self):
        if self.top==self.maxsize-1:
            return True
        else:
            return False
    
    # Check stack empty     
    def isEpmty(self):
        if self.top==-1:
            return True
        else:
            return False
    
    # Add data to stack    
    def push(self,data):
        if self.isfull():
            return None     # Cheak if stack not full
        else:
            self.top += 1
            self.stack.append(data)   # First top++ then add to stack 
            
    # Delete data from stack        
    def pop(self):
        if self.isEpmty():
            return None    # Cheak if stack not full
        else:
            self.top -= 1
            return self.stack.pop()   # First pop the data then top--
    
    # Peak data from stack
    def peak(self):
        if self.isEpmty():
            return None
        else:
            return self.stack[self.top]

# Convert expression from infix to prefix            
def infixtoPrefix(exp):
    opstack=STACK()
    varstack=STACK()
    prec={}      
    prec["("]=1
    prec["+"]=2
    prec["-"]=2
    prec["*"]=3
    prec["/"]=3
    prec["^"]=4
    
    for item in exp:
        
        if item in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm" or item in "123456789":
            varstack.push(item)       # If operand add to varstack
            
        elif item=="(":
            opstack.push(item)              
        
        elif item==")":
            while (opstack.peak() != "("):
                operand1=varstack.pop()
                operand2=varstack.pop()
                oprerator=opstack.pop()
                
                tempstr=oprerator+operand2+operand1
                varstack.push(tempstr)
                # Pop 2 operand and 1 operator and genarate prefix expression
            
            opstack.pop()   # Pop '('
        
        else:
            while(not opstack.isEpmty()) and (prec[opstack.peak()] >= prec[item]):  # If precedence item in opstack > item 
                operand1=varstack.pop()
                operand2=varstack.pop()
                oprerator=opstack.pop()
                
                tempstr=oprerator+operand2+operand1
                varstack.push(tempstr)
                # Pop 2 operand and 1 operator and genarate prefix expression then add to varstack
                
            opstack.push(item)  #add item in opstack
            
    while not opstack.isEpmty():
        operand1=varstack.pop()
        operand2=varstack.pop()
        oprerator=opstack.pop()
                
        tempstr=oprerator+operand2+operand1
        varstack.push(tempstr)
        # Pop 2 operand and 1 operator and genarate prefix expression
    
    return varstack.peak()  # retern varstack to print in output

# Convert expression from infix to postfix
def infixtoPostfix(exp):
    opstack=STACK()
    opstack.push(" ") #first item in opstack for comparison
    string=""
    prec={}
    prec[" "]=1
    prec["("]=2
    prec["+"]=3
    prec["-"]=3
    prec["*"]=4
    prec["/"]=4
    prec["^"]=5
    
    for item in exp:
        if item in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm" or item in "123456789":
            string += item      # if item is operand print in output
            
        elif item=="(":
            opstack.push(item)
            
        elif item==")":
            while (opstack.peak() != "("):
                string += opstack.pop()    # pop operator
                    
            opstack.pop()   # pop '('
            
        elif not (opstack.isEpmty()) and prec[item] > prec[opstack.peak()]:    # If precedence item in opstack < item
            opstack.push(item)
            
        elif not (opstack.isEpmty()) and prec[item] == prec[opstack.peak()]:   # If precedence item in opstack = item
            temp=opstack.pop()  # pop item from opstack
            opstack.push(item)  # push item in opstack
            string += temp      # print pop item in output
                   
        else:
            while(not opstack.isEpmty()) and (prec[opstack.peak()] > prec[item]):   # If precedence item in opstack > item
                temp=opstack.pop()  # pop item from opstack
                opstack.push(item)  # push item in opstack
                string += temp      # print pop item in output
        
    while not opstack.isEpmty():
            string += opstack.pop()    # print anything remaining in stack
    
    return string # print expression       

# Convert expression from prefix to infix 
def prefixtoinfix(exp):
    s=STACK()
    top=len(exp)-1
    
    #Read the experssion from the end
    while top>=0:
        
        if exp[top]!="/" and exp[top]!="*" and exp[top]!="-" and exp[top]!="+" and exp[top]!="^":
            s.push(exp[top])    #add oprand to stack
            top -= 1
            
        else:
            tempstr = "(" + s.pop() + exp[top] + s.pop() + ")"
            s.push(tempstr)  # pop 2 operand with 1 operator then push to stack
            top -= 1
    
    return s.pop()  # print in output

# Convert expression from postfix to infix
def postfixtoinfix(exp):
    op=STACK()

    for item in exp:
        
        if item in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm" or item in "123456789":
            op.push(item)   # add operand to stack
            
        else:
            # pop 2 operand with 1 operator then push to stack
            temp1=op.pop()
            temp2=op.pop()
            temp = '(' + temp2 + item + temp1 + ')'
            op.push(temp)
    
    return op.pop() #print in output

# Convert expression from prefix to postfix
def prefixtopostfix(exp):
    # First convert to infix then convert infix expression to postfix
    infix=prefixtoinfix(exp)
    Postfix=infixtoPostfix(infix)
    return Postfix                 

# Convert expression from postfix to prefix 
def postfixtoprefix(exp):
    # First convert to infix then convert infix expression to prefix
    infix=postfixtoinfix(exp)
    prefix=infixtoPrefix(infix)
    return prefix           

            
## Menu Of The Program ##            
while (1):
    print("1. Infix To Postfix")
    print("2. Infix To Prefix")
    print("3. Postfix To Infix")
    print("4. Prefix To Infix")
    print("5. Postfix To Prefix")
    print("6. Prefix To Postfix")
    print("7. Exit")
    
    select=input("Please choise 1 to 7:")
     
    if select== "1" :
        exp=list(input("Enter Expression:"))
        print("Postfix:",infixtoPostfix(exp))
    elif select== "2":
        exp=list(input("Enter Expression:"))
        print("Prefix:",infixtoPrefix(exp))
    elif select== "3":
        exp=list(input("Enter Expression:"))
        print("Infix:",postfixtoinfix(exp))
    elif select== "4":
        exp=list(input("Enter Expression:"))
        print("Infix:",prefixtoinfix(exp))
    elif select== "5":
        exp=list(input("Enter Expression:"))
        print("Prefix:",postfixtoprefix(exp))
    elif select== "6":
        exp=list(input("Enter Expression:"))
        print("Postfix",prefixtopostfix(exp))
    elif select== "7":
        break
    else:
        print("Invalid Number")
        