# ============================================================
# Problema   : Remove Adjacent Duplicates (Reduce Pairs)
# Link       : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Plataforma : LeetCode (variação)
# Estrutura  : Stack (Pilha)
# Justificativa: A pilha é adequada para este problema porque
#   permite comparar diretamente o elemento atual com o último
#   inserido (topo da pilha). Quando dois caracteres adjacentes
#   são iguais, o topo é removido, eliminando o par. Caso contrário,
#   o caractere é empilhado. Esse comportamento segue o padrão LIFO
#   e evita a necessidade de reprocessar a string inteira a cada
#   remoção. Assim, cada caractere é processado apenas uma vez,
#   resultando em complexidade O(n) no tempo e O(n) no espaço.
# ============================================================

def reduce_pairs(s: str) -> str:
    
    """
    Remove pares adjacentes idênticos repetidamente usando pilha.
    Retorna a string final.
    """
    pilha: list[str] = []
    for ch in s:
        if pilha and pilha[-1] == ch:
            # encontrou par adjacente igual -> desempilha (remove o par)
            pilha.pop()
        else:
            pilha.append(ch)
    return ''.join(pilha)