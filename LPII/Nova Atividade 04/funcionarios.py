# Linguagem de Programação II
# Atividade Contínua 04 - Classes abstratas, herança e polimorfismo
# Arquivo: funcionarios.py
# Prof. Rafael Maximo
#
# e-mail: lucas.tavernari@aluno.faculdadeimpacta.com.br


class Pessoa:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade


class Funcionario(Pessoa):
    
    def __init__(self, nome, idade, email, carga_horaria):
        super().__init__(nome, idade)
        self.__email = email
        self.__carga_horaria = carga_horaria

    def calcula_salario(self):
        raise NotImplementedError

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        raise NotImplementedError
       
    def aumenta_salario(self):
        raise NotImplementedError

    @property
    def email(self):
        return self.__email

class Programador(Funcionario):

    def __init__(self, nome, idade, email, carga_horaria):
        self.__salario_base = 35
        self.__minimo_carga_horaria = 20
        self.__maximo_carga_horaria = 40
        self.__salario_mes = 0
        super().__init__(self, nome, idade, email, carga_horaria)

    def calcula_salario(self):
        salario_semana = self.__salario_base * self.__carga_horaria
        self.__salario_mes = salario_semana * 4.5
        return self.__salario_mes

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if self.__maximo_carga_horaria >= nova_carga_horaria >= self.__minimo_carga_horaria:
            self.__carga_horaria = nova_carga_horaria
        else:
            raise ValueError
        
    def aumenta_salario(self):
        aumento = self.__salario_base * 1.05
        self.__salario_base = aumento

class Estagiario(Funcionario):

    def __init__(self, nome, idade, email, carga_horaria_semanal):
        self.__salario_base = 15.50
        self.__minimo_carga_horaria = 16
        self.__maximo_carga_horaria = 30
        self.__salario_mes = 0
        super().__init__(self, nome, idade, email, carga_horaria)

    def calcula_salario(self):
        ax_alimento = 250
        salario_semana = self.__salario_base * self.__carga_horaria
        self.__salario_mes = salario_semana * 4.5
        return self.__salario_mes + ax_alimento

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if self.__maximo_carga_horaria >= nova_carga_horaria >= self.__minimo_carga_horaria:
            self.__carga_horaria = nova_carga_horaria
        else:
            raise ValueError
        
    def aumenta_salario(self):
        aumento = self.__salario_base * 1.05
        self.__salario_base = aumento

class Vendedor(Funcionario):

    def __init__(self, nome, idade, email, carga_horaria_semanal):
        self.__salario_base = 30
        self.__minimo_carga_horaria = 15
        self.__maximo_carga_horaria = 45
        self.__salario_mes = 0
        self.__visitas = 0
        super().__init__(self, nome, idade, email, carga_horaria)

    def calcula_salario(self):
        ax_alimento = 350
        ax_transporte = self.__visitas * 30
        salario_semana = self.__salario_base * self.__carga_horaria
        self.__salario_mes = salario_semana * 4.5
        return self.__salario_mes + ax_alimento + ax_transporte

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if self.__maximo_carga_horaria >= nova_carga_horaria >= self.__minimo_carga_horaria:
            self.__carga_horaria = nova_carga_horaria
        else:
            raise ValueError
        
    def aumenta_salario(self):
        aumento = self.__salario_base * 1.05
        self.__salario_base = aumento

    @property
    def visitas(self):
        return self.__visitas

    def realizar_visita(self, n_visitas):
        if type(n_visitas) == int:
            if n_visitas > 0:
                self.__visitas += n_visitas
            else:
                raise ValueError
        else:
            raise TypeError

    def zerar_visitas(self):
        self.__visitas = 0