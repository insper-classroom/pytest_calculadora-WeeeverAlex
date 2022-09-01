import pytest
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores
import numpy as np

#SOMA
@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1, v2)

@pytest.mark.op_complexas
def test_soma_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    assert -12 == soma(v1, v2)

#SUBTRAÇÃO
@pytest.mark.op_simples
def test_sub_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert -2 == sub(v1, v2)

@pytest.mark.op_complexas
def test_sub_dois_valores_negativos():
    v1 = -5.0
    v2 = -8.0
    assert 3 == sub(v1, v2)

#MULTIPLICAÇÃO
@pytest.mark.op_simples
def test_multiplicacao_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 35 == multiplicacao(v1, v2)

@pytest.mark.op_complexas
def test_multiplicacao_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    assert 35 == multiplicacao(v1, v2)    

#DIVISÃO
@pytest.mark.op_simples
@pytest.mark.exercicio_1
def test_divisao_dois_valores_positivos():
    v1 = 8.0
    v2 = 2.0
    assert 4.0 == divisao(v1, v2)

@pytest.mark.op_complexas
@pytest.mark.exercicio_1
def test_divisao_dois_valores_negativos():
    v1 = -8.0
    v2 = -2.0
    assert 4.0 == divisao(v1, v2)   

@pytest.mark.op_complexas
@pytest.mark.exercicio_1
def test_divisao_por_zero():
    v1 = 8.0
    v2 = 0.0
    assert np.inf == divisao(v1, v2)     

#MEDIA_LISTA_VALORES
@pytest.mark.op_simples
@pytest.mark.exercicio_1
def test_media_lista_valores_positivos():
    valores = [1, 2, 3, 4, 5]
    assert 3 == media_lista_valores(valores)

@pytest.mark.op_complexas
@pytest.mark.exercicio_1
def test_media_lista_valores_negativos():
    valores = [-1, -2, -3, -4, -5]
    assert -3 == media_lista_valores(valores)

@pytest.mark.op_complexas
@pytest.mark.exercicio_1
def test_media_lista_valores_nulos():
    valores = [1, 2, 3, 4, 5,'abc']
    numeros = [i for i in valores if isinstance(i, (int, float))]
    assert 3 == media_lista_valores(numeros)

@pytest.mark.op_complexas
@pytest.mark.exercicio_1
def test_media_lista_vazia():
    assert 0 == media_lista_valores([])


