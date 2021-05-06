# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: conta.py
# Prof. Rafael Maximo
#
# Email Impacta: lucas.tavernari@aluno.faculdadeimpacta.com.br


class Conta:

    def __init__(self, clientes, numero, saldo):
        self.__clientes = clientes
        self.__numero = numero
        self.__saldo = saldo
        self.__extrato = [("saldo inicial", saldo)]

    @property
    def clientes(self):
        return self.__clientes

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    def sacar(self, valor):
        if valor > self.__saldo:
            raise ValueError
        else:
            self.__saldo -= valor
            self.__extrato.append(("saque", valor))

    def depositar(self, valor):
        self.__saldo += valor
        self.__extrato.append(("deposito", valor))

    def tirar_extrato(self):
        return self.__extrato
