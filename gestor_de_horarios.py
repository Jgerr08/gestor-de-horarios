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
    (uso de funciones, condicionales, ciclos for)
    recibe: listas de materias, dias, horas_inicio, horas_fin
    imprime los detalles de las materias registradas mediante un bucle
    No devuelve un valor
    """
    for i in range(len(horario)):
        print(f"Materia: {horario[i][0]} | Día: {horario[i][1]}"
              f" | Hora de inicio: {horario[i][2]}"
              f" | Hora de fin: {horario[i][3]}")


def hay_empalme(horario, dia, hora_inicio, hora_fin):
    """
    (uso de funciones, condicionales, ciclos while)
    recibe: listas de materias, dias, horas_inicio, horas_fin
    y variables de dia, hora_inicio, hora_fin
    compara un día y horario específicos contra las listas de horarios
    de las materias ya registradas para verificar si se empalman.
    devuelve: valor booleano (True o False)
    """
    i = 0
    ren = len(horario)
    while i < ren:
            if (dia == horario[i][1] and hora_inicio < horario[i][3]
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
    y las añade a la matriz.
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