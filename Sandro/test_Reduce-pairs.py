# ============================================================
# Problema   : Testes - Remove Adjacent Duplicates (Reduce Pairs)
# Link       : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Plataforma : LeetCode (variação) / Teste de implementação
# Estrutura  : Stack (Pilha)
# Justificativa: Este código valida a função de remoção de pares
#   adjacentes utilizando uma pilha. Os testes cobrem diferentes
#   cenários, incluindo strings com múltiplas remoções, casos sem
#   duplicatas e casos extremos como string vazia. A estrutura de
#   pilha é mantida, pois a função testada depende do comportamento
#   LIFO para remover pares corretamente. Os testes garantem que a
#   lógica esteja correta e que cada entrada produza a saída esperada,
#   assegurando a confiabilidade da solução.
# ============================================================

if __name__ == "__main__":
    exemplos = {
        "abbaca": "ca",
        "azxxzy": "ay",
        "aabccb": "",
        "abc": "abc",
        "": "",
        "aa": "",
        "abba": "",  # abba -> remove bb -> aa -> remove aa -> ""
    }
    for entrada, esperado in exemplos.items():
        saida = reduce_pairs(entrada)
        print(f"{entrada!r} -> {saida!r} (esperado: {esperado!r})")
        assert saida == esperado
    print("OK reduce_pairs testes")