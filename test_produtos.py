from produtos import produtos


def test_lista_nao_vazia():
    assert len(produtos) > 0


def test_existe_categoria_perifericos():
    categorias = [p["categoria"] for p in produtos]
    assert "Periféricos" in categorias


def test_todos_produtos_tem_nome():
    for produto in produtos:
        assert "nome" in produto


def test_todos_produtos_tem_preco():
    for produto in produtos:
        assert "preco" in produto


def test_precos_maiores_que_zero():
    for produto in produtos:
        assert produto["preco"] > 0
