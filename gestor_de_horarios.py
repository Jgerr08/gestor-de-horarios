def quitar_acentos(texto):
    """
    (manipulación de cadenas)
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
        i+=1
    return texto

def validar_dia(texto):
    """
    (manipulación de cadenas)
    recibe: cadena de texto
    normaliza el texto recibido y lo compara
    con los días habiles de la lista
    para comprobar que sea valido
    devuelve: valor booleano (True o False)
    """
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]
    texto = normalizar_dia(texto)
    for elem in dias:
        if texto == elem:
            return True
    return False


def quitar_espacios(texto):
    """
    (manipulación de cadenas)
    recibe: cadena de texto
    elimina los espacios en blanco al principio y al fin
    de la cadena
    devuelve: la cadena sin espacios al inicio ni al final
    """
    return texto.strip()

def minusculas(texto):
    """
    (manipulación de cadenas)
    recibe: cadena de texto
    convierte el texto a minusculas
    devuelve: la cadena con todas las letras del texto
    en minusculas
    """
    return texto.lower()

def normalizar_dia(texto):
    """
    (manipulación de cadenas)
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
    (manipulación de cadenas)
    recibe:  nombre de la materia escrito por el usuario
    quita espacios que sobran y pone mayúscula al inicio de cada palabra
    devuelve: el nombre de la materia formateado
    """
    materia = materia.strip()
    materia = materia.split()
    materia = " ".join(materia)
    materia = materia.title()
    return materia


def validar_horario(hora_inicio, hora_fin):
    """
    (uso de operadores, funciones, condicionales)
    recibe: hora_inicio valor numérico, hora_fin valor numérico
    calcula la duración de la materia al restar hora_inicio a hora_fin
    comprueba que sea positiva, si la resta es mayor que 0
    devuelve: valor booleano (True o False)
    """
    duracion = hora_fin - hora_inicio
    if duracion <= 0:
        return False
    return True


def mostrar_horario(horario):
    """
    (uso de funciones, condicionales, ciclos)
    recibe: listas de materias, dias, horas_inicio, horas_fin
    imprime los detalles de las materias registradas mediante un bucle
    No devuelve un valor
    """
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    i = 0
    while i < len(dias):
        j = 0
        while j < len(horario):
            if normalizar_dia(dias[i]) == normalizar_dia(horario[j][1]):
                print(f"Materia: {formatear_materia(horario[j][0])} | Día: {dias[i]}"
                f" | Hora de inicio: {horario[j][2]}"
                f" | Hora de fin: {horario[j][3]}")
            j+=1
        i+=1



def hay_empalme(horario, dia, hora_inicio, hora_fin):
    """
    (uso de funciones, condicionales, ciclos)
    recibe: listas de materias, dias, horas_inicio, horas_fin
    y variables de dia, hora_inicio, hora_fin
    compara un día y horario específicos contra las listas de horarios
    de las materias ya registradas para verificar si se empalman.
    devuelve: valor booleano (True o False)
    """
    i = 0
    ren = len(horario)
    while i < ren:
            if (normalizar_dia(dia) == normalizar_dia(horario[i][1]) and hora_inicio < horario[i][3]
                 and hora_fin > horario[i][2]):
                return True
            i+=1
    return False


def agregar_materias(horario, materia, dia, hora_inicio, hora_fin):
    """
    (uso de funciones)
    recibe: matriz de horario
    y variables de materia, dia, hora_inicio, hora_fin
    crea una fila con los datos de la materia
    y la añade a la matriz.
    No devuelve nada
    """
    lista = [materia, dia, hora_inicio, hora_fin]
    horario.append(lista)


horario = []

continuar = True
contador = 0

# Ciclo que se repite mientras el usuario quiera agregar materias
while continuar:
    materia = input("Materia: ")
    dia = input("Día: ")

    while not validar_dia(dia):
        print("Día inválido. Escribe un día de lunes a viernes.")
        dia = input("Día: ")

    hora_inicio = int(input("Hora inicio: "))
    hora_fin = int(input("Hora fin: "))

    # Si el horario no es válido, se vuelve a pedir la materia
    if not validar_horario(hora_inicio, hora_fin):
        print("La hora de fin debe ser mayor que la hora de inicio")
        continue

    # Se revisa si hay empalme con alguna materia ya registrada
    empalme = hay_empalme(horario, dia, hora_inicio, hora_fin)

    # Si hay empalme se avisa al usuario
    if empalme:
        print("Hay empalme entre las dos materias.")
    else:
        # Si no hay empalme, se registra la materia
        agregar_materias(horario, materia, dia, hora_inicio, hora_fin)
        contador += 1

    respuesta = int(input("¿Desea agregar otra materia? (si = 1/no = 0)"))
    continuar = respuesta == 1

print("El número de materias inscritas es:", contador)
print("Detalles de tu horario:")

mostrar_horario(horario)