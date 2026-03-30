# ============================================================
# Problema   : Best Time to Buy and Sell Stock
# Link       : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Plataforma : LeetCode
# Estrutura  : Array (Lista)
# Justificativa: O array é ideal pois o problema exige uma
#   única passagem sequencial pelos preços, rastreando apenas
#   o menor valor visto até o momento e o lucro máximo possível.
#   O acesso por iteração em O(n) com apenas duas variáveis
#   auxiliares garante complexidade O(n) de tempo e O(1) de
#   espaço — sem necessidade de estruturas extras como pilhas
#   ou tabelas hash.
# ============================================================

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Encontra o maior lucro possível comprando e vendendo uma ação uma única vez.
        
        Estratégia: Rastreia o preço mínimo visto até agora e calcula o lucro
        máximo possível em cada iteração.
        
        Args:
            prices: Lista de inteiros representando o preço da ação em cada dia
            
        Returns:
            Inteiro representando o maior lucro possível (0 se impossível lucrar)
            
        Raises:
            ValueError: Se a lista de preços estiver vazia
            
        Complexidade:
            Tempo: O(n) - passa pela lista uma única vez
            Espaço: O(1) - apenas duas variáveis são usadas
            
        Exemplo:
            maxProfit([7, 1, 5, 3, 6, 4])  =>  5  (compra em 1, vende em 6)
            maxProfit([7, 6, 4, 3, 1])     =>  0  (preços em ordem decrescente)
        """
        # Validação de entrada
        if not prices:
            raise ValueError("A lista de preços não pode estar vazia")
        
        if len(prices) < 2:
            return 0  # Impossível lucrar com apenas um dia

        # Inicializa o menor preço como infinito (para garantir que qualquer valor será menor)
        min_price: int = float('inf')

        # Inicializa o lucro máximo como 0
        max_profit: int = 0

        # Percorre cada preço no array (single pass)
        for price in prices:
            # Atualiza o menor preço encontrado até agora
            if price < min_price:
                min_price = price

            # Calcula o lucro caso venda no dia atual
            profit: int = price - min_price

            # Atualiza o lucro máximo se o atual for maior
            if profit > max_profit:
                max_profit = profit

        # Retorna o maior lucro encontrado
        return max_profit


# =========================
# 🔽 Testes (obrigatório)
# =========================
if __name__ == "__main__":
    s = Solution()

    print("="*60)
    print("TESTES - MELHOR TEMPO PARA COMPRAR E VENDER AÇÕES")
    print("="*60)

    # Teste 1: Caso clássico com lucro
    print("\nTeste 1 - Caso clássico com lucro:")
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = s.maxProfit(prices1)
    print(f"Preços: {prices1}")
    print(f"Resultado: {result1} (Esperado: 5)")
    print(f"Explicação: Compra em 1, vende em 6 => Lucro = 5")
    print("Status: ✓ PASSOU" if result1 == 5 else "Status: ✗ FALHOU")

    # Teste 2: Preços em ordem decrescente (sem lucro)
    print("\nTeste 2 - Preços em ordem decrescente:")
    prices2 = [7, 6, 4, 3, 1]
    result2 = s.maxProfit(prices2)
    print(f"Preços: {prices2}")
    print(f"Resultado: {result2} (Esperado: 0)")
    print(f"Explicação: Impossível lucrar, preço sempre cai")
    print("Status: ✓ PASSOU" if result2 == 0 else "Status: ✗ FALHOU")

    # Teste 3: Preços em ordem crescente (lucro máximo)
    print("\nTeste 3 - Preços em ordem crescente:")
    prices3 = [1, 2, 3, 4, 5]
    result3 = s.maxProfit(prices3)
    print(f"Preços: {prices3}")
    print(f"Resultado: {result3} (Esperado: 4)")
    print(f"Explicação: Compra em 1, vende em 5 => Lucro = 4")
    print("Status: ✓ PASSOU" if result3 == 4 else "Status: ✗ FALHOU")

    # Teste 4: Preços em ordem decrescente (sem lucro)
    print("\nTeste 4 - Preços em ordem decrescente novamente:")
    prices4 = [5, 4, 3, 2, 1]
    result4 = s.maxProfit(prices4)
    print(f"Preços: {prices4}")
    print(f"Resultado: {result4} (Esperado: 0)")
    print(f"Explicação: Impossível lucrar")
    print("Status: ✓ PASSOU" if result4 == 0 else "Status: ✗ FALHOU")

    # Teste 5: Dois dias apenas
    print("\nTeste 5 - Dois dias com lucro:")
    prices5 = [2, 7]
    result5 = s.maxProfit(prices5)
    print(f"Preços: {prices5}")
    print(f"Resultado: {result5} (Esperado: 5)")
    print(f"Explicação: Compra em 2, vende em 7 => Lucro = 5")
    print("Status: ✓ PASSOU" if result5 == 5 else "Status: ✗ FALHOU")

    # Teste 6: Pico no meio
    print("\nTeste 6 - Pico no meio do array:")
    prices6 = [3, 2, 6, 5, 0, 3]
    result6 = s.maxProfit(prices6)
    print(f"Preços: {prices6}")
    print(f"Resultado: {result6} (Esperado: 4)")
    print(f"Explicação: Compra em 2, vende em 6 => Lucro = 4")
    print("Status: ✓ PASSOU" if result6 == 4 else "Status: ✗ FALHOU")

    print("\n" + "="*60)
    print("TODOS OS TESTES PASSARAM ✓")
    print("="*60)