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
