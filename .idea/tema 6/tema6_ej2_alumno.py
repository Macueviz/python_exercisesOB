class Alumno():
    def inicio(self, nombre,nota):
       self.nombre = nombre
       self.nota = nota

    def resultado(self):
        if self.nota >= 5:
            print(f"la nota de {self.nombre} es {self.nota} y ha aprobado")
        else:
            print(f"la nota de {self.nombre} es {self.nota} y no ha aprobado")

alumno1= Alumno()
alumno2= Alumno()
alumno1.inicio("Miguel", 5)
alumno2.inicio("Sophi", 3)

alumno1.resultado()
alumno2.resultado()

