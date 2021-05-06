# Linguagem de Programação II
# AC02 ADS-EaD - Classes e Herança
# Prof. Rafael Maximo
#
# Email Impacta: lucas.tavernari@aluno.faculdadeimpacta.com.br

# ------------------ #
# Criando uma classe #
# ------------------ #

# Crie a classe Mamifero seguindo o exemplo da classe Reptil
# Para esta AC não utilizem o @property ainda


class Reptil:
    """
    Classe mãe - não deve ser editada

    Observem que criei os atributos (características) no inicializador
    da classe, o __init__, recebendo os valores como parâmetros e
    que NÃO utilizei o @property ainda.
    """
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return '{} ainda não atingiu maturidade sexual'.format(self.nome)


class Mamifero:
    """
    Complete a classe seguindo o exemplo da classe Reptil,
    adaptando as características de acordo com a imagem fornecida
    junto ao enunciado no Classroom.

    Atenção aos nomes dos atributos e métodos, pois eles devem estar
    escritos exatamente como os da imagem, com letra minúscula,
    separados por um sublinhado _ e sem cedilha nem acentos.

    Qualquer erro de digitação implicará em uma falha nos testes
    e portanto perda de pontuação.
    """
    def __init__(self, nome: str, cor_pelo: str, idade: int, tipo_pata: str):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata

    def correr(self):
        """Retorna a frase: '<nome> correndo'

        Onde <nome> é o nome dado à istância do animal em questão.
        """
        return f'{self.nome} correndo'

    def mamar(self):
        """
        Se o animal tiver 1 ano ou menos, retorna:
        '<nome> mamando'
        Caso contrário, retorna:
        '<nome> já desmamou'
        """
        if self.idade <= 1:
            return f'{self.nome} mamando'
        else:
            return f'{self.nome} já desmamou'


# ------------------------- #
# Criando as classes filhas #
# ------------------------- #

# Crie as classes filhas Cavalo, Cachoro, Gato, Cobra e Jacaré
# seguindo o exemplo da classe Camaleao abaixo
# Para esta AC não utilizem o @property ainda

class Camaleao(Reptil):
    """
    Exemplo de solução do exercício:

    Além dos atributos da classe mãe, possui o atributo:
    inseto_favorito, do tipo string.

    Implementa os métodos específicos:
    mudar_de_cor() e comer_inseto()

    Notem que não é preciso implementar o método tomar_sol()
    nem o método botar_ovo(), pois eles são herdados automaticamente
    da classe mãe, que é definida ali em cima,
    na declaração da classe filha.
    """
    def __init__(self, nome, cor, idade, inseto_favorito):
        """
        O super é uma forma de acessar o método inicializador
        da classe mãe e delegar a ele o trabalho de atribuir os
        valores para os atributos comuns a todas as classes filhas
        (atributos provenientes da classe mãe).
        seria equivalente a copiar o código aqui e redefinir manualmente
        todos os atributos:
            self.nome = nome
            self.cor = cor
            self.idade = idade
        Ou seja, podemos utilizar o super para reaproveitar o código
        da classe mãe sem precisar digitá-lo ou copiá-lo
        """
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)


"""
Implementem aqui as cinco classes filhas de Mamifero ou Reptil,
de acordo com o caso, conforme dado no diagrama apresentado no padrão UML.

Os atributos específicos de cada classe filha DEVEM OBRIGATORIAMENTE ser
recebidos como parâmetros no momento da criação, a única exceção é o
número de vidas do gato, que SEMPRE é inicializado em 7.

Os métodos de cada classe filha devem sempre RETORNAR uma string
no seguinte formato '<nome do animal> <método em questão no gerúndio>'
Sem nenhuma pontuação, conforme os exemplos a seguir.

Exemplo:
método trocar_pele() retorna: '<nome> trocando de pele'
método dormir() retorna: '<nome> dormindo'
método miar() retorna: '<nome> miando'
Onde <nome> é o nome dado para cada animal (o valor atributo `nome` de
cada instância, não o nome da classe)
"""

class Cavalo(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    cor_crina, do tipo string.

    Implementa os métodos específicos:
    galopar() e relinchar()
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina: str):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.cor_crina = cor_crina

    def galopar(self):
        return f'{self.nome} galopando'

    def relinchar(self):
        return f'{self.nome} relinchando'


class Cachorro(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    raca, do tipo string. (raça, porém sem o ç)

    Implementa os métodos específicos:
    latir() e rosnar()
    """
    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca: str):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.raca = raca

    def latir(self):
        return f'{self.nome} latindo'

    def rosnar(self):
        return f'{self.nome} rosnando'


class Gato(Mamifero):
    """
    Além dos atributos da classe mãe, possui o atributo:
    vidas, do tipo inteiro. (não deve ser recebido como parâmetro,
    começa sempre em 7 quando um novo gato é instanciado)

    Implementa os métodos específicos:
    miar() e morrer()

    No início do método morrer, você deve verificar quantas vidas o gato
    ainda tem sobrando, se for igual a zero, retornar:
    '<nome> morreu'

    se ainda houver vidas sobrando, subtrair 1 de vida e retornar:
    '<nome> tem <vidas> vidas sobrando'

    Onde <vidas> é o número de vidas restantes do gato, ou seja, quantas
    vidas "extras" ele ainda tem, além da atual.
    """
    def __init__(self, nome: str, cor_pelo, idade: int, tipo_pata):
        self.vidas = 7

    def miar(self):
        return f'{self.nome} miando'

    def morrer(self):
        self.vidas -= 1

        if self.vidas <= 0:
            return f'{self.nome} morreu'
        else:
            return f'{self.nome} tem {self.vidas} vidas sobrando'


class Cobra(Reptil):
    """
    Além dos atributos da classe mãe, possui o atributo:
    veneno, do tipo booleano.

    Implementa os métodos específicos:
    rastejar() e trocar_pele()
    """
    def __init__(self, nome, cor, idade, veneno: bool):
        super().__init__(nome, cor, idade)
        self.veneno = veneno

    def rastejar(self):
        return f'{self.nome} rastejando'

    def trocar_pele(self):
        return f'{self.nome} trocando de pele'


class Jacare(Reptil):
    """
    Além dos atributos da classe mãe, possui o atributo:
    num_dentes, do tipo inteiro.

    Implementa os métodos específicos:
    atacar() e dormir()
    """
    def __init__(self, nome, cor, idade, num_dentes: int):
        super().__init__(nome, cor, idade)
        self.num_dentes = num_dentes

    def atacar(self):
        return f'{self.nome} atacando'

    def dormir(self):
        return f'{self.nome} dormindo'