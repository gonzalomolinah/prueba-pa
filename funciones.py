

# Valida que un string sea solo numeros
def validar_numero(entrada: str) -> bool:
    for caracter in entrada:
        if caracter not in "0123456789":
            return False
    return True

# Valida que un string sea solo letras o numeros, 
# para no tener problemas con los directorios
def validar_nombre(entrada: str) -> bool:
    if len(entrada) == 0:
        return False
    for caracter in entrada:
        if caracter.lower() not in "abcdefghijklmnñopqrstuvwxyz0123456789_":
            return False
    return True

# Lo mismo pero con el archivo de config
def validar_configuracion(entrada: str) -> bool:
    if len(entrada) < 4:
        return False
    if entrada[-4:] != ".txt":
        return False
    for caracter in entrada[:-4]:
        if caracter.lower() not in "abcdefghijklmnñopqrstuvwxyz0123456789_":
            return False
    return True
