class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad
    
    def set_edad(self, new_edad):
        self._edad = new_edad

# Creating an instance of Persona
dalton = Persona('Dalt', 20)

# Accessing the private attributes (not recommended to directly access)
print(dalton._nombre)
print(dalton._edad)

# Using getters to retrieve values
nombre = dalton.get_nombre()
edad = dalton.get_edad()
print(f'El nombre es {nombre} y la edad es {edad}')

# Updating edad using the setter
dalton.set_edad(30)

# Retrieving the updated edad
edad = dalton.get_edad()  # Update edad to get the new value
print(f'El nombre es {nombre} y la edad es {edad}')
