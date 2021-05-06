from agenda import Agenda
from test_agenda import TestEmail, TestContato, TestAgenda

te = TestEmail()
tc = TestContato()
ta = TestAgenda()

te.test_01_cria_email()
te.test_02_cria_email_erro()
te.test_03_email_aluno()
te.test_04_email_aluno_erro()
te.test_05_email_institucional()
te.test_06_email_institucional_erro()

tc.test_07_cria_contato()
tc.test_08_cria_contato_erro()
tc.test_09_adiciona_telefone()
tc.test_10_apaga_telefone()
tc.test_11_apaga_telefone_principal()
tc.test_12_adiciona_email()
tc.test_13_apaga_email()
tc.test_14_apaga_email_principal()
tc.test_15_buscar_contato()

ta.test_20_cria_agenda()
ta.test_21_adiciona_contato()
ta.test_22_busca_contatos()
ta.test_23_ligar_contato()
ta.test_24_exclui_contato()

#----------------- exemplo_de_uso.py
ag1 = Agenda('Rafael', '11999888777', 'rafael@exemplo.com')

ag1.novo_contato('Ana Maria', '999111000', 'ana@email.com')
ag1.novo_contato('João Paulo', '111222333', 'joaopl@email2.com')
ag1.novo_contato('Julia Matos', '16123123123', 'julia@impacta.com.br')
ag1.novo_contato('Pedro Matos', '1623234545', 'pedro@impacta.com.br')

lista = ag1.busca_contatos('23')
print(lista)

#----------------- exemplo_exporta_json.py
a1 = Agenda('Rafael', '11-999887766', 'rafael@email.com')
a1.novo_contato('Ana', '11-999888563', 'ana@email.com')
a1.novo_contato('Pedro', '11-955552222', 'pedro@email.com')
a1.novo_contato('Mariana', '21-145145145', 'mariana@email.com')
a1.novo_contato('Gustavo', '11-952525252', 'gustavo@email.com')

# primeiro contato
c1 = a1.contatos[0]
# atualiza telefone principal e adiciona novos telefones
c1.adiciona_telefone('11988776655')
c1.adiciona_telefone('1122332233', 'casa')
c1.adiciona_telefone('1145004588', 'trabalho')
# adiciona novos emails
c1.adiciona_email('ana.matos@empresa.com.br', 'trabalho')

# segundo contato
c2 = a1.contatos[1]
# adiciona novos telefones
c2.adiciona_telefone('11-4477-8877', 'casa')
# adiciona novos emails
c2.adiciona_email('pedro.santos@empresa.com', 'trabalho')

# terceiro contato
c3 = a1.contatos[2]
# adiciona novos telefones
c3.adiciona_telefone('19-562-562-562', 'chacara')
c3.adiciona_telefone('21-951-951-987', 'trabalho-rio')
c3.adiciona_telefone('11-987-963-963', 'trabalho-sp')
# adiciona novos emails
c3.adiciona_email('mari.neves@empresa.com', 'trabalho')
c3.adiciona_email('sakura.chan@gmail.com', 'jogos')

# quarto contato
c4 = a1.contatos[3]
# adiciona novos telefones
c4.adiciona_telefone('11-4477-8877', 'casa')
# adiciona novos emails
c4.adiciona_email('gustavo.santos@empresa.com', 'trabalho')

a1.exportar_contatos('exemplo_json_file')