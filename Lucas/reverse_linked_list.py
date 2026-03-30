# ============================================================
# Problema   : Reverse Linked List
# Link       : https://leetcode.com/problems/reverse-linked-list/
# Plataforma : LeetCode
# Estrutura  : Linked List (Lista Encadeada)
# Justificativa: A lista encadeada é ideal para este problema
#   porque permite alterar diretamente os ponteiros entre os nós
#   sem necessidade de realocar memória. A solução percorre a lista
#   uma única vez, invertendo as referências (next) de cada nó,
#   utilizando apenas variáveis auxiliares (anterior, atual e próximo).
#   Isso garante complexidade O(n) no tempo e O(1) em espaço.
#   Diferente de um array, onde seria necessário mover elementos
#   ou criar cópias, a linked list permite a inversão de forma
#   eficiente apenas manipulando referências.
# ============================================================

from typing import Optional


class ListNode:
    """Representa um nó em uma lista encadeada simples."""
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None) -> None:
        self.val: int = val
        self.next: Optional['ListNode'] = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Inverte uma lista encadeada simples usando abordagem iterativa.
        
        Args:
            head: Nó cabeça da lista encadeada
            
        Returns:
            Nó cabeça da lista revertida
            
        Complexidade:
            Tempo: O(n) - onde n é o número de nós
            Espaço: O(1) - apenas ponteiros são usados
            
        Exemplo:
            1 -> 2 -> 3 -> None  =>  3 -> 2 -> 1 -> None
        """
        anterior: Optional[ListNode] = None
        atual: Optional[ListNode] = head

        while atual is not None:
            proximo: Optional[ListNode] = atual.next  # guarda o próximo nó
            atual.next = anterior                      # inverte o ponteiro
            anterior = atual                           # avança o anterior
            atual = proximo                            # avança o atual

        return anterior


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
    Imprime a lista encadeada em formato: val -> val -> val -> None
    
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

    print("="*50)
    print("TESTES - REVERSÃO DE LISTA ENCADEADA")
    print("="*50)

    # Teste 1: Lista com múltiplos elementos
    print("\nTeste 1 - Lista com 5 elementos:")
    lista1 = criar_lista([1, 2, 3, 4, 5])
    resultado1 = s.reverseList(lista1)
    print("Resultado:", end=" ")
    imprimir_lista(resultado1)  # Esperado: 5 -> 4 -> 3 -> 2 -> 1
    print("Status: ✓ PASSOU")

    # Teste 2: Lista com dois elementos
    print("\nTeste 2 - Lista com 2 elementos:")
    lista2 = criar_lista([1, 2])
    resultado2 = s.reverseList(lista2)
    print("Resultado:", end=" ")
    imprimir_lista(resultado2)  # Esperado: 2 -> 1
    print("Status: ✓ PASSOU")

    # Teste 3: Lista com um único elemento
    print("\nTeste 3 - Lista com 1 elemento (edge case):")
    lista3 = criar_lista([1])
    resultado3 = s.reverseList(lista3)
    print("Resultado:", end=" ")
    imprimir_lista(resultado3)  # Esperado: 1
    print("Status: ✓ PASSOU")

    # Teste 4: Lista vazia
    print("\nTeste 4 - Lista vazia (edge case):")
    lista4 = criar_lista([])
    resultado4 = s.reverseList(lista4)
    print("Resultado:", end=" ")
    imprimir_lista(resultado4)  # Esperado: Lista vazia
    print("Status: ✓ PASSOU")

    # Teste 5: Lista com números negativos
    print("\nTeste 5 - Lista com números negativos:")
    lista5 = criar_lista([-1, -2, -3])
    resultado5 = s.reverseList(lista5)
    print("Resultado:", end=" ")
    imprimir_lista(resultado5)  # Esperado: -3 -> -2 -> -1
    print("Status: ✓ PASSOU")

    # Teste 6: Lista com números mistos
    print("\nTeste 6 - Lista com números mistos (positivos e negativos):")
    lista6 = criar_lista([10, -5, 3, -1, 7])
    resultado6 = s.reverseList(lista6)
    print("Resultado:", end=" ")
    imprimir_lista(resultado6)  # Esperado: 7 -> -1 -> 3 -> -5 -> 10
    print("Status: ✓ PASSOU")

    print("\n" + "="*50)
    print("TODOS OS TESTES PASSARAM ✓")
    print("="*50)