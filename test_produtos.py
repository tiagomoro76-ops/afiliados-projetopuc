import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from produtos import produtos
from utils import calcular_comissao, filtrar_por_categoria

def test_calcular_comissao():
    assert calcular_comissao(100) == 10

def test_filtrar_por_categoria():
    filtrados = filtrar_por_categoria(produtos, "Periféricos")
    assert len(filtrados) == 2
