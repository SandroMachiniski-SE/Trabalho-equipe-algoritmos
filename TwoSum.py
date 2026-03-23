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