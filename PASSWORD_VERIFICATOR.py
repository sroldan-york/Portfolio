Nombre= input("Digite su nombre de usuario: ")
Nombre1= len(Nombre)


while True:
    if Nombre1>=6 and Nombre1<=12:
        Letras= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Numeros= "0123456789"
        validacion=0
        validacion1=0
        for letra in Nombre:
            if letra in Letras:
                validacion = validacion + 1
            elif letra in Numeros:
                validacion1 = validacion1 + 1
        total = validacion+validacion1
        if validacion1==0:
            print("su usuario debe de contener letras y numeros")
        elif validacion==0:
            print("su usuario debe de contener letras y numeros")
        elif total==Nombre1:
            print("Nombre de usuario valido! ")
            Contra= input("digite su contraseña: ")
            largo_contra= len(Contra)
            while True:
                if largo_contra>=8:
                    minuscula=0
                    mayuscula=0
                    numeros=0
                    caracter=0
                    for letra in Contra:
                        minuscula_letra=letra.islower()
                        mayuscula_letra=letra.isupper()
                        numeros_letra=letra.isdigit()
                        caracter_letra=letra.isalnum()
            
                        if minuscula_letra==True:
                            minuscula=minuscula+1
                        elif mayuscula_letra==True:
                            mayuscula=mayuscula+1
                        elif numeros_letra==True:
                            numeros=numeros+1
                        elif caracter_letra!=True:
                            caracter=caracter+1
                    total=minuscula+mayuscula+numeros+caracter
                    if minuscula==0:
                        print("su contraseña debe de tener minusculas")
                    elif mayuscula==0:
                        print("su contraseña debe de tener mayusculas")
                    elif numeros==0:
                        print("su contraseña debe de tener numeros")
                    elif caracter==0:
                        print("su contraseña debe de tener caracteres")
                    else:
                        print("Contraseña Valida!")
                    break
                else:
                    print("tu contraseña debe de tener mas de 8 caracteres")
                    break
        else:
            print("su usuario debe de contener letras y numeros")
    
    elif Nombre1<6:
        print("Su nombre de usuario es muy corto ")
        
    elif Nombre1>12:
        print("Su nombre de usuario es muy grande ")
    break
