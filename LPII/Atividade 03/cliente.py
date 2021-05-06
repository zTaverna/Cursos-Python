# Linguagem de Programação II
# AC03 ADS-EaD - Módulos e importação
# arquivo: cliente.py
# Prof. Rafael Maximo
#
# Email Impacta: lucas.tavernari@aluno.faculdadeimpacta.com.br


class Cliente:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.telefone = telefone
        self.email = email

    @property
    def nome(self):
        return self.__nome


    @property
    def telefone(self):
        return self.__telefone


    @telefone.setter
    def telefone(self, novo_telefone):
        if type(novo_telefone) is int:
            self.__telefone = novo_telefone
        else:
            raise TypeError

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novo_email):
        if type(novo_email) is str:
            if bool('@' in novo_email):
                self.__email = novo_email
            else:
                raise ValueError
        else:
            raise TypeError