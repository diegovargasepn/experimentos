class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f'El estudiante {self.nombre} está estudiando.')
    
    def noestudiar(self):
        print(f'El estudiante {self.nombre} no está estudiando.')

nombre = input('Ingrese el nombre del estudiante: ')
edad = input('Ingrese la edad del estudiante: ')
grado = input('Ingrese el grado del estudiante: ')

estudiante1 = Estudiante(nombre, edad, grado)

status = input('Quiere estudiar? (s/n): ')

if status.lower() == 's':
    estudiante1.estudiar()
elif status.lower() == 'n':
    estudiante1.noestudiar()
else:
    print('Opcion invalida')

