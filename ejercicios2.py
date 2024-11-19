class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años' )

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        Persona.__init__(self, nombre, edad)
        self.grado = grado
    
    def presentar(self):
        print(f'El grado que estoy cursando es {self.grado}')

persona1 = Estudiante('Carlos', 28, 'noveno')

Persona.presentar(persona1) #Llama a la función presentar de la clase persona

persona1.presentar() #Llama a la función presentar de la clase estudiante



