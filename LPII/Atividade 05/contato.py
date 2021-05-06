from telefone import Telefone
from email_ import Email


class DeleteError(Exception):
    """
    Erro criado para indicar que não foi possível deletar o valor
    ou item pedido. Não é preciso implementar nada nesta classe
    - Não deve ser modificada -
    """
    pass


class CreateContactError(Exception):
    """
    Erro criado para indicar que não foi possível criar o contato.
    Não é preciso implementar nada nesta classe
    - Não deve ser modificada -
    """
    pass


class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self._telefones = {}
        self._emails = {}
        self.adiciona_telefone(telefone)
        self.adiciona_email(email)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError
        if nome == '':
            raise CreateContactError()
        self._nome = nome

    def adiciona_telefone(self, telefone, tipo='principal'):
        self._telefones[tipo] = Telefone(telefone)

    def adiciona_email(self, email, tipo='principal'):
        self._emails[tipo] = Email(email)

    def apaga_telefone(self, tipo):
        if tipo == 'principal':
            raise DeleteError()
        if tipo in self._telefones.keys():
            del self._telefones[tipo]

    def apaga_email(self, tipo):
        if tipo == 'principal':
            raise DeleteError()
        if tipo in self._emails.keys():
            del self._emails[tipo]

    @property
    def telefones(self):
        return self._telefones

    @property
    def emails(self):
        return self._emails

    def lista_telefones(self):
        lista = []
        for chave, valor in self._telefones.items():
            telefone = (chave, valor)
            lista.append(telefone)
        return lista

    def lista_emails(self):
        lista = []
        for chave, valor in self._emails.items():
            email = (chave, valor)
            lista.append(email)
        return lista

    def buscar(self, valor_busca):
        for telefone in self._telefones.values():
            if valor_busca in telefone.telefone:
                return True
        for email in self._emails.values():
            if valor_busca in email.email:
                return True
        if valor_busca in self._nome:
            return True
        return False

    def create_dump(self):
        return {
            'nome': self._nome,
            'telefones': self._telefones,
            'emails': self._emails
        }

    def __repr__(self):
        return f'<Contato: {self._nome}>'