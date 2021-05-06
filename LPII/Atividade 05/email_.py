class Email:
    """
    Classe para representar um Email, responsável por realizar a validação
    do email recebido. As instruções e regras de validação estão descritas
    nas docstrings de cada método a seguir.
    """

    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if self.valida_email(email):
            self._email = email
            self._usuario = email.split('@')[0]
            self._dominio = email.split('@')[1]

    @staticmethod
    def valida_email(email):
        if not isinstance(email, str):
            raise TypeError()
        if email.count('@') != 1:
            raise ValueError()
        parsed_email = email.replace('.', '').replace('@', '')
        if not parsed_email.isalnum():
            raise ValueError()
        return True

    @property
    def eh_aluno_impacta(self):
        return self._dominio == 'aluno.faculdadeimpacta.com.br'

    @property
    def eh_impacta(self):
        return 'faculdadeimpacta.com.br' in self._dominio

    def __eq__(self, other):
        if not isinstance(other, Email):
            raise TypeError('Não é possível comparar um email com '
                            'objetos de outro tipo')
        return self.email == other.email

    def to_json(self):
        """
        Retorna o endereço de email para ser a representação serializada
        de email no arquivo json.
        """
        return self._email

    def __repr__(self):
        """
        Retorna uma string representando o objeto do tipo email,
        siga o padrão usado para a representação de Telefone
        """
        return f'<Email: {self._email}>'