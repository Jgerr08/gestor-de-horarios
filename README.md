# Gestor de Horarios

## Contexto
Como experiencia personal, la universidad me ha hecho cambiar muchos hábitos negativos que iba arrastrando desde etapas anteriores. Ahora, a una semana de cerrar el semestre,puedo mirar atrás y decir que lo que más me costó cambiar es la administración del tiempo.
Por eso decidí crear como proyecto un gestor de horarios, ya que la organización es un factor que influye en el éxito de un estudiante universitario y que le permite planificar sus actividades diarias y aprovechar mejor su día. Contar con una herramienta como esta que permita organizar sus actividades puede facilitar el manejo del tiempo de cualquier estudiante.

En 2015 se realizó un estudio con 494 estudiantes de primer año de universidad, en donde se comparaba el manejo del tiempo de los alumnos con mejores calificaciones contra los de peores calificaciones.Como resultado, se encontraron claras diferencias a favor en el manejo del tiempo por parte de los alumnos de mejor desempeño (Garzón y Gil, 2018). Fuente: https://www.redalyc.org/journal/298/29858802008/html/

Este programa es un gestor de horarios diseñado para ayudar a los estudiantes como yo a organizar sus actividades cotidianas eficientemente. Este se puede ejecutar en la terminal utilizando Python 3.

## Funcionamiento del programa

El programa tiene un menú que permite seleccionar 4 opciones:
1. Permite al usuario registrar materias mientras él lo desee, indicando el día y la hora correspondiente como entrada. En el proceso de agregar cada materia, el programa toma en cuenta las materias ya existentes y las compara con las propuestas por el usuario para encontrar posibles empalmes. Si este es el caso, el programa le avisa al usuario de esta situación, no agrega la materia y le pregunta si desea continuar agregando. Al final, muestra el horario ordenado de forma correcta desplegando todas las materias guardadas para que el usuario pueda consultar su horario.
2. Permite al usuario cargar un archivo de horario para que lo pueda visualizar y modificar posteriormente. Se verifica que exista en la ruta de la carpeta del programa y se carga a la matriz de horario.
3. Permite al usuario eliminar materias manualmente. Si la matriz de horario incluye alguna materia, le se muestra en consola junto con las posiciones de las materias para que pueda seleccionar la que va a eliminar. Después se realiza una validación para evitar error de indice en la matriz, para luego pasar a borrar la materia directamente.
4. Muestra los detalles el horario actual incluyendo cantidad de horas por semana y número de materias inscritas en caso de que existan materias en la matriz. De lo contrario avisa al usuario que no hay materias registradas.

Si se selecciona algún otro número diferente a estos marca Opción no válida.

## Uso de bibliotecas con OS

Importé el módulo `os`, que es parte de la biblioteca estándar de Python y usé la función `os.path.exists()` para comprobar si el archivo seleccionado realmente existe en la ruta donde corre el programa.
Esto lo apliqué en la función `existe_archivo` para que en mi programa hubiera una validación para verificar esto y evitar que este se detenga con un error si el usuario escribe algún archivo que no existe.

## Instrucciones
Descargar el archivo y correr en terminal con:

```
python gestor_de_horarios.py
```

En Mac o Linux puede ser necesario usar :
```
python3 gestor_de_horarios.py
```

# Correcciones
Durante el semestre, recibí diversas recomendaciones en los avances del proyecto por parte de los becarios. A continuación se describen los cambios realizados.

## Corrección 1
Sub-Competencia: Usa la forma más apropiada al problema para guardar los datos (matrices) (avance 7).

Error original: Las materias se imprimían en el orden que se iban registrando por lo que al mostrarlas el horario salía desordenado y difícil de leer.

Cambio realizado: En la función `mostrar_horario` agregué una lista con los días hábiles de la semana. Se realizan ciclos anidados donde se realiza una comparación entre cada día con la columna del día de la matriz para imprimirlas en orden. Lo apliqué también a la función `mostrar_horario_enumerado` que se usa en la opción 3.

```
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    i = 0
    print(f"{'Materia':<32}{'Dia':<16}{'Hora inicio':<16}Hora fin")
    while i < len(dias):
        j = 0
        while j < len(horario):
            if normalizar_dia(dias[i]) == normalizar_dia(horario[j][1]):
                print(f"{formatear_materia(horario[j][0]):<32}"
                      f"{dias[i]:<16}"
                      f"{horario[j][2]:<16}"
                      f"{horario[j][3]}")
            j += 1
        i += 1
```

Líneas de código donde se ve la corrección:

139 a 151 `mostrar_horario`
161 a 175 `mostrar_horario_enumerado`

## Corrección 2

Sub-Competencia: Manipula cadenas de forma útil (para validación, presentación y busqueda) (avance 8)

Error original: En este avance me sugirieron que agregara una función para eliminar materias en caso de que el usuario se equivocara.

Cambio realizado: Agregué la siguiente función en donde se crea una matriz nueva y le agrega todas las filas del horario excepto la de la posicion que recibe como parámetro. Al eliminarla se muestra el nombre de la materia con la función `formatear_materia`.

`def eliminar_materia(horario, pos)`

Líneas de código donde se ve la corrección:
238 a 254

## Corrección 3
Sub-Competencia:  Manipula cadenas de forma útil (para validación, presentación y búsqueda) (avance 8)

Error original: Como tal esto no me lo marcaron como error, pero yo noté que al mostrar las materias cuando usaba el caracter tab `\t` había mucha inconsistencia en el alineado del texto de la tabla.
```
print("Materia\t\tDia\t\tHora inicio\tHora fin")
```

```
print(f"{formatear_materia(horario[j][0])}\t\t"
f"{dias[i]}\t\t"
f"{horario[j][2]}\t\t"
f"{horario[j][3]}")
```

Cambio realizado: Ya tenía algo de experiencia usando el especificador de formato `:<` en f-strings, pero de igual forma revisé su documentación y lo apliqué en las filas y los encabezados para que cada dato de la columna ocupe siempre 16 caracteres (excepto los nombres de las materias que ocupan 32 porque suelen ser más largos) y quede alineado a la izquierda.
```
print(f"{'Materia':<32}{'Dia':<16}{'Hora inicio':<16}Hora fin")
```

```
print(f"{j+1:<16}"
f"{formatear_materia(horario[j][0]):<32}"
f"{dias[i]:<16}"
f"{horario[j][2]:<16}"
f"{horario[j][3]:<16}")
```


Líneas de código donde se ve la corrección:
141 a 149 mostrar_horario(horario)
163 a 173 mostrar_horario_enumerado(horario)


# Referencias
Garzón & Gil (2018). Gestión del tiempo en alumnado universitario con diferentes niveles de rendimiento académico. https://www.redalyc.org/journal/298/29858802008/html/

Python Software Foundation. (2026). os.path.exists(). Python 3.15.2 documentation. https://docs.python.org/3/library/os.path.html#os.path.exists

Python Software Foundation. (2026). Format Specification Mini-Language. Python 3.15.2 documentation. https://docs.python.org/3/library/string.html#format-specification-mini-language
