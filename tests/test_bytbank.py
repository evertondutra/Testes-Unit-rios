from faker import Faker
from codigo.bytebank import Funcionario


class TestClass:


    def test_quando_idade_recebe_13_03_2000_deve_retornar_(self):
        entrada = '13/03/2000'
        esperado = 22
        # Given
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        # When
        resultado = funcionario_teste.idade()
        # Then
        assert resultado == esperado

    def test_quando_insere_nome_completo_retorna_ultimo_sobrenome(self):
        fake = Faker()
        nome = fake.name()
        nome_quebrado = nome.split(' ')
        esperado = nome_quebrado[-1]

        funcionario = Funcionario(nome, '13/01/2000', 1111)

        resultado = funcionario.sobrenome()

        assert resultado == esperado

