"""
Pytest
  Para instalar: pip install pytest

  O pytest identifica quais são os casos de teste automaticamente desde
  que o nome dos métodos de teste estejam no seguinte formato:
  test_*.py ou *_test.py

  Documentação:
  https://docs.pytest.org/en/stable/

  Ex.1: Executando um test no terminal
  pytest test_simulacao_pytest

  Ex.2: Aumentando a verbosidade de informações
  pytest -v test_simulacao_pytest

  Ex.3: Especifcando a funcao
  pytest -v test_simulacao_pytest::test_simulacao_1

  Ex.4: Criando um decorator/marcador pora marcar os testes (posso usar mais de um marcador)
    @pytest.mark.[name_test]
    pytest -m simulacao: roda todos os tests na pasta
    pytest test_simulacao_pytest -m -v simulacao: especifica os teste

  OBS.: Podemos usar os marquers a nivel de classe e a nivel de métodos

  Ex.5: Posso especificar um ou mais marcadores/decorators nos métodos
  class TesteSimulacao:

    @pytest.mark.simulacao
    def test_simulacao_1(self):
        assert 1 == 1

    @pytest.mark.simulacao
    @pytest.mark.skip
    def test_simulacao_2(self):
        assert 2 == 2

    !IMPORTANT: Evitar colocar mais de um método nas classes

  Ex.6: @pytest.mark.skip, esse decorator faz o pyteste pular o test

  DEBUGANDO TESTES

    --pdb:
        pytest -m carrinho --pdb

        Olhar a saida do erro no terminal

        u: Sobe no erro linha por linha
        d: Desçe no erro linha por linha
        c: Continua o teste e encerra o debug

        obs.: só para quando tem erro

    --trace
      pytest -m carrinho --trace

      n: avança para a proxima linha com exeção de funções e métodos
      s: debuga o método (entra no método) inteiro
      c: Continua o teste e encerra o debug

      obs: debuga o teste linha a linha desde o começo

    breakpoint() -> meio do código
"""