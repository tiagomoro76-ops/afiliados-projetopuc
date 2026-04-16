def calcular_comissao(preco, taxa=0.1):
    """Calcula a comissão do afiliado"""
    return preco * taxa

def filtrar_por_categoria(produtos, categoria):
    """Filtra produtos por categoria"""
    return [p for p in produtos if p["categoria"].lower() == categoria.lower()]
