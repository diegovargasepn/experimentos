class MiClase():
    def __init__(self):
        self._atributo_privado = 'valor' #Argumento privado, se puede acceder por consola

    def __hablar(self):
        print('hola como estas')

class MiClase2():
    def __init__(self):
        self.__atributivo_privado = 'color' #Argumento muy privado, no se accede directo por consola

objeto = MiClase()
objeto2 = MiClase2()
#print(objeto._atributo_privado)
#print(objeto._atributo_privado)
objeto.__hablar()
