def validar_horario(hora_inicio, hora_fin):
    """
    (uso de operadores, funciones, condicionales)
    recibe: hora_inicio valor numérico, hora_fin valor numérico
    calcula la duración de la materia al restar hora_fin a hora_inicio
    comprueba que sea positiva, si la resta es mayor que 0  
    devuelve: valor booleano (True o False)
    """
    duracion = hora_fin - hora_inicio
    if duracion <= 0:
        return False
    return True


# Declaración de arreglos
materias = []
dias = []
horas_inicio = []
horas_fin = []

# Declaración de variable booleana que permite el ciclo while
continuar = True
contador = 0
# Ciclo que se mantiene activo mientras el usuario siga añadiendo materias.
while continuar:

    materia = input("Materia: ")
    dia = input("Día: ")
    hora_inicio = int(input("Hora inicio: "))
    hora_fin = int(input("Hora fin: "))
    empalme = False

    if not validar_horario(hora_inicio, hora_fin):
        print("La hora de fin debe ser mayor que la hora de inicio")
        continue

    # Se recorre el arreglo de materias
    for i in range(len(materias)):

        # Se verifica que no haya empalme 
        if (dia == dias[i] and hora_inicio < horas_fin[i]
                and hora_fin > horas_inicio[i]):

            print("Existe un empalme en el horario")
            empalme = True
            break
            

    # Si no hay empalme se añaden los datos a los arreglos correspondientes.
    if not empalme: 
        materias.append(materia)
        dias.append(dia)
        horas_inicio.append(hora_inicio)
        horas_fin.append(hora_fin)
        contador += 1
        
    respuesta = int(input("¿Desea agregar otra materia? (si = 1/no = 0)"))
    continuar = respuesta == 1 

print("El número de materias inscritas es:", contador)
print("Detalles de tu horario:")

for m in range(len(materias)):
    print(f"Materia: {materias[m]} | Día: {dias[m]}"
          f"| Hora de inicio: {horas_inicio[m]} | Hora de fin: {horas_fin[m]}")