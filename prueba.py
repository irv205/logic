def prueba(n,m):

    if(n > m and m%2 == 0): return "U"
    elif (n>m and m%2 != 0): return "D"
    elif (n<=m and n%2 == 0): return "L"
    elif (n<=m and n%2 != 0): return "R"


"""
Ejecutar en consola de python
import prueba

prueba.prueba(1,1)
prueba.prueba(2,2)
prueba.prueba(3,1)
prueba.prueba(3,3)
"""