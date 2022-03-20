#1
"""Diseñe e implemente la clase BankAccount, la misma debe contar con los siguientes
métodos:
deposit(amount) : deposita una cantidad de dinero que se debe comprobar
que sea positiva.
withdraw(amount): retira una cantidad de dinero que se debe comprobar
que sea positiva.
getBalace(): que devuelva el balance de la cuenta.
getCBU(): devuelve el CBU de la cuenta.
Las cuentas se identifican con un CBU.
"""
class BankAccount:

    def __init__(self, cbu):
        self.__balance = 0
        self.__cbu = cbu

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def withraw(self, amount):
        if amount > 0:
            self.__balance -= amount
        return self.__balance

    def getBalance(self):
        return self.__balance

    def getCBU(self):
        return self.__cbu

    def __str__(self):
        return "CBU: " + str(self.__cbu) + "\n" + "Balance: " + str(self.__balance)
