
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