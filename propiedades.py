class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_name):
        self.__nombre = new_name

    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
dalto = Persona('Lucas', 30)

nombre = dalto.nombre

print(nombre)

dalto.nombre = 'Juan'

nombre = dalto.nombre

print(nombre)