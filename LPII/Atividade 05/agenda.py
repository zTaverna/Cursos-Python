import json

from contato import Contato


def dumper(obj):
    """
    Função auxiliar para ser usada no momento de serializar
    os objetos para json.
    - Não deve ser modificada -
    """
    try:
        return obj.to_json()
    except AttributeError:
        return obj.__dict__


class Agenda:
    def __init__(self, titular, meu_numero, meu_email):
        self.meu_contato = Contato(titular, meu_numero, meu_email)
        self.contatos = []

    def novo_contato(self, nome, telefone, email):
        novo_contato = Contato(nome, telefone, email)
        self.contatos.append(novo_contato)

    def busca_contatos(self, valor_busca):
        lista = []
        for contato in self.contatos:
            if contato.buscar(valor_busca):
                lista.append(contato)
        return lista

    def ligar(self, valor_busca, tipo='principal'):
        lista = self.busca_contatos(valor_busca)
        res = None
        for contato in lista:
            if tipo in contato.telefones:
                res = contato
                break
        if res == None:
            return 'Nenhum contato possui o tipo de telefone dado!'
        else:
            return f'Ligando para {res.nome}: {res.telefones[tipo]}'

    def apagar_contato(self, email_busca):
        for i, o in enumerate(self.contatos):
            for email in o.emails.values():
                if email_busca == email.email:
                    del self.contatos[i]
                    return f'{o} excluído com sucesso!'
        return 'Nenhum contato corresponde ao email dado.'

    def exportar_contatos(self, nome_arquivo):
        if (nome_arquivo[-4:] != '.json'):
            nome_arquivo += '.json'

        contatos_exportados = []

        for contato in self.contatos:
            contatos_exportados.append(contato.create_dump())

        arquivo = open(nome_arquivo, 'w')
        arquivo.write(
            json.dumps(
                contatos_exportados, default=dumper, indent=4, ensure_ascii=True))

    def carregar_contatos(self, nome_arquivo):
        json_file = json.load(open(nome_arquivo))
        for item in json_file:
            contato = Contato(item['nome'], item['telefones']['principal'],
                              item['emails']['principal'])
            for tipo in item['telefones']:
                if tipo != 'principal':
                    contato.adiciona_telefone(item['telefones'][tipo], tipo)
            for tipo in item['emails']:
                if tipo != 'principal':
                    contato.adiciona_email(item['emails'][tipo], tipo)
            self.contatos.append(contato)