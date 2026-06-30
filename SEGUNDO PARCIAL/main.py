from biblioteca import *

listas ={
    'legajos' :[],
    'ape_nom' :[],
    'generos' :[],
    'pp' :[],
    'sp' :[],
    'promedio':[]
}

def inicio():
    print('--------------------------------------------------------------------------------------')
    print('SISTEMA DE DATOS ESTUDIANTILES')
    print('--------------------------------------------------------------------------------------')
    print('[1] LEER ARCHIVO .JSON Y GENERAR LISTA DE DICCIONARIOS')
    print('[2] PARA REALIZAR LA CARGA DE DATOS SECUENCIAL')
    print('[3] PARA MOSTRAR TODOS LOS DATOS DE LOS ESTUDIANTES')
    print('[4] PARA CALCULAR PROMEDIO DE CADA ESTUDIANTE')
    print('[5] PARA MOSTRAR LISTA DE ESTUDIANTES ORDENADO POR PROMEDIO DE MANERA DESCENDENTE')
    print('[6] PARA MOSTRAR EL/LOS ESTUDIANTES CON MAYOR PROMEDIO')
    print('[7] PARA BUSCAR INFORMACION DE UN ESTUDIANTE POR LEGAJO')
    print('[8] PARA EXPORTAR A JSON LA LISTA INCLUYENDO PROMEDIOS CALCULADOS')
    print('[9] PARA EXPORTAR A CSV LA LISTA INCLUYENDO PROMEDIOS CALCULADOS')
    print('[10] PARA SALIR DEL PROGRAMA')
    print('--------------------------------------------------------------------------------------')
    entrada = int(input('Ingrese opcion a elegir: '))
    #VALIDACION ENTRADA
    while entrada > 10 or entrada < 1:
        entrada = int(input('Ingrese una opcion VALIDA a elegir: '))
    match entrada:
        case 1:
            cargar_json(listas)
            inicio()
        case 2:
            entrada_datos(listas)
            inicio()
        case 3:
            if len(listas['legajos']) == 0:
                print('LAS LISTAS ESTAN VACIAS')
                inicio()
            else:
                mostrar_datos = int(input('¿DESEA MOSTRAR TODOS LOS DATOS[0] O SOLO UN DATO[1]?: '))
                while mostrar_datos != 0 and mostrar_datos != 1:
                    print('ELIJA UNA OPCION VALIDA')
                    mostrar_datos = int(input('¿DESEA MOSTRAR TODOS LOS DATOS[0] O SOLO UN DATO[1]?: '))
                match mostrar_datos:
                    case 0:
                        mostrar_datos_entrada(listas)
                    case 1:
                        mostrar_elemento(listas)
                inicio()
        case 4:
            calcular_promedio_estudiantes(listas)
            inicio()
        case 5:
            ordenar_por_promedio(listas)
            inicio()
        case 6:
            mayores_promedios(listas)
            inicio()
        case 7:
            busqueda_legajo(listas)
            inicio()
        case 8:
            exportar_json(listas)
            inicio()
        case 9:
            exportar_csv(listas)
            inicio()
        case 10:
            return('HASTA LUEGO')
inicio()
           
