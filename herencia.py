class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def presentar(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años y soy {self.nacionalidad}.")

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    def presentar(self):
        print(f'''Hola, me llamo {self.nombre}, \n
              tengo {self.edad} años, \n
              soy {self.nacionalidad},\n
              trabajo como {self.trabajo} \n
              y mi salario es de {self.salario}''')
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, carrera, promedio):
        super().__init__(nombre, edad, nacionalidad)
        self.carrera = carrera
        self.promedio = promedio

    def presentar(self):
        print(f'''Hola, me llamo {self.nombre}, \n
              tengo {self.edad} años, \n
              soy {self.nacionalidad},\n
              estudio la carrerda de {self.carrera} \n
              y mi promedio es de {self.promedio}''')

persona1 = Empleado('Roberto', 30, 'ecuatoriano', 'Programador', 100000)

persona2 = Persona('Diego', 30, 'ecuatoriano')

persona3 = Estudiante('Rodrigo', 20, 'ecuatoriano', 'Matemática', 9.5)

persona1.presentar()

persona2.presentar()

persona3.presentar()

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f' Mi habilidad es: {self.habilidad}')    

#HERENCIA MÚLTIPLE
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        return f'{super().mostrar_habilidad()}'
    
    def mostrar_habilidad(self):
        print(f''' Hola, mi nombre es {self.nombre}, \n
              Mi habilidad es {self.habilidad}, \n
              y trabajo eb {self.empresa}''')
    
persona4 = EmpleadoArtista('Carlos', 38, 'ecuatoriano', 'cantar', 1200, 'AAAA')

persona4.presentarse()

persona4.mostrar_habilidad()

herencia = issubclass(EmpleadoArtista, Persona)

instancia = isinstance(persona4, EmpleadoArtista)

print(herencia)

print(instancia)