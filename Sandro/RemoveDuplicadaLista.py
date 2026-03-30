# ============================================================
# Problema   : Remover Duplicatas de Lista Encadeada
# Link       : N/A (implementação própria)
# Plataforma : Implementação própria / Estrutura de Dados
# Estrutura  : Linked List + Hash Set (Conjunto)
# Justificativa: A lista encadeada é utilizada para armazenar
#   os elementos de forma dinâmica, permitindo a remoção de nós
#   apenas ajustando ponteiros, sem necessidade de deslocamento
#   de dados. Para garantir eficiência na detecção de duplicatas,
#   é utilizado um conjunto (set), que permite verificar se um
#   elemento já foi visto em tempo O(1). Assim, ao percorrer a
#   lista uma única vez, é possível remover duplicatas de forma
#   eficiente, resultando em complexidade O(n) no tempo e O(n)
#   no espaço. Sem o uso do set, seria necessário comparar cada
#   elemento com os demais, levando a O(n²).
# ============================================================

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