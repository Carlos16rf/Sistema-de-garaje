from datetime import datetime

class Coche:
    def __init__(self, matricula):
        self.matricula = matricula
        self.hora_entrada = datetime.now()
        self.hora_salida = None
        
    def registrar_salida(self):
        self.hora_salida = datetime.now()  
        
    def calcular_tiempo(self):
        if self.hora_salida is None:
            hora_actual = datetime.now()
            tiempo = hora_actual - self.hora_entrada
        else:
            tiempo = self.hora_salida - self.hora_entrada
        return tiempo.total_seconds() / 3600  # Devolver tiempo en horas
        
    def tiempo(self):
        matricula_buscada = input("Matrícula: ")
        if self.matricula == matricula_buscada:
            self.registrar_salida()
            tiempo_estacionado = self.calcular_tiempo()
            print(f"Tiempo estacionado: {tiempo_estacionado:.2f} horas")
            return tiempo_estacionado
        else:
            print("Matrícula no encontrada.")
            
    def money(self):
        precio_por_minuto = 0.85  # Ahora es un número flotante
        tiempo_horas = self.calcular_tiempo()
        tiempo_en_minutos = tiempo_horas * 60
        
        # Calcula el total a pagar
        total_a_pagar = tiempo_en_minutos * precio_por_minuto
        print(f"Total a pagar: ${total_a_pagar:.2f}")
        return total_a_pagar
