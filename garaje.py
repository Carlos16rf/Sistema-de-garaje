from coche import Coche  # Importamos la clase Coche

class Garaje:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.vehiculos = []  # Lista para almacenar los coches en el garaje
    
    def agregar_coche(self, coche):
        if len(self.vehiculos) < self.capacidad:
            self.vehiculos.append(coche)
            print(f"Coche {coche.matricula} ingresado al garaje.")
        else:
            print("Garaje lleno. No se puede agregar más coches.")
            
    def listar_coches(self):
        print("Coches actualmente en el garaje:")
        for coche in self.vehiculos:
            print(coche.matricula)
    
    def contar_coches(self):
        numero_coche = len(self.vehiculos)
        print(f"Hay {numero_coche} coches en el garaje.")
        return numero_coche
