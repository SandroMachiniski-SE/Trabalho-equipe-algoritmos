from typing import List

def verificar_duplicados(numeros: List[int]) -> bool:
    """
    Esta função recebe uma lista de números inteiros e retorna True
    se algum número aparecer mais de uma vez
    """

    # Criamos um 'set'(conjunto). No python, conjuntos não aceitam itens repetidos
    # e são muito rápidos para busca de informações

    vistos = set()

    # Iniciamos um laço de repetição para olhar cada número da lista, um por um.
    for num in numeros:

        # Verificamos se o número atual já foi adicionado ao nosso conjunto 'vistos'.
        if num in vistos:
            # Se ele já está na lista, siginifica que encontramos uma duplicata.
            # O 'return' encerra a função de imediato enviando o valor True.
            return True
        
        # Se o número não estava na lista, nós o adicionamos agora
        # para que passmos checar se ele aprece de novo nos próximos ciclos.
        vistos.add(num)

    # Se o laço 'for' terminar de percorre toda a lista e nunca entrar no 'if'
    # siginifica que todos os números são únicos.
    return False

# Bloco principal de execução (teste do código)
if __name__ == "__main__":

    # Teste 1: Lista com número 1 repetido. Deve resultar em verdadeiro.
    resultado_teste_1 = verificar_duplicados([1, 2, 3, 1])
    print(f"Teste com repetidos: {resultado_teste_1}") # Saída esperada: True

    # Teste 2: Lista com números todos diferentes. Deve resultar em falso.
    resultado_teste_2 = verificar_duplicados([1, 2, 3, 4])
    print(f"Teste sem repetidos: {resultado_teste_2}") # Saída esperada: False

    # Verificação automática simples usando 'assert'.
    assert resultado_teste_1 is True
    assert resultado_teste_2 is False

    print("\nTodos os teste passaram com sucesso.")