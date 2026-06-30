import json
import csv
"FUNCIONES DE VALIDACIONES"
def son_caracteres(cadena:str):
    """
    Esta funcion validad si una cadena esta solamente compuesta por letras mayusuculas y minusculas
    """
    bandera_caracter = False
    for caracter in cadena: #recorre la cadena
        bandera_caracter = False
        if(ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122):#verifica si su valor entero entra en el rango solicitado
            bandera_caracter = True
        else:
            bandera_caracter = False
            break
    return bandera_caracter

def validar_genero(cadena:str):
    """
Esta funcion valida un genero M/F/X
    """
    bandera = False
    longitud = len(cadena)
    if longitud == 1:
        for caracter in cadena:
            if(ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122):
                if (ord(caracter) == 77 or ord(caracter) == 70 or ord(caracter) == 88 or ord(caracter) == 109 or ord(caracter) == 102 or ord(caracter) == 120):
                    bandera = True
            else:
                bandera = False
    else:
        bandera = False
         
    return bandera

def es_int(cad:int):
    """
    Esta funcion valida si una cadena esta compuesta solamente de numeros enteros
    Retorna: Un valor booleano dependiendo si el parametro es un numero entero o no
    """
    bandera_numero = False
    for caracter in cad: #recorre la cadena
        bandera_numero = False
        if (ord(caracter) >= 48 and ord(caracter) <= 57):#verifica si su valor entero entra en el rango marcado
            bandera_numero = True
        else:
            bandera_numero = False
            break
    return bandera_numero

def nota_1_10(cad:int):
    """
    Esta funcion valida notas del 1 al 10
    Retorna: Un valor booleano dependiendo si el parametro es un numero entero y se encuentra en el rango 1-10
    """
    bandera_numero = False
    for caracter in cad: #recorre la cadena
        bandera_numero = False
        if (ord(caracter) >= 48 and ord(caracter) <= 57):#verifica si su valor entero entra en el rango marcado
            bandera_numero = True
        else:
            bandera_numero = False
            break
    if bandera_numero == True:
        numero = int(cad)
        if numero < 1 or numero > 10:
            bandera_numero = False
    return bandera_numero

def apellido_nombre(cadena:str):
    """
    Esta funcion validad si una cadena esta solamente compuesta por letras mayusuculas y minusculas
    retorna: Un valor booleano dependiendo si el parametro esta compuesto por letras y espacios
    """
    bandera_caracter = False
    for caracter in cadena: #recorre la cadena
        bandera_caracter = False
        if(ord(caracter) >= 65 and ord(caracter) <= 90) or (ord(caracter) >= 97 and ord(caracter) <= 122) or (ord(caracter) == 32):#verifica si su valor entero entra en el rango solicitado
            bandera_caracter = True
        else:
            bandera_caracter = False
            break
    return bandera_caracter

'------------------------------------------------------------------------------------------------'
#EJERCICIO 1
def cargar_json(lista:dict):
    with open('data_sp.json',"r",encoding="utf-8") as archivo:
        datos = json.load(archivo)
    for alumno in datos["estudiantes"]:
        lista['legajos'].append(alumno['legajo'])
        lista['ape_nom'].append(alumno['ape_nom'])
        lista['generos'].append(alumno['genero'])
        lista['pp'].append(alumno['pp'])
        lista['sp'].append(alumno['sp'])
    print('CARGA EXITOSA')
'------------------------------------------------------------------------------------------------'
#EJERCICIO 2
def entrada_datos(listas:dict):
    "ESTA FUNCION REALIZA EL INGRESO DE DATOS, UTILIZANDO FUNCIONES DE VALIDACIONES "
    entrada = input("Desea ingresar datos?(N para salir): ")
    while entrada != 'N' and entrada != 'n':
        #LEGAJO 
        num_legajo = input('Ingrese numero de legajo: ')
        #VALIDACION LEGAJO
        validacion_legajo = es_int(num_legajo)
        while validacion_legajo == False or num_legajo in listas['legajos']:
            num_legajo = input('Ingrese numero de legajo VALIDO: ')
            validacion_legajo = es_int(num_legajo)
        listas['legajos'].append(num_legajo)
        #APELLIDO/NOMBRE 
        ape_nom_estudiante = input('Ingrese apellido/nombre del estudiante: ')
        #VALIDACION APELLIDO/NOMBRE
        validacion_ape_nom = apellido_nombre(ape_nom_estudiante)
        while validacion_ape_nom == False:
            ape_nom_estudiante = input('Ingrese apellido/nombre VALIDO del estudiante: ')
            validacion_ape_nom = apellido_nombre(ape_nom_estudiante)
        listas['ape_nom'].append(ape_nom_estudiante)
        #GENERO
        genero_estudiante = input('Ingrese el genero M/F/X: ')
        #VALIDACION GENERO
        validacion_genero = validar_genero(genero_estudiante)
        while validacion_genero == False:
            genero_estudiante = input('Ingrese el genero VALIDO M/F/X: ')
            validacion_genero = validar_genero(genero_estudiante)
        listas['generos'].append(genero_estudiante)
        #PP
        nota_pp = input('Ingrese la nota del primer parcial: ')
        #VALIDACION PP
        validacion_pp = nota_1_10(nota_pp)
        while validacion_pp == False:
            nota_pp = input('Ingrese la nota VALIDA del primer parcial: ')
            validacion_pp = nota_1_10(nota_pp)
        listas['pp'].append(nota_pp)
        #SP
        nota_sp = input('Ingrese la nota del segundo parcial: ')
        #VALIDACION SP
        validacion_sp = nota_1_10(nota_sp)
        while validacion_sp == False:
            nota_sp = input('Ingrese la nota VALIDA del segundo parcial: ')
            validacion_sp = nota_1_10(nota_sp)
        listas['sp'].append(nota_sp)
        entrada = input("Desea ingresar datos?(N/n para salir): ")
'------------------------------------------------------------------------------------------------'
#EJERCICIO 3

#RECORRER TODOS LOS ELEMENTOS
def mostrar_datos_entrada(lista:dict):
    "esta funcion sirve para recorrer todos los elementos de las llaves del diccionario"
    print('LEGAJOS/APELLIDO NOMBRE/GENERO/PP/SP/PROMEDIO')
    cant_elementos_listas = len(lista['legajos'])
    for x in range (cant_elementos_listas):
        print(lista['legajos'][x],'/',lista['ape_nom'][x],'/',lista['generos'][x],'/',lista['pp'][x],'/',lista['sp'][x])

#CARGAR UN SOLO ELEMENTO
def mostrar_elemento(lista:dict):
    "esta funcion solo recorrer un elemento de las llaves"
    cant_elementos_listas = len(lista['legajos']) - 1
    elemento = int(input(f'Que elemento del 0 al {cant_elementos_listas} desea revisar:'))
    while elemento < 0 or elemento > cant_elementos_listas:
        elemento = int(input('INGRESE UN ELEMENTO VALIDO del 0 al {cant_elementos_listas} desea revisar'))
    print('LEGAJOS/APELLIDO NOMBRE/GENERO/PP/SP')
    print(lista['legajos'][elemento],'/',lista['ape_nom'][elemento],'/',lista['generos'][elemento],'/',lista['pp'][elemento],'/',lista['sp'][elemento],'/',)
    
'---------------------------------------------------------------------------------------------------'
#EJERCICIO 4
def calcular_promedio_estudiantes(lista:dict):
    "esta funcion sirve para calcular el promedio de los elementos pp y sp de las llaves del diccionario, imprimiendolos al final"
    cant_elementos_listas = len(lista['legajos'])
    for x in range(cant_elementos_listas):
        #tomamos nota del pp y sp y lo dividimos en 2
        promedio = (int(lista['pp'][x]) + int(lista['sp'][x])) / 2
        lista['promedio'].append(promedio)
        print('LEGAJOS/APELLIDO NOMBRE/GENERO/PP/SP/PROMEDIO')
        print(lista['legajos'][x],'/',lista['ape_nom'][x],'/',lista['generos'][x],'/',lista['pp'][x],'/',lista['sp'][x],'/',lista['promedio'][x])

'----------------------------------------------------------------------------------------------------'
#EJERCICIO 5
def ordenar_por_promedio(lista:dict):
    "esta funcion sirve para ordenar e imprimir de manera descendente los elementos de las llaves del diccionario"
    cant_promedios = len(lista['promedio'])#cantidad de promedios totales
    rango_cant_promedios = list(range(cant_promedios))#rango de promedios (0/promedios totales)
    for i in range(cant_promedios):
        for j in range(0,cant_promedios-i-1):
            #realizamos la comparacion si el segundo elemento es mayor, y si se cumple, los indices cambian de posicion
            if lista['promedio'][rango_cant_promedios[j]] < lista['promedio'][rango_cant_promedios[j+1]]:
                rango_cant_promedios[j],rango_cant_promedios[j+1] = rango_cant_promedios[j+1],rango_cant_promedios[j]

    "realizamos un nuevo diccionario ordenado para no modificar el original"
    lista_ordenada = {}
    for clave in lista.keys():
        lista_ordenada[clave] = []
        #acomodamos los elementos en el orden de indices anteriormente acomodados
        for indices in rango_cant_promedios:
            lista_ordenada[clave].append(lista[clave][indices])
    print('LEGAJOS/APELLIDO NOMBRE/GENERO/PP/SP/PROMEDIO')
    for x in range(cant_promedios):
        print(lista_ordenada['legajos'][x],'/',lista_ordenada['ape_nom'][x],'/',lista_ordenada['generos'][x],'/',lista_ordenada['pp'][x],'/',lista_ordenada['sp'][x],'/',lista_ordenada['promedio'][x])
        
'-----------------------------------------------------------------------------------------------------'
#EJERCICIO 6
def mayores_promedios(lista:dict):
    "esta funcion sirve para mostrar el o los alumnos con mayores promedios comparandolos entre si"
    mayor_promedio = 0
    posiciones =[]#lista vacia en la cual va a guardar las posiciones
    n = len(lista['promedio'])#cantidad total de promedios a recorrer
    for x in range(0,n):
        if lista['promedio'][x] > mayor_promedio:#si el promedio es mayor al mayor promedio, ese promedio es el nuevo mayor promedio
            mayor_promedio = lista['promedio'][x]
 
    for i in range(0,n):
        if lista['promedio'][i] == mayor_promedio:#si el promedio es igual al mayor promedio, se guardara la posicion i dentro de la lista posiciones, la cual guarda la posicion de los mayores promedios
            posiciones.append(i)
    print('LEGAJOS/APELLIDO NOMBRE/GENERO/PP/SP/PROMEDIO')
    for elemento in posiciones:#recorre los elementos guardados en las posiciones con mayores promedios
        print(lista['legajos'][elemento],'/',lista['ape_nom'][elemento],'/',lista['generos'][elemento],'/',lista['pp'][elemento],'/',lista['sp'][elemento],'/',lista['promedio'][elemento])

'-----------------------------------------------------------------------------------------------------'
#EJERCICIO 7
def busqueda_legajo(lista:dict):
    "esta funcion sirve para buscar los elementos de las llaves del diccionario mediante el numero de legajo"
    lista_legajos = lista['legajos']
    legajo_buscado = input(f'Ingrese el legajo a buscar {lista_legajos}: ')
    validacion_legajo_buscado = es_int(legajo_buscado)
    while legajo_buscado not in lista_legajos or validacion_legajo_buscado == False:
        legajo_buscado = input(f'Ingrese UN LEGAJO VALIDO a buscar {lista_legajos}: ')
        validacion_legajo_buscado = es_int(legajo_buscado)
    posicion = lista_legajos.index(legajo_buscado)
    print('LEGAJOS/APELLIDO NOMBRE/GENERO/PP/SP')
    print(lista['legajos'][posicion],'/',lista['ape_nom'][posicion],'/',lista['generos'][posicion],'/',lista['pp'][posicion],'/',lista['sp'][posicion])
'-----------------------------------------------------------------------------------------------------'
#EJERCICIO 8
def exportar_json(lista:dict):
    "creamos un archivo el cual este en modo de escritura"
    with open("datos.json","w") as f:
        "cargamos el diccionario"
        json.dump(lista,f)
    print('EXPORTACION EXITOSA')    
'-----------------------------------------------------------------------------------------------------'
#EJERCICIO 9
def exportar_csv(lista:dict):
    "creamos un archivo el cual este en modo de escritura"
    with open("datos.csv","w",newline='')as archivo:
        "creamos un escritor csv el cual convierte las listas de python en lineas del archivo"
        escritor = csv.writer(archivo)
        "escribe las llaves"
        escritor.writerow(lista.keys())
        "escribe los elementos dentro de las llaves en el rango de la cantidad de legajos"
        for i in range(len(lista["legajos"])):
            escritor.writerow([
                lista["legajos"][i],
                lista["ape_nom"][i],
                lista["generos"][i],
                lista["pp"][i],
                lista["sp"][i],
                lista["promedio"][i]
            ])

    
    

                                                                        
                                            
    
