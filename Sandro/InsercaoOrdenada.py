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