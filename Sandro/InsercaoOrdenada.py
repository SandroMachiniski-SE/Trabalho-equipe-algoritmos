# ============================================================
# Problema   : Inserção Ordenada em Lista Encadeada
# Link       : N/A (implementação própria)
# Plataforma : Implementação própria / Estrutura de Dados
# Estrutura  : Linked List (Lista Encadeada)
# Justificativa: A lista encadeada é adequada para este problema
#   porque permite inserir elementos em qualquer posição sem
#   necessidade de deslocar outros elementos, apenas ajustando
#   ponteiros. Durante a inserção, percorremos a lista até
#   encontrar a posição correta e atualizamos as referências
#   (next) para incluir o novo nó. Em estruturas como arrays,
#   seria necessário deslocar vários elementos para manter a
#   ordem, o que tornaria a operação menos eficiente (O(n)).
#   Já na lista encadeada, a inserção em si ocorre em O(1),
#   sendo necessário apenas o custo de busca O(n).
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_sorted(self, data):
        new_node = Node(data)

        # Caso a lista esteja vazia ou o novo valor seja menor que o primeiro
        if self.head is None or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        # Percorre até encontrar a posição correta
        current = self.head
        while current.next is not None and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Inserção de elementos em uma lista ordenada diretamente na inserção

lista = LinkedList()
lista.insert_sorted(54)
lista.insert_sorted(26)
lista.insert_sorted(93)
lista.insert_sorted(17)
lista.insert_sorted(77)
lista.insert_sorted(30)

lista.print_list()  # saída esperada: 17 -> 26 -> 31 -> 54 -> 77 -> 93