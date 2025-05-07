from cola import Cola

class Banco:
    def __init__(self):
        self.cola_clientes = Cola()
        self.ultimo_cliente = None

    def llega_cliente(self, nombre):
        self.cola_clientes.encolar(nombre)

    def atender_cliente(self):
        self.ultimo_cliente = self.cola_clientes.desencolar()
        return self.ultimo_cliente

    def obtener_clientes_en_espera(self):
        return self.cola_clientes.mostrar()

    def obtener_ultimo_atendido(self):
        return self.ultimo_cliente
