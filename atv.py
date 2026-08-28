from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass


class Carro(Veiculo):
    def acelerar(self):
        print(f"🚗 O carro {self.modelo} está acelerando rapidamente!")


class Moto(Veiculo):
    def acelerar(self):
        print(f"🏍️ A moto {self.modelo} está acelerando e ganhando velocidade!")


class Caminhao(Veiculo):
    def acelerar(self):
        print(f"🚚 O caminhão {self.modelo} está acelerando lentamente por causa do seu peso!")


# Bônus: nova classe utilizando a mesma interface
class CarroEletrico(Veiculo):
    def acelerar(self):
        print(f"🔋 O carro elétrico {self.modelo} está acelerando silenciosamente!")


# Lista heterogênea: diferentes tipos de veículos
pista_de_corrida = [
    Carro("Ferrari 488"),
    Moto("Yamaha R1"),
    Caminhao("Volvo FH"),
    CarroEletrico("Tesla Model 3")
]


# Simulação da corrida usando polimorfismo
for veiculo in pista_de_corrida:
    veiculo.acelerar()