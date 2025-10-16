import visualizador
from os import path

class Tablero:

    def __init__(self) -> None:
        # Parametros iniciales del enunciado
        self.tablero: list[list[str]] = []
        self.movimientos: int = 0
        self.estado: bool = False

    def cargar_tablero(self, archivo:str) -> None:

        # Abre la ruta del archivo, crea una lista con comprension de listas, y agrega todo

        with open(path.join("config", archivo), "r", encoding="utf-8") as f:
            lista = [linea.strip().split() for linea in f]
            n = lista[0][0]
            m = lista[0][1]
            datos = lista[1:]
            self.tablero = datos

    def mostrar_tablero(self) -> None:
        visualizador.imprimir_tablero(self.tablero)

    def modificar_casilla(self, fila:int, columna:int) -> bool:
        # Validacion
        if type(fila) != int or type(columna) != int:
            return False
        n = len(self.tablero)
        m = len(self.tablero[0])
        if fila < 0 or fila >= n or columna < 0 or columna >= m:
            return False
        if self.tablero[fila][columna] == ".":
            return False
        
        # Busca el dato, si hay una X la saca, de lo contrario la suma
        caracter = self.tablero[fila][columna]
        self.movimientos += 1
        if "X" in caracter:
            self.tablero[fila][columna] = caracter[-1]
        else:
            self.tablero[fila][columna] = "X" + caracter
        return True

    def validar(self) -> bool:
        n = len(self.tablero)
        m = len(self.tablero[0])

        #Revisar las filas primero
        for i in range(n-1):
            objetivo = self.tablero[i][-1]
            if objetivo != ".":
                suma = 0
                for j in range(m-1):
                    if "X" in self.tablero[i][j] or "." in self.tablero[i][j]:
                        pass
                    else:
                        suma += int(self.tablero[i][j])
                if suma != int(objetivo):
                    self.estado = False
                    return False
        
        #Revisar las columnas (quizas lo puse al reves pero da un poco lo mismo)
        for j in range(m-1):
            objetivo = self.tablero[-1][j]
            if objetivo != ".":
                suma = 0
                for i in range(n-1):
                    if "X" in self.tablero[i][j] or "." in self.tablero[i][j]:
                        pass
                    else:
                        suma += int(self.tablero[i][j])
                if suma != int(objetivo):
                    self.estado = False
                    return False
        
        self.estado = True
        return True

    def encontrar_solucion(self):
        
        # Por ahora solo revisa si el estado actual es valido
        if self.validar():
            tablero_nuevo = Tablero()
            tablero_nuevo.tablero = self.tablero.copy()
            return tablero_nuevo
        return None


