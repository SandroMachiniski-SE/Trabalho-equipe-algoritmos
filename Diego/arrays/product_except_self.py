# ============================================================
# Problema   : Product of Array Except Self
# Link       : https://leetcode.com/problems/product-of-array-except-self/
# Plataforma : LeetCode
# Estrutura  : Array (Lista)
# Justificativa: O problema exige calcular produtos acumulados
#   sem usar divisão. O array é a estrutura ideal pois permite
#   acesso direto por índice em O(1), viabilizando as duas
#   passagens (prefixo da esquerda e sufixo da direita) que
#   constroem a resposta final em O(n) com O(1) de espaço extra,
#   sem necessidade de estruturas auxiliares adicionais.
# ============================================================

import unittest
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


class TestProdutoExcetoProprio(unittest.TestCase):

    def test_caso_basico(self):
        """Teste 1: Caso clássico do enunciado — [1,2,3,4] → [24,12,8,6]."""
        self.assertEqual(produto_exceto_proprio([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_lista_com_zero(self):
        """Teste 2: Presença de zero — apenas a posição do zero terá produto != 0."""
        self.assertEqual(produto_exceto_proprio([0, 1, 2, 3]), [6, 0, 0, 0])

    def test_lista_com_dois_zeros(self):
        """Teste 3: Dois zeros — todos os produtos resultam em zero."""
        self.assertEqual(produto_exceto_proprio([0, 0, 2, 3]), [0, 0, 0, 0])

    def test_lista_com_negativos(self):
        """Teste 4: Números negativos — sinal deve ser tratado corretamente."""
        self.assertEqual(produto_exceto_proprio([-1, 2, -3, 4]), [-24, 12, -8, 6])

    def test_lista_com_dois_elementos(self):
        """Teste 5: Lista mínima com dois elementos — cada um recebe o valor do outro."""
        self.assertEqual(produto_exceto_proprio([3, 7]), [7, 3])

    def test_lista_com_um_elemento(self):
        """Teste 6: Lista com um único elemento — produto dos demais é 1 (neutro)."""
        self.assertEqual(produto_exceto_proprio([99]), [1])


if __name__ == "__main__":
    unittest.main(verbosity=2)