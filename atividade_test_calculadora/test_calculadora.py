import pytest
from calculadora import soma, divisao, multiplicacao, subtracao

# Testes de soma
def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, -1) == -2
    assert soma(0, 0) == 0

# Testes de divisão
def test_divisao():
    assert divisao(10, 2) == 5
    assert divisao(9, 3) == 3

def test_division_por_zero():
    with pytest.raises(ValueError, match="Não é permitido a divisão por zero!"):
        divisao(10, 0)

# Testes de multiplicação 
def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-1, 5) == -5
    assert multiplicacao(0, 10) == 0
    assert multiplicacao(-2, -3) == 6

def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(-1, -2) == 1
    assert subtracao(-1, 8) == -9
    assert subtracao(2, -4) == 6
    assert subtracao(2, 7) == -5