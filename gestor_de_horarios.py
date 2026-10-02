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


def mostrar_horario(materias, dias, horas_inicio, horas_fin):
    """
    (uso de funciones, condicionales, ciclos)
    recibe: listas de materias, dias, horas_inicio, horas_fin
    imprime los detalles de las materias registradas mediante un bucle
    No devuelve un valor
    """
    for i in range(len(materias)):
        print(f"Materia: {materias[i]} | Día: {dias[i]}"
              f" | Hora de inicio: {horas_inicio[i]}"
              f" | Hora de fin: {horas_fin[i]}")


def hay_empalme(materias, dia, dias, hora_inicio,
                horas_inicio, hora_fin, horas_fin):
    """
    (uso de funciones, condicionales, ciclos)
    recibe: listas de materias, dias, horas_inicio, horas_fin
    y variables de dia, hora_inicio, hora_fin
    compara un día y horario específicos contra las listas de horarios
    de las materias ya registradas para verificar si se empalman.
    devuelve: valor booleano (True o False)
    """
    for i in range(len(materias)):
        if (dia == dias[i] and hora_inicio < horas_fin[i]
                and hora_fin > horas_inicio[i]):
            return True

    return False


def agregar_materias(materias, materia, dia, dias, hora_inicio,
                     horas_inicio, hora_fin, horas_fin):
    """
    (uso de funciones)
    recibe: listas de materias, dias, horas_inicio, horas_fin
    y variables de materia, dia, hora_inicio, hora_fin, contador
    agrega una materia, su día y su horario a las listas
    correspondientes e incrementa el contador.
    No devuelve nada
    """
    materias.append(materia)
    dias.append(dia)
    horas_inicio.append(hora_inicio)
    horas_fin.append(hora_fin)


materias = []
dias = []
horas_inicio = []
horas_fin = []

continuar = True
contador = 0

while continuar:
    materia = input("Materia: ")
    dia = input("Día: ")
    hora_inicio = int(input("Hora inicio: "))
    hora_fin = int(input("Hora fin: "))

    if not validar_horario(hora_inicio, hora_fin):
        print("La hora de fin debe ser mayor que la hora de inicio")
        continue

    empalme = hay_empalme(materias, dia, dias, hora_inicio,
                          horas_inicio, hora_fin, horas_fin)

    if empalme:
        print("Hay empalme entre las dos materias.")
    else:
        agregar_materias(materias, materia, dia, dias, hora_inicio,
                         horas_inicio, hora_fin, horas_fin)
        contador += 1

    respuesta = int(input("¿Desea agregar otra materia? (si = 1/no = 0)"))
    continuar = respuesta == 1

print("El número de materias inscritas es:", contador)
print("Detalles de tu horario:")

mostrar_horario(materias, dias, horas_inicio, horas_fin)