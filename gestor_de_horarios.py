#Declaración de arreglos donde guardaremos los datos necesarios para registrar y organizar las materias.
materias = []
dias = []
horas_inicio = []
horas_fin = []

#Declaración de variable booleana que permite el ciclo while
continuar = True

#Ciclo que se mantiene activo mientras el usuario siga añadiendo materias.
while(continuar):

    materia = input("Materia:")
    dia = input("Día:")
    hora_inicio = int(input("Hora i:"))
    hora_fin = int(input("Hora f:" ))
    i=0
    #Se recorre el arreglo de materias
    for i in range(len(materias)):
        #Se verifica que no haya empalme comprobando si el día es el mismo y si las horas chocan mediante operadores de comparación.
        if(dia == dias[i] and hora_inicio < horas_fin[i] and hora_fin > horas_inicio[i]):
            print("Existe un empalme en el horario")
        i+=1

    #Si no hay empalme se añaden los datos a los arreglos correspondientes.
    materias.append(materia)
    dias.append(dia)
    horas_inicio.append(hora_inicio)
    horas_fin.append(hora_fin)
        
    respuesta = int(input("¿Desea agregar otra materia? (si = 1/no = 0)"))
    continuar = respuesta == 1
            