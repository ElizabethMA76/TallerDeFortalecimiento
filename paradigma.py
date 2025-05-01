class Estudiante:
    def _init_(self, nombre, cal1, cal2, cal3):
        self.nombre = nombre
        self.cal1 = cal1
        self.cal2 = cal2
        self.cal3 = cal3

    def calcular_promedio(self):
        return (self.cal1 + self.cal2 + self.cal3) / 3

    def resultado(self):
        promedio = self.calcular_promedio()
        return "Aprobado" if promedio >= 6 else "Reprobado"


# Captura de datos por teclado
nombre = input("Ingresa el nombre del estudiante: ")
cal1 = float(input("Ingresa la primera calificación: "))
cal2 = float(input("Ingresa la segunda calificación: "))
cal3 = float(input("Ingresa la tercera calificación: "))

est = Estudiante(nombre, cal1, cal2, cal3)
print(f"{est.nombre} tiene un promedio de {est.calcular_promedio():.2f} y está {est.resultado()}")