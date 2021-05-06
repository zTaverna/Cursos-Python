# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: banco.py
# Prof. Rafael Maximo
#
# Email Impacta: lucas.tavernari@aluno.faculdadeimpacta.com.br

# A classe Banco ira precisar da classe Conta, que deve ser importada aqui:
# sigam o exemplo dado na live 03, anexei os arquivos na postagem do Classroom.

from conta import Conta


class Banco:

    def __init__(self, nome):
        self.__contas = []
        self.__nome = nome

    @property
    def contas (self):
        return self.__contas

    @property
    def nome(self):
        return self.__nome

    def abre_conta(self, clientes, saldo):
        if saldo < 0:
            raise ValueError
        else:
            numero = len(self.__contas) + 1
            c1 = Conta(clientes, numero, saldo)
            self.__contas.append(c1)
