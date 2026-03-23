from typing import List

def produto_exceto_proprio(numeros: List[int]) -> List[int]:
    """
    Calcula o produto de todos os elementos, exceto o atual, sem usar divisão.
    Utiliza a técnica de acúmulo por prefixos e sufixos.
    """
    n = len(numeros)
    # Criamos a lista de resposta preenchida com 1s (elemento neutro da multiplicação)
    resposta = [1] * n

    # Passo 1: Calcular os produtos à ESQUERDA (prefixo)
    # Cada posição acumula o produto de tudo o que veio antes dela.
    prefixo = 1
    for i in range(n):
        resposta[i] = prefixo
        prefixo *= numeros[i]

    # Passo 2: Calcular os produtos à DIREITA (sufixo)
    # Multiplicamos o que já temos na resposta pelo produto de tudo o que vem depois.
    sufixo = 1
    for i in range(n - 1, -1, -1):  # Percorre a lista de trás para frente
        resposta[i] *= sufixo
        sufixo *= numeros[i]

    return resposta

if __name__ == "__main__":
    # Teste: [1, 2, 3, 4] deve retornar [24, 12, 8, 6]
    # Explicação do primeiro item (24): é o produto de 2 * 3 * 4
    entrada = [1, 2, 3, 4]
    resultado = produto_exceto_proprio(entrada)
    
    print(f"Entrada: {entrada}")
    print(f"Resultado: {resultado}")

    # Verificação automática
    assert resultado == [24, 12, 8, 6]
    print("\n--- Teste do algoritmo de produto passou! ---")