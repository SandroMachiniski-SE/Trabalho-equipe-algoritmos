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


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove o n-ésimo nó a partir do fim da lista em uma única passagem.
    Usa um nó 'dummy' antes da cabeça para simplificar a remoção do primeiro nó,
    e dois ponteiros com distância n+1 entre si para localizar o alvo.
    """
    dummy = ListNode(0, head)
    fast = slow = dummy

    # Avança 'fast' n+1 passos para abrir a distância necessária entre os ponteiros.
    for _ in range(n + 1):
        fast = fast.next

    # Move ambos até 'fast' chegar ao fim; 'slow' ficará antes do nó a remover.
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove o nó alvo ajustando o ponteiro 'next' do nó anterior.
    slow.next = slow.next.next
    return dummy.next


class TestRemoveNthFromEnd(unittest.TestCase):

    def test_remove_segundo_do_fim(self):
        """Teste 1: Remove o 2º nó a partir do fim de [1,2,3,4,5] → [1,2,3,5]."""
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(remove_nth_from_end(head, 2)), [1, 2, 3, 5])

    def test_remove_ultimo(self):
        """Teste 2: Remove o 1º nó a partir do fim (último) → [1,2,3,4]."""
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(remove_nth_from_end(head, 1)), [1, 2, 3, 4])

    def test_remove_primeiro(self):
        """Teste 3: Remove o nó mais distante do fim (cabeça da lista) → [2,3,4,5]."""
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(to_list(remove_nth_from_end(head, 5)), [2, 3, 4, 5])

    def test_lista_com_um_elemento(self):
        """Teste 4: Lista com um único elemento, removendo-o → lista vazia."""
        head = build_list([1])
        self.assertIsNone(remove_nth_from_end(head, 1))

    def test_lista_com_dois_elementos_remove_primeiro(self):
        """Teste 5: Lista [1,2], remove o 2º do fim (cabeça) → [2]."""
        head = build_list([1, 2])
        self.assertEqual(to_list(remove_nth_from_end(head, 2)), [2])

    def test_lista_com_dois_elementos_remove_ultimo(self):
        """Teste 6: Lista [1,2], remove o 1º do fim (último) → [1]."""
        head = build_list([1, 2])
        self.assertEqual(to_list(remove_nth_from_end(head, 1)), [1])


if __name__ == "__main__":
    unittest.main(verbosity=2)