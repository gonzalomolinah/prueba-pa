# Tarea 1: DCCasillas 4️⃣➕5️⃣🟰9️⃣

## Consideraciones generales :octocat:

Todas las funciones de Tablero y DCCasillas se encuentran totalmente funcionales menos ```encontrar_solucion```. Todos los test cases estan aprobados. El menu esta totalmente funcional. Cumple con PEP8 y modularizacion.
Las explicaciones de los metodos realizados se encuentran como comentarios dentro del codigo.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️

#### ```Tablero```
##### ✅ ```__init__```

Crea un tablero vacío (```list[list[str]]```), inicializa ```movimientos = 0``` y ```estado = False```.

##### ✅ ```cargar_tablero```

Abre el archivo de configuración, lee su contenido y arma ```self.tablero``` con las celdas como str (mantiene . para espacios vacíos).

##### ✅ ```mostrar_tablero```

Imprime el tablero en consola, fila por fila, para visualizar el estado actual.

##### ✅ ```modificar_casilla```

Valida tipos y rangos. Alterna la celda entre habilitada/deshabilitada (p. ej., con un prefijo 'X') y suma 1 a movimientos. Retorna True/False según si la acción fue válida.

##### ✅ ```validar```

Verifica si la configuración actual del tablero cumple las metas/condiciones del enunciado (por filas/columnas u objetivos definidos). Actualiza self.estado y retorna True/False.

##### 🟠 ```encontrar_solucion```

Versión mínima: si el tablero ya es válido, retorna el mismo tablero; en otro caso retorna ```None```. Pendiente: que encuentre la solución y retorne una copia de una solución sin alterar el estado actual del tablero.
Solo entrega el tablero correcto cuando no es necesario encontrar solución (1/10 tests).

---

#### ```DCCasillas```
##### ✅ ```__init__```

Guarda usuario, inicia ```puntaje = 0```, prepara la lista de tableros y ```tablero_actual = None```.

##### ✅ ```abrir_tablero```

Selecciona el tablero en juego por índice y asigna self.tablero_actual.

##### ✅ ```guardar_estado```

Escribe data/{usuario}.txt con: cantidad de tableros y sus movimientos, dimensiones y el tablero completo. Retorna ```True``` si el guardado funciona (usuario válido y hay tableros), ```False``` en caso contrario.

##### ✅ ```recuperar_estado```

Lee data/{usuario}.txt, reconstruye la lista de tableros. Proceso inverso a ```guardar_estado```.

#### Menú
##### ✅ Consola

Interfaz por terminal con validación básica de entradas con el módulo ```funciones.py```.

##### ✅ Menú de Inicio

Opciones pedidas, cada una llama al método correspondiente.

##### ✅ Menú de Acciones

Opciones pedidas, cada una llama al método correspondiente.

##### ✅ Modularización

Código separado en módulos: ```tablero.py```, ```dccasillas.py```, ```funciones.py```, ```main.py```. Dentro de ```funciones.py``` y ```main.py``` se segmenta el codigo mediante funciones para reciclar código.

##### ✅ PEP8
Cumple con las normas de PEP8

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```, para ejecutarlo simplemente se debe correr ```python3 main.py``` (o ```py```/```python``` dependiendo de la versión). Además se debe crear los siguientes archivos y directorios adicionales:
1. ```configuracion.txt``` en ```/config```
2. Se necesita el modulo ```visualizador.pyc```

El código está pensado para ejecutarse en Python 3.12.9, por lo que se aconseja usar esta versión o alguna 3.12.X (otras versiones podrían funcionar, pero no se puede asegurar que no ocurran errores).

## Librerías :books:

### Librerías externas utilizadas
La lista de librerías externas que utilicé fueron las siguientes:

1. ```os```: ```path / DCCasillas y Tablero```
Se usó ```path.join()``` para crear las rutas de los archivos, y ```path.isfile()``` para confirmar la existencia de un archivo.

### Librerías propias
Se creo el modulo funciones que cuenta con 3 funciones para validar la entrada de los usuarios. La explicacion de estas se encuentra comentada en el mismo codigo
1. ```funciones```: Contiene a ```validar_numero```, ```validar_nombre``` y ```validar_configuracion```


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. En el caso de la opcion 1 del menu principal. si el usuario selecciona esta opcion y ya tiene un usuario creado, se le da la opcion de cambiar el nombre o volver al menu anterior.


-------



## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions>: simplemente valida que exista un archivo en un directorio y está implementado en el archivo ```tablero.py``` en las líneas 58 y 59. ```os.path.isfile``` devuelve un booleano si es que existe o no el archivo
