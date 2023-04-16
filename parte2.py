from parte1 import calificaciones

def nota_final(lista_diccionarios):
    for diccionario in lista_diccionarios:
        parcial1 = float(diccionario["Parcial1"]) * 0.3
        parcial2 = float(diccionario["Parcial2"]) * 0.3
        practicas = float(diccionario["Practicas"]) * 0.4
        diccionario["Nota final"] = parcial1 + parcial2 + practicas
    return lista_diccionarios


