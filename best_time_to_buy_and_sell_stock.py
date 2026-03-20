class Solution:
    def maxProfit(self, prices):
        """
        Função que recebe um array de preços e retorna o maior lucro possível.
        """

        # Inicializa o menor preço como infinito (para garantir que qualquer valor será menor)
        menor_preco = float('inf')

        # Inicializa o lucro máximo como 0
        lucro_max = 0

        # Percorre cada preço no array
        for preco in prices:

            # Atualiza o menor preço encontrado até agora
            if preco < menor_preco:
                menor_preco = preco

            # Calcula o lucro caso venda no dia atual
            lucro = preco - menor_preco

            # Atualiza o lucro máximo se o atual for maior
            if lucro > lucro_max:
                lucro_max = lucro

        # Retorna o maior lucro encontrado
        return lucro_max


# =========================
# 🔽 Testes (obrigatório)
# =========================
if __name__ == "__main__":
    s = Solution()

    print("Teste 1:", s.maxProfit([7, 1, 5, 3, 6, 4]))  # Esperado: 5
    print("Teste 2:", s.maxProfit([7, 6, 4, 3, 1]))    # Esperado: 0

    # Testes adicionais (exigência do professor)
    print("Teste 3:", s.maxProfit([1, 2, 3, 4, 5]))    # Esperado: 4
    print("Teste 4:", s.maxProfit([5, 4, 3, 2, 1]))    # Esperado: 0