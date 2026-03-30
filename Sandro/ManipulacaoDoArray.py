# ============================================================
# Problema   : Manipulação de Array (Lista de Números)
# Link       : N/A (implementação própria)
# Plataforma : Implementação própria / Estrutura de Dados
# Estrutura  : Array (Lista em Python)
# Justificativa: A estrutura de array (lista em Python) é adequada
#   para este problema porque permite armazenar múltiplos valores
#   de forma sequencial e oferece operações prontas e eficientes,
#   como inserção (append), busca (operador in), ordenação (sorted)
#   e funções agregadas como max, min e sum. Essas operações são
#   otimizadas internamente e facilitam a manipulação dos dados.
#   Como o problema envolve leitura, análise e consulta de valores,
#   o uso de array é simples, direto e eficiente para esse tipo de
#   processamento.
# ============================================================

# criando uma lista para entrada do usuário

numeros = []
for i in range(5):
    valor = int(input(f"Digite o {i+1}° número: "))
    numeros.append(valor)


# mostrar as informações da lista
print("\nLista completa:", numeros )
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("Soma dos números:", sum(numeros))
print("Lista em ordem crescente:", sorted(numeros))


# verificar se um número específico está na lista

busca = int(input("\nDigite um número para verificar se está na lista: "))
if busca in numeros:
    print(f"O número {busca} está na lista!")
else:
    print(f"O número {busca} não está na lista.")