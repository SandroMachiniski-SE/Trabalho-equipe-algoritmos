# ============================================================
# Problema   : Min Stack
# Link       : https://leetcode.com/problems/min-stack/
# Plataforma : LeetCode
# Estrutura  : Stack (Pilha) com pilha auxiliar
# Justificativa: A pilha é a estrutura ideal porque todas as
#   operações exigidas pelo problema acontecem no topo, como
#   inserção, remoção e consulta. Para garantir getMin() em O(1),
#   a solução utiliza uma segunda pilha auxiliar que armazena os
#   menores valores conforme os elementos são inseridos. Assim,
#   sempre que um novo valor menor ou igual ao mínimo atual entra,
#   ele também é colocado na min_stack. Isso evita percorrer toda
#   a pilha principal para descobrir o menor elemento, o que
#   levaria O(n). Dessa forma, push, pop, top e getMin permanecem
#   com complexidade O(1).
# ============================================================

class MinStack:
    """
    Implementa uma pilha com operação de obter o mínimo em O(1).
    
    Estratégia: Usa duas pilhas - uma principal e outra auxiliar que rastreia
    o mínimo em cada nível.
    
    Complexidade:
        push: O(1)
        pop: O(1)
        top: O(1)
        getMin: O(1)
    """
    
    def __init__(self) -> None:
        self.stack: list[int] = []      # pilha principal
        self.min_stack: list[int] = []  # pilha auxiliar para mínimos

    def push(self, val: int) -> None:
        """
        Adiciona um valor à pilha.
        
        Args:
            val: Inteiro a ser adicionado
        """
        self.stack.append(val)

        # Se a pilha de mínimos estiver vazia ou o valor for menor ou igual
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Remove o elemento do topo da pilha.
        
        Raises:
            IndexError: Se a pilha estiver vazia
        """
        if not self.stack:
            raise IndexError("pop from empty stack")
            
        # Se o valor removido for o menor, remove também da min_stack
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def top(self) -> int:
        """
        Retorna o elemento do topo sem remover.
        
        Returns:
            Inteiro no topo da pilha
            
        Raises:
            IndexError: Se a pilha estiver vazia
        """
        if not self.stack:
            raise IndexError("top from empty stack")
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Retorna o mínimo elemento da pilha.
        
        Returns:
            Inteiro representando o valor mínimo
            
        Raises:
            IndexError: Se a pilha estiver vazia
        """
        if not self.min_stack:
            raise IndexError("getMin from empty stack")
        return self.min_stack[-1]


if __name__ == "__main__":
    print("="*60)
    print("TESTES - MIN STACK (PILHA COM MÍNIMO)")
    print("="*60)

    # Teste 1: Operações básicas
    print("\nTeste 1 - Operações básicas:")
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(f"Após 3 pushes [-2, 0, -3]")
    print(f"getMin(): {s.getMin()} (Esperado: -3)")
    print(f"top(): {s.top()} (Esperado: -3)")
    assert s.getMin() == -3 and s.top() == -3
    print("Status: ✓ PASSOU")

    # Teste 2: Pop e verificação
    print("\nTeste 2 - Pop e novas consultas:")
    s.pop()
    print(f"Após pop()")
    print(f"top(): {s.top()} (Esperado: 0)")
    print(f"getMin(): {s.getMin()} (Esperado: -2)")
    assert s.top() == 0 and s.getMin() == -2
    print("Status: ✓ PASSOU")

    # Teste 3: Push com novo mínimo
    print("\nTeste 3 - Push com novo mínimo:")
    s.push(-5)
    print(f"Após push(-5)")
    print(f"getMin(): {s.getMin()} (Esperado: -5)")
    assert s.getMin() == -5
    print("Status: ✓ PASSOU")

    # Teste 4: Pop do novo mínimo
    print("\nTeste 4 - Pop do novo mínimo:")
    s.pop()
    print(f"Após pop() de -5")
    print(f"getMin(): {s.getMin()} (Esperado: -2)")
    assert s.getMin() == -2
    print("Status: ✓ PASSOU")

    # Teste 5: Valores duplicados
    print("\nTeste 5 - Valores duplicados como mínimo:")
    s2 = MinStack()
    s2.push(1)
    s2.push(1)
    s2.push(1)
    print(f"Stack com [1, 1, 1]")
    print(f"getMin(): {s2.getMin()} (Esperado: 1)")
    s2.pop()
    print(f"Após um pop")
    print(f"getMin(): {s2.getMin()} (Esperado: 1)")
    assert s2.getMin() == 1
    print("Status: ✓ PASSOU")

    # Teste 6: Números mistos (positivos e negativos)
    print("\nTeste 6 - Números misto (positivos e negativos):")
    s3 = MinStack()
    s3.push(3)
    s3.push(-1)
    s3.push(5)
    s3.push(-2)
    print(f"Stack com [3, -1, 5, -2]")
    print(f"getMin(): {s3.getMin()} (Esperado: -2)")
    s3.pop()  # Remove -2
    print(f"Após pop() de -2")
    print(f"getMin(): {s3.getMin()} (Esperado: -1)")
    assert s3.getMin() == -1
    print("Status: ✓ PASSOU")

    print("\n" + "="*60)
    print("TODOS OS TESTES PASSARAM ✓")
    print("="*60)