import unittest
from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    Para cada dia, retorna quantos dias é preciso esperar até uma temperatura maior.
    Se não houver dia mais quente à frente, o valor é 0.

    Utiliza uma stack monotônica decrescente de índices:
    - Empilhamos índices cujas temperaturas ainda não encontraram um dia mais quente.
    - Ao encontrar uma temperatura maior, desempilhamos e calculamos a diferença de dias.

    Complexidade: O(n) de tempo, O(n) de espaço.
    """
    answer = [0] * len(temperatures)
    stack = []  # armazena índices dos dias ainda sem resposta

    for i, temp in enumerate(temperatures):
        # Enquanto a temperatura atual for maior que a do índice no topo da pilha,
        # encontramos o próximo dia mais quente para aquele índice.
        while stack and temperatures[stack[-1]] < temp:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)

    return answer


class TestDailyTemperatures(unittest.TestCase):

    def test_caso_base(self):
        """Teste 1: Exemplo clássico do enunciado."""
        self.assertEqual(
            daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0]
        )

    def test_temperaturas_crescentes(self):
        """Teste 2: Sequência sempre crescente — cada dia espera exatamente 1 dia."""
        self.assertEqual(daily_temperatures([1, 2, 3, 4, 5]), [1, 1, 1, 1, 0])

    def test_temperaturas_decrescentes(self):
        """Teste 3: Sequência sempre decrescente — nunca há dia mais quente à frente."""
        self.assertEqual(daily_temperatures([5, 4, 3, 2, 1]), [0, 0, 0, 0, 0])

    def test_temperaturas_iguais(self):
        """Teste 4: Todas as temperaturas iguais — nenhum dia é mais quente."""
        self.assertEqual(daily_temperatures([30, 30, 30, 30]), [0, 0, 0, 0])

    def test_lista_com_um_elemento(self):
        """Teste 5: Lista com um único dia — nunca há próximo dia mais quente."""
        self.assertEqual(daily_temperatures([42]), [0])

    def test_pico_no_meio(self):
        """Teste 6: Pico no meio da lista — dias após o pico nunca são superados."""
        self.assertEqual(daily_temperatures([30, 60, 50, 40]), [1, 0, 0, 0])


if __name__ == "__main__":
    unittest.main(verbosity=2)