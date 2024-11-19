class A:
    def hablar(self):
        print('Hola desde A')

class B(A):
    def hablar(self):
        print('Hola desde B')
    
class C(A):
    def hablar(self):
        print('Hola desde C')   

class D(B,C):
    def hablar(self):
        print('Hola desde D')   
    #pass 

d = D()

d.hablar() #PRIORIDAD D->B->C->A

#GRAFOS DIRIGIDOS!! COMO HACER EL GRAFO 

print(D.mro())

A.hablar(d)
