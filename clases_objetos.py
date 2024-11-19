class Celular:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def llamar(self):
        print(f'Estas llamando a alguien desde un {self.modelo}')
    def cortar(self):
        print(f'Cortaste la llamada desde un {self.modelo}')

celular1 = Celular("Apple", "iPhone 13", "Negro")
celular2 = Celular("Samsung", "Galaxy S21", "Azul")   

celular1.llamar()
celular2.cortar()


