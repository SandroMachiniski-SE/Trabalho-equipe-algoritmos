class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove_duplicates(self):
        if self.head is None:
            return

        seen = set()
        current = self.head
        seen.add(current.data)
        while current.next:
            if current.next.data in seen:
                # Pula o nó duplicado
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next

# Teste
if __name__ == "__main__":
    lista = LinkedList()
    lista.append(1)
    lista.append(2)
    lista.append(2)
    lista.append(3)
    lista.append(3)
    lista.append(1)

    print("Antes de remover duplicatas:")
    lista.print_list()

    lista.remove_duplicates()

    print("Depois de remover duplicatas:")
    lista.print_list()