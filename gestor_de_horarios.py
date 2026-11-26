import os


def validar_dia(texto):
    """
    (uso de funciones, manipulacion de cadenas)
    recibe: cadena de texto
    normaliza el texto recibido y lo compara
    con los dias habiles de la lista
    para comprobar que sea valido
    devuelve: valor booleano (True o False)
    """
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
    texto = normalizar_dia(texto)
    for elem in dias:
        if texto == elem:
            return True
    return False


def pedir_materias():
    """
    (uso de funciones, ciclos)
    recibe: nada
    pide al usuario los detalles de la materia a agregar.
    Usa ciclos while para volver a pedir el dia si
    no es de lunes a viernes y las horas si la de fin no
    es mayor que la de inicio
    devuelve: materia, dia, hora_inicio, hora_fin (int)
    """
    materia = input("Materia: ")
    dia = input("Dia: ")
    while not validar_dia(dia):
        print("Dia invalido. Escribe un dia de lunes a viernes.")
        dia = input("Dia: ")

    hora_inicio = int(input("Hora inicio: "))
    hora_fin = int(input("Hora fin: "))

    while not validar_horario(hora_inicio, hora_fin):
        print("Las horas deben ser de 7 a 22 \n"
              "La hora de fin debe ser mayor que la hora de inicio")
        hora_inicio = int(input("Hora inicio: "))
        hora_fin = int(input("Hora fin: "))

    return materia, dia, hora_inicio, hora_fin


def quitar_acentos(texto):
    """
    (uso de funciones, manipulacion de cadenas)
    recibe: cadena de texto
    reemplaza aquellas vocales que tienen acento por esas
    mismas letras sin acento
    devuelve:la cadena sin acentos (str)
    """
    reemplazar = "áéíóú"
    cambio = "aeiou"
    i = 0
    for elem in reemplazar:
        texto = texto.replace(elem, cambio[i])
        i += 1
    return texto


def quitar_espacios(texto):
    """
    (uso de funciones, manipulacion de cadenas)
    recibe: cadena de texto
    elimina los espacios en blanco al principio y al final
    de la cadena
    devuelve: la cadena sin espacios al inicio o al final
    """
    return texto.strip()


def minusculas(texto):
    """
    (uso de funciones, manipulacion de cadenas)
    recibe: cadena de texto
    convierte el texto a minusculas
    devuelve: la cadena con todas las letras del texto
    en minusculas
    """
    return texto.lower()


def normalizar_dia(texto):
    """
    (uso de funciones, manipulacion de cadenas)
    recibe: nombre del dia escrito por el usuario
    convierte el texto a minusculas, le quita los espacios
    en blanco que puede llegar a haber y quita acentos
    devuelve: el nombre del dia normalizado
    """
    texto = minusculas(texto)
    texto = quitar_espacios(texto)
    texto = quitar_acentos(texto)
    return texto


def formatear_materia(materia):
    """
    (uso de funciones, manipulacion de cadenas)
    recibe:  nombre de la materia escrito por el usuario
    quita espacios que sobran y pone mayuscula al inicio de cada palabra
    devuelve: el nombre de la materia formateado
    """
    materia = materia.split()
    materia = " ".join(materia)
    materia = materia.title()
    return materia


def validar_horario(hora_inicio, hora_fin):
    """
    (uso de operadores, funciones, condicionales)
    recibe: hora_inicio valor numerico, hora_fin valor numerico
    calcula la duracion de la materia al restar hora_inicio a hora_fin
    comprueba que sea positiva, si la resta es mayor que 0
    revisa que las horas esten entre 7 y 22.
    devuelve: valor booleano (True o False)
    """
    duracion = hora_fin - hora_inicio
    if duracion <= 0:
        return False
    if hora_inicio < 7 or hora_fin > 22:
        return False
    return True


def mostrar_horario(horario):
    """
    (uso de funciones, condicionales, ciclos)
    recibe: matriz de horario
    imprime los detalles de las materias registradas mediante un bucle
    No devuelve un valor
    """
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    i = 0
    print("Materia\t\tDia\t\tHora inicio\tHora fin")
    while i < len(dias):
        j = 0
        while j < len(horario):
            if normalizar_dia(dias[i]) == normalizar_dia(horario[j][1]):
                print(f"{formatear_materia(horario[j][0]):<16}"
                      f"{dias[i]:<16}"
                      f"{horario[j][2]:<16}"
                      f"{horario[j][3]}")
            j += 1
        i += 1


def mostrar_horario_enumerado(horario):
    """
    (uso de funciones, condicionales, ciclos)
    recibe: matriz de horario
    imprime los detalles de las materias registradas mediante un bucle
    No devuelve un valor
    """
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    i = 0
    print("Posicion\tMateria\t\tDia\t\tHora inicio\tHora fin")
    while i < len(dias):
        j = 0
        while j < len(horario):
            if normalizar_dia(dias[i]) == normalizar_dia(horario[j][1]):
                print(f"{j+1:<16}"
                      f"{formatear_materia(horario[j][0]):<16}"
                      f"{dias[i]:<16}"
                      f"{horario[j][2]:<16}"
                      f"{horario[j][3]:<16}")
            j += 1
        i += 1


def obtener_total_horas(horario):
    """
    (uso de operadores, funciones, ciclos, matrices)
    recibe: matriz de horario
    recorre la matriz de horario
    calcula la duracion de la materia al restar hora_inicio a hora_fin
    y la suma al total
    devuelve: el total de horas
    """
    total = 0
    i = 0
    while i < len(horario):
        duracion = horario[i][3] - horario[i][2]
        total += duracion
        i += 1
    return total


def existe_archivo(nombre):
    """
    (uso de funciones, rutas)
    recibe: el nombre del archivo
    verifica si el archivo existe en la
    carpeta donde se ejecuta el programa
    devuelve: valor booleano (True o False)
    """
    return os.path.exists(nombre)


def hay_empalme(horario, dia, hora_inicio, hora_fin):
    """
    (uso de funciones, condicionales, ciclos)
    recibe: matriz de horario, variables de dia, hora_inicio, hora_fin
    compara un dia y horario especificos contra las materias ya registradas
    en la matriz para verificar si se empalman.
    devuelve: valor booleano (True o False)
    """
    i = 0
    ren = len(horario)
    while i < ren:
        if (normalizar_dia(dia) == normalizar_dia(horario[i][1])
            and hora_inicio < horario[i][3] and hora_fin > horario[i][2]):
            return True
        i += 1
    return False


def agregar_materias(horario, materia, dia, hora_inicio, hora_fin):
    """
    (uso de funciones, listas, matrices)
    recibe: matriz de horario
    y variables de materia, dia, hora_inicio, hora_fin
    crea una fila con los datos de la materia
    y la añade a la matriz.
    No devuelve nada
    """
    lista = [materia, dia, hora_inicio, hora_fin]
    horario.append(lista)


def eliminar_materia(horario, pos):
    """
    (uso de funciones, ciclos, matrices)
    recibe: matriz de horario y posicion
    de la materia a eliminar
    crea una matriz nueva y le agrega todas las filas
    del horario excepto la que esta en la posicion
    indicada
    devuelve: una matriz nueva sin la materia eliminada
    """
    mat = []
    i = 0
    while i < len(horario):
        if i != pos - 1:
            mat.append(horario[i])
        i += 1
    return mat


def guardar_horario(horario, nombre):
    """
    (uso de funciones, condicionales, ciclos, archivos)
    recibe: matriz de horario, cadena de nombre
    crea un archivo con el nombre que recibe
    como parametro y lo llena a partir de los
    datos que tiene la matriz de horario usando
    ciclos while, le pone comas para que sea del
    estilo csv
    No devuelve nada
    """
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    nombre = nombre.replace(".txt", "")
    archivo = open(f"{nombre}.txt", "w")
    i = 0
    archivo.write("Materia,Dia,Hora_inicio,Hora_fin\n")
    while i < len(dias):
        j = 0
        while j < len(horario):
            if normalizar_dia(dias[i]) == normalizar_dia(horario[j][1]):
                archivo.write(f"{formatear_materia(horario[j][0])},{dias[i]},"
                              f"{horario[j][2]},{horario[j][3]}\n")
            j += 1
        i += 1
    archivo.close()


def cargar_horario(nombre):
    """
    (uso de funciones, archivos, ciclos,
    matrices, cadenas )
    recibe un archivo que contiene el horario
    abre el archivo, se salta el encabezado y por cada linea
    quita los espacios, separa los datos por comas y
    convierte las horas a enteros, agregando cada fila
    a una matriz
    devuelve: matriz con los datos cargados
    """
    archivo = open(nombre, "r")
    lineas = archivo.readlines()
    archivo.close()
    mat = []
    i = 1
    while i < len(lineas):
        fila = quitar_espacios(lineas[i])
        fila = fila.split(",")
        if len(fila) == 4:
            fila[2] = int(fila[2])
            fila[3] = int(fila[3])
            mat.append(fila)
        i += 1
    return mat


horario = []
nombre = ""
continuar = True
contador = 0


# Ciclo que repite el menu del gestor de horarios

while continuar:
    print("Bienvenido al Gestor de Horarios \n"
          "1: Agregar materias manualmente\n"
          "2: Cargar horario y abrirlo\n"
          "3: Eliminar materia\n"
          "4: Mostrar detalles del horario actual\n"
          "0: Salir\n"
          "Seleccione una opcion:")

    opcion = int(input())
    if opcion == 1:
        agregar = True

        # Ciclo que se repite mientras el usuario quiera agregar materias
        while agregar:
            materia, dia, hora_inicio, hora_fin = pedir_materias()

            # Se revisa si hay empalme con alguna materia ya registrada
            empalme = hay_empalme(horario, dia, hora_inicio, hora_fin)

            # Si hay empalme se avisa al usuario
            if empalme:
                print("Hay empalme entre las dos materias.")
            else:
                # Si no hay empalme, se registra la materia
                agregar_materias(horario, materia, dia, hora_inicio, hora_fin)
                contador += 1

            respuesta = int(input("¿Desea agregar otra materia? "
                                  "(si = 1/no = 0): "))
            agregar = respuesta == 1

        # Se pide el nombre del archivo, se guarda el horario y se muestra
        nombre = input("¿Con que nombre lo deseas guardar? (sin extension): ")
        nombre = nombre.replace(".txt", "")
        print("Detalles de tu horario:")
        guardar_horario(horario, nombre)
        mostrar_horario(horario)

        regresar = int(input("¿Desea regresar al menu? (si = 1/no = 0): "))
        continuar = regresar == 1

    elif opcion == 2:
        # Pide el nombre del archivo y comprueba si existe en la ruta
        nombre = input("Escriba el nombre del archivo: ")
        if existe_archivo(nombre):
            # Si el archivo existe se muestra en consola su contenido
            horario = cargar_horario(nombre)
            contador = len(horario)
            print("Detalles de tu horario:")
            mostrar_horario(horario)
        else:
            print("No se encontro el archivo", nombre)
        respuesta = int(input("¿Desea regresar al menu? (si = 1/no = 0): "))
        continuar = respuesta == 1

    elif opcion == 3:
        # Se comprueba si la matriz de horario contiene alguna materia
        if len(horario) > 0:
            # Se da a elegir al usuario la materia a eliminar
            mostrar_horario_enumerado(horario)
            pos = int(input("Numero de la materia a eliminar: "))
            # Validacion para evitar error de indice
            if pos >= 1 and pos <= len(horario):
                materia = horario[pos - 1][0]
                horario = eliminar_materia(horario, pos)
                guardar_horario(horario, nombre)
                print("Se eliminó la materia:", formatear_materia(materia))
                contador -= 1
            else:
                print("Numero invalido")
        else:
            print("No hay materias en el horario. Crea o carga uno primero.")
    elif opcion == 4:
        # Se muestra el horario actual si tiene materias
        if len(horario) > 0:
            horas = obtener_total_horas(horario)
            print("El numero de materias inscritas es:", contador)
            print("El numero total de horas es:", horas)
            mostrar_horario(horario)
        else:
            print("No hay materias en el horario.")
    elif opcion == 0:
        continuar = False

    else:
        print("Opcion no valida.")
