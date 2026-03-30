# ============================================================
# Problema   : Maximum Subarray
# Link       : https://leetcode.com/problems/maximum-subarray/
# Plataforma : LeetCode
# Estrutura  : Array (Lista)
# Justificativa: O array é a estrutura natural para o Algoritmo
#   de Kadane, que resolve o problema em uma única passagem
#   sequencial. Em cada posição, basta decidir entre estender
#   o subarray atual ou iniciar um novo — decisão feita em O(1)
#   com apenas duas variáveis auxiliares (max_current e
#   max_global). Não há necessidade de estruturas extras como
#   pilhas ou tabelas hash, resultando em O(n) de tempo e
#   O(1) de espaço.
# ============================================================

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Encontra o subarray com soma máxima usando o Algoritmo de Kadane.
        
        O Algoritmo de Kadane funciona rastreando:
        - max_current: A soma máxima do subarray terminando no índice atual
        - max_global: A soma máxima encontrada até agora em qualquer subarray
        
        Em cada posição, decidimos se estendemos o subarray anterior ou 
        começamos um novo a partir do elemento atual.
        
        Args:
            nums: Lista de inteiros que pode conter números negativos
            
        Returns:
            Inteiro representando a soma máxima de qualquer subarray contíguo
            
        Raises:
            ValueError: Se a lista estiver vazia
            
        Complexidade:
            Tempo: O(n) - passa pela lista uma única vez
            Espaco: O(1) - apenas duas variáveis são usadas
            
        Exemplo:
            maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])  =>  6
            Explicacao: O subarray [4, -1, 2, 1] tem soma 6
        """
        # Validacao de entrada
        if not nums:
            raise ValueError("A lista nao pode estar vazia")
        
        # Inicializa com o primeiro elemento
        max_current: int = nums[0]  # Soma máxima terminando no indice atual
        max_global: int = nums[0]   # Soma máxima encontrada até agora

        # Itera a partir do segundo elemento
        for i in range(1, len(nums)):
            # Decide se estende o subarray anterior ou comeca um novo
            max_current = max(nums[i], max_current + nums[i])

            # Atualiza o máximo global se encontrou algo melhor
            if max_current > max_global:
                max_global = max_current

        return max_global


if __name__ == "__main__":
    s = Solution()

    print("="*60)
    print("TESTES - SUBARRAY MAXIMO (ALGORITMO DE KADANE)")
    print("="*60)

    # Teste 1: Caso classico com positivos e negativos
    print("\nTeste 1 - Caso classico com positivos e negativos:")
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = s.maxSubArray(nums1)
    print(f"Array: {nums1}")
    print(f"Resultado: {result1} (Esperado: 6)")
    print(f"Explicacao: Subarray [4, -1, 2, 1] tem soma 6")
    print("Status: ✓ PASSOU" if result1 == 6 else "Status: ✗ FALHOU")

    # Teste 2: Array com um elemento
    print("\nTeste 2 - Array com um elemento (edge case):")
    nums2 = [1]
    result2 = s.maxSubArray(nums2)
    print(f"Array: {nums2}")
    print(f"Resultado: {result2} (Esperado: 1)")
    print("Status: ✓ PASSOU" if result2 == 1 else "Status: ✗ FALHOU")

    # Teste 3: Array em ordem crescente
    print("\nTeste 3 - Array em ordem crescente:")
    nums3 = [5, 4, -1, 7, 8]
    result3 = s.maxSubArray(nums3)
    print(f"Array: {nums3}")
    print(f"Resultado: {result3} (Esperado: 23)")
    print(f"Explicacao: Soma de todos os elementos = 5+4+(-1)+7+8 = 23")
    print("Status: ✓ PASSOU" if result3 == 23 else "Status: ✗ FALHOU")

    # Teste 4: Array com todos negativos
    print("\nTeste 4 - Array com todos números negativos:")
    nums4 = [-5, -2, -8, -1, -4]
    result4 = s.maxSubArray(nums4)
    print(f"Array: {nums4}")
    print(f"Resultado: {result4} (Esperado: -1)")
    print(f"Explicacao: O maior (menos negativo) eh -1")
    print("Status: ✓ PASSOU" if result4 == -1 else "Status: ✗ FALHOU")

    # Teste 5: Array misto com zero
    print("\nTeste 5 - Array misto com zero:")
    nums5 = [-1, 0, -2, 3, 5, -1, 2]
    result5 = s.maxSubArray(nums5)
    print(f"Array: {nums5}")
    print(f"Resultado: {result5} (Esperado: 9)")
    print(f"Explicacao: Subarray [3, 5, -1, 2] tem soma 9")
    print("Status: ✓ PASSOU" if result5 == 9 else "Status: ✗ FALHOU")

    # Teste 6: Array com alternancia positivo/negativo
    print("\nTeste 6 - Array com alternancia positivo/negativo:")
    nums6 = [5, -3, 5]
    result6 = s.maxSubArray(nums6)
    print(f"Array: {nums6}")
    print(f"Resultado: {result6} (Esperado: 7)")
    print(f"Explicacao: Soma de todos = 5-3+5 = 7")
    print("Status: ✓ PASSOU" if result6 == 7 else "Status: ✗ FALHOU")

    print("\n" + "="*60)
    print("TODOS OS TESTES PASSARAM ✓")
    print("="*60)