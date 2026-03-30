# ============================================================
# Problema   : K-ésimo elemento da pilha
# Link       : N/A (implementação própria)
# Plataforma : Implementação própria / Estrutura de Dados
# Estrutura  : Stack (Pilha) baseada em Array (lista Python)
# Justificativa: A pilha foi implementada utilizando uma lista
#   dinâmica (array) do Python, que oferece operações eficientes
#   no final da estrutura, como append e pop em O(1). Além disso,
#   o uso de indexação negativa permite acessar diretamente o
#   k-ésimo elemento a partir do topo (self._data[-k]) também em
#   O(1), sem necessidade de percorrer a pilha. Isso torna a
#   solução mais eficiente do que uma pilha tradicional baseada
#   apenas em operações sequenciais, onde seria necessário iterar
#   até o elemento desejado. Assim, todas as operações principais
#   (push, pop, top e kth_from_top) possuem complexidade O(1).
# ============================================================

from typing import Any, List

class StackK:
    
    """
    Pilha com acesso O(1) ao k-ésimo elemento a partir do topo.
    Implementação: usamos uma lista interna; kth_from_top(k) acessa a partir do final:
        kth_from_top(k) -> self._data[-k]
    Todas as operações são O(1) em Python: append, pop e index negativo.
    """
    def __init__(self):
        self._data: List[Any] = []

    def push(self, x: Any) -> None:
        self._data.append(x)

    def pop(self) -> Any:
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def top(self) -> Any:
        if not self._data:
            raise IndexError("top from empty stack")
        return self._data[-1]

    def kth_from_top(self, k: int) -> Any:
        """
        Retorna o k-ésimo elemento a partir do topo (k=1 -> topo).
        Lança IndexError se k < 1 ou k > len(self).
        """
        if k < 1 or k > len(self._data):
            raise IndexError("k out of range")
        return self._data[-k]

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"StackK({self._data!r})"