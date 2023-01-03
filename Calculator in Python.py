#calculator to pratice
#Bruno - 03/01/2023

def Add (count, count2):
    result = str(count + count2)
    print ("Soma:" + result)
    

def Sub (count, count2):
    result = str(count - count2)
    print ("Subtração:" + result)

def Div (count, count2):
    result = str(count / count2)
    print ("Divisão:" + result)

def Mult (count, count2):
    result = str(count * count2)
    print ("Multiplicação:" +  result)


valor = float(input("Please, insert a number:"))

valor2 = float(input("Please, insert a second number:"))

oper = int(input("qual operação fará?"))

if oper == 1:
    Add(valor, valor2)
elif oper == 2:
    Sub(valor, valor2)
elif oper == 3:
    Mult(valor, valor2)
elif oper == 4:
    Div(valor, valor2)
else:
    print ("Insira uma opção valida")




