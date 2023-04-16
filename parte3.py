from parte1 import calificaciones
from parte2 import nota_final

class Aprobado:
    def __init__(self, nota_final, asistencia, parcial1, parcial2, practicas, aprobado):
        self.nota_final = nota_final
        self.asistencia = asistencia
        self.practicas = practicas
        self.aprobado = aprobado
        self.parcial1 = parcial1
        self.parcial2 = parcial2

        def alumno_aprobado(self):
            if self.nota_final >= 5 and self.asistencia >= 75 and self.parcial1 >= 4 and self.parcial2 >= 4 and self.practicas >= 4:
                self.aprobado = True
                print("El alumno está aprobado")
            else:
                self.aprobado = False
                print("El alumno está suspenso")
            return self.aprobado
