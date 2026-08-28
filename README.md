# Gestor de Horarios

## Contexto
Tener un horario organizado es un factor muy importante para el éxito de un estudiante universitario ya que le permite planificar su día a día, optimizar su tiempo y mejorar su desempeño académico.

Este programa es un gestor de horarios diseñado para ayudar a los estudiantes a organizar sus actividades cotidianas eficientemente. El programa corre en la terminal utilizando Python 3. Permite al usuario registrar, consultar y modificar su horario, dependiendo de sus actividades escolares o extraescolares, así como encontrar posibles empalmes entre ellas y evitar conflictos de agenda. 


## Pseudocódigo

```text
EO(materia, dia, hora_inicio, hora_fin)

//Declaración de arreglos donde guardaremos los datos necesarios para registrar y organizar las materias.

  materias = []
  dias = []
  horas_inicio = []
  horas_fin = []
  continuar = 1

  i = 0

// Ciclo que se mantiene activo mientras el usuario siga añadiendo materias.
  mientras (continuar == 1)
    leer materia
    leer dia
    leer hora_inicio
    leer hora_fin

//Se recorre el arreglo de materias
    ciclo (i en materias)

//Se verifica que no haya empalme comprobando si el día es el mismo y si las horas chocan mediante operadores de comparación.
      si(dia == dias[i] y hora_inicio < horas_fin[i] y hora_fin > horas_inicio[i])

        Imprimir("Existe un empalme en el horario")
  
      i = i + 1

//Si no hay empalme se añaden los datos a los arreglos correspondientes.

    añadir materia a materias
    añadir dia a dias
    añadir hora_inicio a horas_inicio
    añadir hora_fin a horas_fin

    Imprimir("¿Desea agregar otra materia? (si = 1/no = 0)")
      leer continuar

EF(materias, dias, horas_inicio, horas_fin)
  


