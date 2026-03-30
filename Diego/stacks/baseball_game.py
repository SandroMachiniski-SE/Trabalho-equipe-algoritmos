# ============================================================
# Problema   : Baseball Game
# Link       : https://leetcode.com/problems/baseball-game/
# Plataforma : LeetCode
# Estrutura  : Stack (Pilha)
# Justificativa: O problema exige acesso constante às últimas
#   pontuações válidas para aplicar as operações '+' e 'D', e
#   remoção imediata da mais recente com 'C'. A pilha (LIFO)
#   é a estrutura ideal para isso: push e pop em O(1) refletem
#   naturalmente o histórico mutável de pontuações, sem
#   necessidade de reindexar ou percorrer a estrutura.
# ============================================================

import unittest
from typing import List


def cal_points(operations: List[str]) -> int:
    """
    Simula um jogo de baseball processando uma lista de operações e retorna
    a soma total dos pontos válidos ao final.

    Operações válidas:
      - Número inteiro (como string): adiciona esse valor como nova pontuação.
      - "+": nova pontuação é a soma das duas últimas pontuações válidas.
      - "D": nova pontuação é o dobro da última pontuação válida.
      - "C": invalida (remove) a última pontuação válida.
    """
    stack = []

    for op in operations:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))

    return sum(stack)


class TestCalPoints(unittest.TestCase):

    def test_caso_base(self):
        """Teste 1: Exemplo clássico do enunciado — resultado esperado é 30."""
        self.assertEqual(cal_points(["5", "2", "C", "D", "+"]), 30)

    def test_apenas_numeros(self):
        """Teste 2: Sem operações especiais — soma direta dos valores."""
        self.assertEqual(cal_points(["1", "2", "3", "4"]), 10)

    def test_operacao_D(self):
        """Teste 3: Operação 'D' deve dobrar a última pontuação válida."""
        self.assertEqual(cal_points(["5", "D"]), 15)  # 5 + 10

    def test_operacao_C(self):
        """Teste 4: Operação 'C' deve remover a última pontuação da pilha."""
        self.assertEqual(cal_points(["5", "3", "C"]), 5)  # 3 é removido

    def test_operacao_mais(self):
        """Teste 5: Operação '+' soma as duas últimas pontuações válidas."""
        self.assertEqual(cal_points(["3", "4", "+"]), 14)  # 3 + 4 + 7

    def test_sequencia_complexa(self):
        """Teste 6: Sequência mista com números negativos e múltiplas operações."""
        self.assertEqual(cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]), 27)


if __name__ == "__main__":
    unittest.main(verbosity=2)