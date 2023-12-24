# Programación Tradicional
                                        # Definición de variables globales
balan = 0
interest_rate = 0.05

                                           # Función para depositar dinero en la cuenta
def depost(amount):
    global balan
    balan += amount

                            # Función para retirar dinero de la cuenta
def withdraw(amount):
    global balan
    balan -= amount

# Función para calcular el interés y actualizar el saldo
def calculate_interest():
    global balan, interest_rate
    interest = balan * interest_rate
    balan += interest

                                               # Uso de las funciones en la programación tradicional
deposit(1000)
withdraw(500)
calculate_interest()

                                                 # Imprimir el saldo final
print("Balance (Traditional):", balance)


# Programación Orientada a Objetos (POO)
# Ejemplo: Gestión de una cuenta bancaria

class BankAccount:
    def __init__(self, initial_balan=0, interest_rate=0.05):
        self.balan = initial_balan
        self.interest_rate = interest_rate

    def depost(self, amount):
        self.balan += amount

    def withdraw(self, amount):
        self.balan -= amount

    def calculate_interest(self):
        interest = self.balan * self.interest_rate
        self.balance += interest

# Crear una instancia de la clase BankAccount
account = BankAccount()

# Uso de los métodos en la programación orientada a objetos
account.deposit(1000)
account.withdraw(500)
account.calculate_interest()

# Imprimir el saldo final
print("Balance (OOP):", account.balan)
