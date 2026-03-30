# ============================================================
# Problema   : Two Sum
# Link       : https://leetcode.com/problems/two-sum/
# Plataforma : LeetCode
# Estrutura  : Hash Map (Dicionário)
# Justificativa: O uso de um hash map (dicionário) permite
#   armazenar os valores já percorridos junto com seus índices,
#   possibilitando verificar em tempo O(1) se o complemento
#   necessário (target - num) já foi visto anteriormente.
#   Dessa forma, o problema é resolvido em apenas uma passagem
#   pela lista (O(n)), evitando a abordagem ingênua de dois loops
#   aninhados, que teria complexidade O(n²). O dicionário é ideal
#   para esse tipo de busca rápida por chave.
# ============================================================

class Solution:
    def twoSum(self, nums, target):
        mapa = {}  # valor -> índice
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in mapa:
                return [mapa[complemento], i]
            mapa[num] = i
        print("Target:", target)
        print("Nums:", nums)
        return None  # ou []


# Exemplo de uso
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))   # saída esperada: [0, 1]
    print(s.twoSum([1, 2, 3], 10))       # saída esperada: None (e imprime Target e Nums)