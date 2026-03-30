# ============================================================
# Problema   : Middle of the Linked List
# Link       : https://leetcode.com/problems/middle-of-the-linked-list/
# Plataforma : LeetCode
# Estrutura  : Linked List (Lista Encadeada)
# Justificativa: A lista encadeada não oferece acesso direto
#   por índice, o que torna impossível calcular o meio com uma
#   simples divisão. A solução elegante é o algoritmo dos dois
#   ponteiros (slow/fast): o ponteiro 'fast' avança 2 nós por
#   vez enquanto o 'slow' avança 1, de modo que quando 'fast'
#   chega ao fim, 'slow' está exatamente no meio — tudo em
#   O(n) de tempo e O(1) de espaço, sem percorrer a lista duas
#   vezes nem usar estruturas auxiliares.
# ============================================================

from __future__ import annotations
import unittest
from typing import Optional, Iterable


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def build_list(values: Iterable[int]) -> Optional[ListNode]:
    """Constrói uma linked list a partir de um iterável de inteiros."""
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list[int]:
    """Converte uma linked list em uma lista Python para facilitar comparações."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Retorna o nó do meio da linked list usando o algoritmo dos dois ponteiros.
    O ponteiro 'fast' avança duas posições por ciclo enquanto o 'slow' avança uma,
    então quando 'fast' chega ao fim, 'slow' está exatamente no meio.
    Em listas de tamanho par, retorna o segundo nó do meio.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


class TestMiddleNode(unittest.TestCase):

    def test_lista_impar(self):
        """Teste 1: Lista com 5 elementos — meio é o elemento de índice 2 (valor 3)."""
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(middle_node(head)), [3, 4, 5])

    def test_lista_par(self):
        """Teste 2: Lista com 6 elementos — retorna o segundo nó do meio (valor 4)."""
        head = build_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(to_list(middle_node(head)), [4, 5, 6])

    def test_lista_com_um_elemento(self):
        """Teste 3: Lista com um único elemento — o meio é ele mesmo."""
        head = build_list([42])
        self.assertEqual(to_list(middle_node(head)), [42])

    def test_lista_com_dois_elementos(self):
        """Teste 4: Lista com dois elementos — retorna o segundo (segundo nó do meio)."""
        head = build_list([1, 2])
        self.assertEqual(to_list(middle_node(head)), [2])

    def test_lista_vazia(self):
        """Teste 5: Lista vazia — deve retornar None."""
        self.assertIsNone(middle_node(None))

    def test_lista_com_tres_elementos(self):
        """Teste 6: Lista com 3 elementos — meio é o elemento central (valor 2)."""
        head = build_list([1, 2, 3])
        self.assertEqual(to_list(middle_node(head)), [2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)