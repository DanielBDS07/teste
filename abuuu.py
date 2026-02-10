acessar = (input('quer entrar na calculadora [s/n]: '))

def conta2(num1, op1 , num2):
    print('sua conta foi' , num1 , op1 , num2 )

def conta3(num1, op1 , num2, O2, n3):
    print('sua conta foi' , num1 , op1 , num2 , O2 , n3)


def conta (num1, op1, num2):
    error = False
    match op1:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case"*":
            result = num1 * num2
        case "/":
            if num2 == 0:
                error = True
                return error
            else:
                result = num1 / num2
        case _:
            error = True
            return error
    return result

def erro (resultado):
    confirmar = True
    if resultado == True:
        print("Você cometeu um equivoco. Não divida por 0 ou insira um operador válido")
    else:
        confirmar = False
        return confirmar

while acessar == 's':
    quantidade = (input('com quantos algaritimos você quer a sua conta?(2 ou 3) :'))
    n1 = float(input("Primeiro digito: ")) 
    O1 = input("Operador Aritmético (+,-,*,/): ") 
    n2 = float(input("Segundo digito: ")) 

    if quantidade == "2":
        chave = True
        result1 = conta(n1,O1,n2)

        if erro(result1) == False:
            print('      ')
            conta2(n1,O1,n2)
            print(f"o resultado é: {result1}")


    elif quantidade == "3":
        O2 = input("2° Operador Aritmético (+,-,*,/): ") 
        n3 = float(input("terceiro digito: "))
        chave = False

        if O2 == "*" or O2 == "/":
            result1 = conta(n2,O2,n3)

            if erro(result1) == False:
                result2 = conta(n1,O1,result1)
            
            if erro(result2) == False:
                print(f"o resultado é: {result2}")
        else:
            result1 = conta(n1,O1,n2)

            if erro(result1) == False:
                result2 = conta(result1,O2,n3)
            
            if erro(result2) == False:
                print('      ')
                conta3(n1, O1 , n2, O2, n3)
                print(f"o resultado é: {result2}")
    print('      ')
    acessar = (input('quer continuar [s/n]: '))
else: 
    print('muito obrigado por acessar, receba!')