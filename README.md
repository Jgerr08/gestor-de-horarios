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

# Referencias
