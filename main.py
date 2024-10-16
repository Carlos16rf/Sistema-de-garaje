from coche import Coche
from garaje import Garaje
from time import sleep

def prueba_garaje():
    # Crear un garaje con capacidad para 3 coches
    garaje = Garaje(capacidad=3)
    
    # Crear algunos coches (ingreso de coches)
    coche1 = Coche(matricula="ABC123")
    coche2 = Coche(matricula="XYZ789")
    
    # Agregar coches al garaje
    garaje.agregar_coche(coche1)
    garaje.agregar_coche(coche2)
    
    # Esperar unos segundos para simular que el coche estuvo estacionado un tiempo
    print("Simulando el tiempo de estacionamiento... (espera unos segundos)")
    sleep(5)  # Esto simula que han pasado 5 segundos
    
    # Registrar la salida de un coche y calcular el tiempo
    coche1.registrar_salida()
    tiempo_estacionado = coche1.calcular_tiempo()
    print(f"El coche {coche1.matricula} estuvo estacionado durante {tiempo_estacionado:.2f} horas.")
    
    # Calcular el costo por el tiempo estacionado
    pago = coche1.money()
    print(f"El coche {coche1.matricula} debe pagar ${pago:.2f}.")

    # Listar los coches que aún están en el garaje
    garaje.listar_coches()
    
    # Contar los coches en el garaje
    garaje.contar_coches()

# Llamar a la función de prueba
prueba_garaje()
