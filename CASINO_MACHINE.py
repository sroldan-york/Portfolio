import random

LINEAS_MAXIMAS=3 #Poniendo una variable toda en mayuscula se va a convertir en una variable constante
MAXIMO=1000
MINIMO=1

LINEAS= 3
COLUMNAS=3

VALOR_SIMBOLOS={
    "!": 2,
    "@": 4,
    "#": 6,
    "$": 8
}

resultado_simbolos={
    "!": 5,
    "@": 4,
    "#": 3,
    "$": 2
}

def ganar(columnas, lineas, apuesta, valores):
    ganado = 0
    ganado_lineas=[]
    for linea in range(lineas):
        simbolo=columnas[0][linea]
        for columna in columnas:
            simbolo_a_revisar=columna[linea]
            if simbolo != simbolo_a_revisar:
                break
        else:
            ganado+=valores[simbolo]*apuesta
            ganado_lineas.append(linea+1)
    return ganado, ganado_lineas
        
def obtener_simbolos(LINEAS, COLUMNAS, SIMBOLOS):
    maquina=[]
    for SIMBOLO, VALOR_SIMBOLOS in SIMBOLOS.items():
        for _ in range(VALOR_SIMBOLOS):
            maquina.append(SIMBOLO)

    tablero= []
    for _ in range(COLUMNAS):# se crea un cuadrito en una columna (o sea, se repite 3 veces)
        tab=[]
        simbolos_puestos=maquina[:]#con estos dos puntos se copia una lista, esto lo hacemos para no cambiar el valor de maquina y cambiar los valores de una copia
        for _ in range(LINEAS):#aqui pasamos 3 veces por las lineas que se tienen que crear (3 lineas)
            valor=random.choice(simbolos_puestos)
            simbolos_puestos.remove(valor)
            tab.append(valor)
        tablero.append(tab)
    return tablero

def mostrar_tablero_tres_por_tres(columna):
    for linea in range(len(columna[0])):
        for i, col in enumerate(columna):
            if i != len(columna) - 1:
                print(col[linea],end=" | ")
            else:
                print(col[linea], end="")
        print()

def dinero():
    while True:
        total=input("Cuanto dinero quiere depositar? $")
        if total.isdigit():
            total=int(total)
            if total> 0:
                break
            else:
                print("el total tiene que ser mayor a 0")
        else:
            print("Digite una cantidad en numeros")
    return total

def numero_de_lineas():
    while True:
        lineas=input("Por cuantas lineas quiere apostar? 1-"+str(LINEAS_MAXIMAS))
        if lineas.isdigit():
            lineas=int(lineas)
            if 1<=lineas<=LINEAS_MAXIMAS:
                break
            else:
                print("Ponga un numero validao de lineas existentes")
        else:
            print("Digite una cantidad en numeros")
    return lineas

def obtener_apuesta():
    while True:
        total=input("Cuanto dinero quiere apostar en cada linea? $")
        if total.isdigit():
            total=int(total)
            if MINIMO<=total<=MAXIMO:
                break
            else:
                print(f"La cantidad tiene que estar entre ${MINIMO}- ${MAXIMO}")
        else:
            print("Digite una cantidad en numeros")
    return total

def juego(balance):
    lineas=numero_de_lineas()
    while True:
        apuesta=obtener_apuesta()
        if 0<(apuesta*lineas)<balance:
            break
        else:
            print(f"no tiene suficiente dinero, tu tienes ${balance}")
    print(f"Estas apostando {apuesta} en {lineas} lineas, en total seria ${apuesta*lineas}")
    imagen=obtener_simbolos(LINEAS, COLUMNAS, VALOR_SIMBOLOS)
    print(mostrar_tablero_tres_por_tres(imagen))
    ganado, ganado_lineas=ganar(imagen,lineas, apuesta, resultado_simbolos)
    print(f"Has ganado ${ganado} y ganaste en",*ganado_lineas ,"lineas")
    return ganado-apuesta*lineas

def volver_a_jugar():
    balance=dinero()
    while True:
        print(f"tu estado de cuenta es ${balance}")
        empezar=input("Presiona enter para jugar (q para salir)")
        if empezar=="q":
            break
        balance+=juego(balance)
    
volver_a_jugar()
