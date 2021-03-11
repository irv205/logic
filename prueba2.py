romanos=[
        "I","V",
        "X", "L",
        "C", "D",
        "M"
    ]

#numero del 1 al 9 y sistema decimal= unidad, decena, centena, 
#unidad de millar de modo que se indique que lugar ocupa en el numero a convertir
def to_romano(num,sis_dec):
        if sis_dec == 1:
            datos=[romanos[0],romanos[1],romanos[2]]
        elif sis_dec == 2:
            datos=[romanos[2],romanos[3],romanos[4]]
        elif sis_dec == 3:
            datos=[romanos[4],romanos[5],romanos[6]]
        elif sis_dec == 4:
            datos=[romanos[6],"Â","Ê"]

        if num == 1: return datos[0]
        elif num == 2: return datos[0]+datos[0]
        elif num == 3: return datos[0]+datos[0]+datos[0]
        elif num == 4: return datos[0]+datos[1]
        elif num == 5: return datos[1]
        elif num == 6: return datos[1]+datos[0]
        elif num == 7: return datos[1]+datos[0]+datos[0]
        elif num == 8: return datos[1]+datos[0]+datos[0]+datos[0]
        elif num == 9: return datos[0]+datos[2]
        else: return ""

def num_to_romano(num):
    num_romano=""
    for i in range(0,len(str(num))):
        num_romano += to_romano(int(str(num)[i]),len(str(num))-i)
    return num_romano

def year_romano(num):
    if "BC" in num:
        num = num.replace("BC","")
        return 754 - int(num)
    elif "AD" in num:
        num = num.replace("AD","")
        return 753 + int(num)

def tam_de_memoria(rango ="753BC-747BC"):
    rangos=(rango.upper()).split("-")
    # rango minimo = rangos[0] y rango maximo = rangos[1]
    ran_min, ran_max, tam = year_romano(rangos[0]),year_romano(rangos[1]),0
    for i in range(ran_min,ran_max + 1 ): #print(num_to_romano(i))
        if tam < len(num_to_romano(i)) : tam =len(num_to_romano(i))
    return tam

"""
Ejecutar en consola de python
import prueba2

prueba2.tam_de_memoria("1BC-1AD")
prueba2.tam_de_memoria("2000AD-2012AD")
prueba2.tam_de_memoria("53BC-47BC")
"""