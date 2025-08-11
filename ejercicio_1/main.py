from abc import ABC, abstractmethod

class Notificador:
    def __init__(self, ):
        pass

    
# Implementación Notificación
class Notificacion(ABC):
    
    @abstractmethod
    def enviar_notificacion(self, nombre_cliente: str):
        pass
    
class NotificacionSMS(Notificacion):
    
    def enviar_notificacion(self, nombre_cliente: str):
        print(f"Enviando notificación por SMS para {nombre_cliente}")
        
class NotificacionWhatsapp(Notificacion):
    
    def enviar_notificacion(self, nombre_cliente: str):
        print(f"Enviando notificación por Whatsapp para {nombre_cliente}")
        
class NotificacionSlack(Notificacion):
    
    def enviar_notificacion(self, nombre_cliente: str):
        print(f"Enviando notificación por Slack para {nombre_cliente}")
        
# Notificador
class Notificador():
    
    def __init__(self):
        pass
        
    def notificar(self, nombre_cliente:str, lista_notificaciones: list[Notificacion]):
        for notificacion in lista_notificaciones:
            notificacion.enviar_notificacion(nombre_cliente=nombre_cliente)
            
# Cliente

class Cliente():
    
    def __init__(self, nombre_cliente: str, lista_notificaciones: list[Notificacion]):
        self.notificador = Notificador()
        self.nombre_cliente = nombre_cliente
        self.lista_notificaciones = lista_notificaciones
        
    def notificar(self):
        self.notificador.notificar(self.nombre_cliente, self.lista_notificaciones)
        
    def set_lista_notificaciones(self, lista_notificaciones: list[Notificacion]):
        self.lista_notificaciones = lista_notificaciones
        
    def add_lista_notificaciones(self, notificacion: Notificacion):
        self.lista_notificaciones.append(notificacion)
        
# Uso

cliente_1 = Cliente("Cliente 1", [NotificacionSMS(), NotificacionSlack()])
cliente_2 = Cliente("Cliente 2", [NotificacionWhatsapp()])
cliente_3 = Cliente("Cliente 3", [NotificacionWhatsapp(), NotificacionSlack(), NotificacionSMS()])

print("Ejecución...")
print("Cliente 1")
cliente_1.notificar()
print("Cliente 2")
cliente_2.notificar()
print("Cliente 3")
cliente_3.notificar()
print("Añadiendo notificación a cliente 2")
cliente_2.add_lista_notificaciones(NotificacionSMS())
cliente_2.notificar()