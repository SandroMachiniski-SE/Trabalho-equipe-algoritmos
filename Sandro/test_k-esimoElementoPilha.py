# ============================================================
# Problema   : Testes - K-ésimo elemento da pilha
# Link       : N/A (teste da implementação própria)
# Plataforma : Implementação própria / Estrutura de Dados
# Estrutura  : Stack (Pilha) baseada em Array
# Justificativa: Este código utiliza a mesma estrutura de pilha
#   baseada em lista (array) para validar o funcionamento das
#   operações implementadas anteriormente, como push, pop, top
#   e acesso ao k-ésimo elemento. Os testes garantem que os
#   comportamentos esperados sejam atendidos, incluindo casos
#   válidos e tratamento de exceções (IndexError). A escolha
#   da pilha baseada em array mantém todas as operações em O(1),
#   permitindo validar eficiência e corretude da estrutura.
# ============================================================

if __name__ == "__main__":
    s = StackK()
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.top() == 30
    assert s.kth_from_top(1) == 30
    assert s.kth_from_top(2) == 20
    assert s.kth_from_top(3) == 10
    try:
        s.kth_from_top(4)
    except IndexError:
        print("k fora do intervalo (correto)")

    print("OK StackK testes")