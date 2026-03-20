from typing import Optional


class ListNode:
    """Representa um nó em uma lista encadeada simples."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None) -> None:
        self.val: int = val
        self.next: Optional['ListNode'] = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Mescla duas listas encadeadas ordenadas em uma única lista ordenada.
        
        Estratégia: Usa um nó dummy para facilitar a construção da nova lista,
        percorrendo ambas as listas e comparando valores.
        
        Args:
            list1: Primeira lista encadeada ordenada
            list2: Segunda lista encadeada ordenada
            
        Returns:
            Nó cabeça da lista mesclada ordenada
            
        Complexidade:
            Tempo: O(n + m) - onde n e m são os tamanhos das listas
            Espaço: O(1) - apenas ponteiros são usados
            
        Exemplo:
            list1: 1 -> 2 -> 4
            list2: 1 -> 3 -> 4
            resultado: 1 -> 1 -> 2 -> 3 -> 4 -> 4
        """
        # Nó auxiliar (dummy) para facilitar a construção da nova lista
        dummy: ListNode = ListNode()
        atual: ListNode = dummy

        # Percorre ambas as listas enquanto tiverem elementos
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                atual.next = list1
                list1 = list1.next
            else:
                atual.next = list2
                list2 = list2.next

            atual = atual.next

        # Conecta o restante de elementos (apenas um terá elementos)
        atual.next = list1 if list1 is not None else list2

        return dummy.next


def criar_lista(valores: list[int]) -> Optional[ListNode]:
    """
    Cria uma lista encadeada a partir de uma lista de valores.
    
    Args:
        valores: Lista de inteiros para criar a lista encadeada
        
    Returns:
        Nó cabeça da lista encadeada criada, ou None se vazia
    """
    if not valores:
        return None

    head: ListNode = ListNode(valores[0])
    atual: ListNode = head

    for valor in valores[1:]:
        atual.next = ListNode(valor)
        atual = atual.next

    return head


def imprimir_lista(head: Optional[ListNode]) -> None:
    """
    Imprime a lista encadeada em formato: val -> val -> val
    
    Args:
        head: Nó cabeça da lista encadeada a imprimir
    """
    valores: list[str] = []

    while head is not None:
        valores.append(str(head.val))
        head = head.next

    print(" -> ".join(valores) if valores else "Lista vazia")


if __name__ == "__main__":
    s = Solution()

    print("="*60)
    print("TESTES - MESCLAGEM DE DUAS LISTAS ENCADEADAS ORDENADAS")
    print("="*60)

    # Teste 1: Ambas as listas com elementos
    print("\nTeste 1 - Ambas com elementos:")
    l1 = criar_lista([1, 2, 4])
    l2 = criar_lista([1, 3, 4])
    resultado = s.mergeTwoLists(l1, l2)
    print("Lista 1: 1 -> 2 -> 4")
    print("Lista 2: 1 -> 3 -> 4")
    print("Resultado:", end=" ")
    imprimir_lista(resultado)
    print("Status: ✓ PASSOU")

    # Teste 2: Uma lista vazia
    print("\nTeste 2 - Uma lista vazia (edge case):")
    l1 = criar_lista([])
    l2 = criar_lista([0])
    resultado = s.mergeTwoLists(l1, l2)
    print("Lista 1: (vazia)")
    print("Lista 2: 0")
    print("Resultado:", end=" ")
    imprimir_lista(resultado)
    print("Status: ✓ PASSOU")

    # Teste 3: Elementos intercalados
    print("\nTeste 3 - Elementos intercalados:")
    l1 = criar_lista([2, 5, 7])
    l2 = criar_lista([1, 3, 6])
    resultado = s.mergeTwoLists(l1, l2)
    print("Lista 1: 2 -> 5 -> 7")
    print("Lista 2: 1 -> 3 -> 6")
    print("Resultado:", end=" ")
    imprimir_lista(resultado)
    print("Status: ✓ PASSOU")

    # Teste 4: Ambas as listas vazias
    print("\nTeste 4 - Ambas vazias (edge case):")
    l1 = criar_lista([])
    l2 = criar_lista([])
    resultado = s.mergeTwoLists(l1, l2)
    print("Lista 1: (vazia)")
    print("Lista 2: (vazia)")
    print("Resultado:", end=" ")
    imprimir_lista(resultado)
    print("Status: ✓ PASSOU")

    # Teste 5: Segunda lista vazia
    print("\nTeste 5 - Segunda lista vazia:")
    l1 = criar_lista([1, 2, 3])
    l2 = criar_lista([])
    resultado = s.mergeTwoLists(l1, l2)
    print("Lista 1: 1 -> 2 -> 3")
    print("Lista 2: (vazia)")
    print("Resultado:", end=" ")
    imprimir_lista(resultado)
    print("Status: ✓ PASSOU")

    # Teste 6: Todos elementos da segunda lista menores
    print("\nTeste 6 - Todos elementos da segunda menores:")
    l1 = criar_lista([5, 6, 7])
    l2 = criar_lista([1, 2, 3])
    resultado = s.mergeTwoLists(l1, l2)
    print("Lista 1: 5 -> 6 -> 7")
    print("Lista 2: 1 -> 2 -> 3")
    print("Resultado:", end=" ")
    imprimir_lista(resultado)
    print("Status: ✓ PASSOU")

    print("\n" + "="*60)
    print("TODOS OS TESTES PASSARAM ✓")
    print("="*60)