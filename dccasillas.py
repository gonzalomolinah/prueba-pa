
from tablero import Tablero
from os import path

class DCCasillas: 

    def __init__(self, usuario:str, config:str) -> None:
        # Parametros iniciales
        self.usuario: str = usuario
        self.puntaje: int = 0
        self.tablero_actual: int | None = None
        self.tableros: list[Tablero] = []

        # Abrir el archivo de configuracion para obtener los tableros
        with open(path.join("config", config), "r", encoding="utf-8") as f:
            lista = [linea.strip() for linea in f]
            n = int(lista[0])

            for i in range(1, n+1):
                archivo = lista[i]

                tab = Tablero()
                tab.cargar_tablero(archivo)
                self.tableros.append(tab)

    def abrir_tablero(self, num_tablero:int) -> None:
        self.tablero_actual = num_tablero

    def guardar_estado(self) -> bool: 
        # Validacion
        if len(self.tableros) == 0:
            return False
        if self.usuario == "":
            return False
        
        # Abre el archivo/sobreescribe, y guarda los datos
        with open(path.join("data", f"{self.usuario}.txt"), "w", encoding="utf-8") as f:
            cantidad_tableros = len(self.tableros)
            print(cantidad_tableros, file=f)
            for i in range(cantidad_tableros):
                tablero = self.tableros[i]
                n = len(tablero.tablero)
                m = len(tablero.tablero[0])
                print(tablero.movimientos, file=f)
                print(n - 1, m - 1, file=f)
                for j in range(n):
                    linea = " ".join(tablero.tablero[j])
                    print(linea, file=f)
        return True


    def recuperar_estado(self) -> bool:
        # Validacion
        if self.usuario == "":
            return False
        if path.isfile(f"data/{self.usuario}.txt") == False:
            return False
        
        # Lo mismo que en guardar_estado pero un proceso inverso
        with open(path.join("data", f"{self.usuario}.txt"), "r", encoding="utf-8") as f:
            lista = [linea.strip().split() for linea in f]
            for linea in lista:
                for caracter in linea:
                    if "-" in caracter:
                        return False

            if len(lista[0]) != 1:
                return False
            
            if len(lista) == 0:
                return False
            
            cantidad_tableros = int(lista[0][0])

            self.tableros = []
            indice = 1
            
            while indice < len(lista):
                if len(lista[indice + 1]) != 2:
                    return False
                
                tablero = Tablero()
                tablero.movimientos = int(lista[indice][0])
                n = int(lista[indice + 1][0])
                m = int(lista[indice + 1][1])
                

                tablero_temporal = lista[indice + 2: indice + 3 + n]
                tablero.tablero = tablero_temporal
                self.tableros.append(tablero)
                indice += 3 + n
                tablero.estado = tablero.validar()
        return True
