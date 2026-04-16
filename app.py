from produtos import produtos
from utils import calcular_comissao, filtrar_por_categoria

def listar_produtos(produtos):
    print("Produtos disponíveis no nicho de eletrônicos:")
    for i, produto in enumerate(produtos, 1):
        comissao = calcular_comissao(produto["preco"])
        print(f"{i}. {produto['nome']} ({produto['categoria']}) - R$ {produto['preco']:.2f} | Comissão: R$ {comissao:.2f}")

def main():
    print("Bem-vindo ao Mini Shopee Afiliado!")
    categoria = input("Digite a categoria para filtrar produtos ou ENTER para ver todos: ").strip()
    if categoria:
        filtrados = filtrar_por_categoria(produtos, categoria)
        if filtrados:
            listar_produtos(filtrados)
        else:
            print("Nenhum produto encontrado nessa categoria.")
    else:
        listar_produtos(produtos)

if __name__ == "__main__":
    main()
