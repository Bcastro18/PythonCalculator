#Main

def Add ():
    count = GetValue1()
    count2 =  GetValue1()
    result = str(count + count2)
    print ("Soma:" + result)
    operationsRecurs()
    
def Sub ():
    count = GetValue1()
    count2 =  GetValue1()
    result = str(count - count2)
    print ("Subtração:" + result)
    operationsRecurs()

def Div ():
    count = GetValue1()
    count2 =  GetValue1()
    result = str(count / count2)
    print ("Divisão:" + result)
    operationsRecurs()

def Mult ():
    count = GetValue1()
    count2 =  GetValue1()
    result = str(count * count2)
    print ("Multiplicação:" +  result)
    operationsRecurs()

def GetValue1():
    valor = float(input("Please, insert a number: "))
    return valor


def operationsRecurs():
    oper = int(input("Choose an operation: "))
    if oper == 1:
        Add()
    elif oper == 2:
        Sub()
    elif oper == 3:
        Mult()
    elif oper == 4:
        Div()
    else:
        print ("Insira uma opção valida! ")
        operationsRecurs()






operationsRecurs()



