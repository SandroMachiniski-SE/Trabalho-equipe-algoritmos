# 🤖 Trabalho — IA para Desenvolvimento + Revisão de Estruturas de Dados I

Repositório desenvolvido para a disciplina de Algoritmos Avançados, com o objetivo de revisar Estruturas de Dados I por meio da resolução de problemas no estilo *code interview*, utilizando Inteligência Artificial como apoio no desenvolvimento.

---

## 📚 Objetivo

Este projeto tem como finalidade:

- Aplicar conceitos de Arrays, Listas Encadeadas e Pilhas
- Resolver problemas clássicos de entrevistas técnicas
- Utilizar IA como ferramenta de apoio no desenvolvimento
- Desenvolver raciocínio lógico e análise de complexidade
- Documentar soluções e aprendizados

---

## 👥 Integrantes e Colaborações

| Integrante | Contribuições |
|-----------|--------------|
| **Lucas Eufrasio** | Best Time to Buy and Sell Stock, Maximum Subarray, Reverse Linked List, Merge Two Sorted Lists, Min Stack, Valid Parentheses (Código, Documentação, Type Hints, Testes) |
| **Diego Cunha** | Contains Duplicate, Product Except Self, Middle of Linked List, Remove Nth From End, Baseball Game, Daily Temperatures (Código, Documentação, Docstrings, Testes) |
| **Sandro Machiniski** | Two Sum, Inserção Ordenada em Lista Encadeada, Manipulação de Array, Remoção de Duplicatas em Lista Encadeada, Stack that supports searching for the k-th element from the top in O(1), Reduction of character sequences by adjacent pairs (iterative removal) |

---

## ⚙️ Requisitos

- **Python:** 3.8 ou superior
- **Dependências:** Nenhuma (apenas biblioteca padrão do Python)

Para verificar sua versão do Python:
```bash
python --version
```

---

- **Ferramenta:** ChatGPT  
- **Acesso:** Web (navegador)  

### 🔎 Como a IA foi utilizada

- Interpretação dos enunciados
- Geração de ideias de solução
- Revisão de código
- Explicação de algoritmos
- Análise de complexidade (tempo e memória)
- Sugestão de testes adicionais

---

## 📂 Estrutura do Repositório

### 📊 Arrays

| Arquivo | Descrição | Autoria | Complexidade | Testes |
|---------|-----------|---------|--------------|--------|
| `best_time_to_buy_and_sell_stock.py` | Encontrar maior lucro em compra/venda de ações | Lucas | O(n) time, O(1) space | 6 testes |
| `MaximumSubarray` | Subarray máximo com Algoritmo de Kadane | Lucas | O(n) time, O(1) space | 6 testes |
| `contains_duplicate.py` | Retorna True se existir valor repetido | Diego | O(n) time, O(n) space | 6 testes |
| `product_except_self.py` | Produto de todos exceto o atual (sem divisão) | Diego | O(n) time, O(n) space | 6 teste |
| `TwoSum.py` | Encontrar dois números que somam um alvo | Sandro | O(n) time, O(n) space | 2 testes |
| `ManipulacaoDoArray.py` | Leitura interativa, exibição de estatísticas e busca em array | Sandro | O(n) time, O(n) space | - |

### 🔗 Listas Encadeadas

| Arquivo | Descrição | Autoria | Complexidade | Testes |
|---------|-----------|---------|--------------|--------|
| `reverse_linked_list.py` | Reverter uma lista encadeada | Lucas | O(n) time, O(1) space | 6 testes |
| `merge_two_sorted_lists.py` | Mesclar duas listas encadeadas ordenadas | Lucas | O(n + m) time, O(1) space | 6 testes |
| `middle_of_linked_list.py` | Encontrar o elemento central da lista | Diego | O(n) time, O(1) space | 6 teste |
| `remove_nth_from_end.py` | Remover o n-ésimo nó a partir do final | Diego | O(n) time, O(1) space | 6 teste |
| `InsercaoOrdenada.py` | Inserção ordenada em lista encadeada | Sandro | O(n) time, O(1) space | - |
| `RemoveDuplicadaLista.py` | Remoção de nós duplicados em lista encadeada | Sandro | O(n) time, O(n) space | 1 teste |

### 📚 Pilhas

| Arquivo | Descrição | Autoria | Complexidade | Testes |
|---------|-----------|---------|--------------|--------|
| `min_stack.py` | Pilha com operação de mínimo em O(1) | Lucas | push/pop/top/getMin: O(1) | 6 testes |
| `valid_parentheses.py` | Validar sequência de parênteses/colchetes/chaves | Lucas | O(n) time, O(n) space | 8 testes |
| `baseball_game.py` | Simulação de pontuação com operações em pilha | Diego | O(n) time, O(n) space | 6 testes |
| `daily_temperatures.py` | Dias até temperatura maior usando pilha monotônica | Diego | O(n) time, O(n) space | 6 testes |
| `search for the k-th` | Pilha que suporta buscar o k-ésimo elemento do topo | Sandro | O(1) | 4 testes |
| `Adjacent pair reduction` | Redução de sequência de caracteres por pares adjacentes  | Sandro | O(n) | 6 testes |

---

## 🎯 Descrição dos Algoritmos

### 📊 Arrays

#### **Two Sum** (Sandro)
- **Objetivo:** Encontrar dois números em um array que somam um valor alvo
- **Estratégia:** Hash Map - Armazenar valores visitados para busca O(1)
- **Complexidade:** O(n) time, O(n) space
- **Caso de Uso:** Problemas de busca com par de elementos

#### **Manipulação de Array** (Sandro)
- **Objetivo:** Ler valores do usuário, exibir estatísticas (maior, menor, soma, ordenação) e verificar presença de elemento
- **Estratégia:** Funções built-in do Python (`max`, `min`, `sum`, `sorted`) e operador `in`
- **Complexidade:** O(n) time, O(n) space
- **Caso de Uso:** Operações básicas de análise sobre arrays

#### **Best Time to Buy and Sell Stock** (Lucas)
- **Objetivo:** Encontrar o maior lucro possível comprando e vendendo uma ação uma única vez
- **Estratégia:** Greedy - Rastrear o preço mínimo e calcular lucro máximo em cada iteração
- **Complexidade:** O(n) time, O(1) space
- **Caso de Uso:** Otimizar decisões financeiras com histórico de preços

#### **Maximum Subarray (Algoritmo de Kadane)** (Lucas)
- **Objetivo:** Encontrar o subarray contíguo com maior soma
- **Estratégia:** Dynamic Programming - Rastrear soma máxima terminando em cada posição
- **Complexidade:** O(n) time, O(1) space
- **Caso de Uso:** Problemas de otimização com subarrays

#### **Contains Duplicate** (Diego)
- **Objetivo:** Identificar se algum elemento aparece mais de uma vez em um array
- **Estratégia:** Utilização de `set()` para busca em tempo constante
- **Complexidade:** O(n) time, O(n) space
- **Testes:** Lista com duplicata, sem duplicata, lista vazia, um elemento, negativos duplicados, todos iguais

#### **Product of Array Except Self** (Diego)
- **Objetivo:** Calcular o produto de todos os números exceto o atual sem usar divisão
- **Estratégia:** Técnica de Prefixos e Sufixos (duas passagens no array)
- **Complexidade:** O(n) time, O(1) space extra
- **Testes:** Caso clássico, lista com zero, dois zeros, negativos, dois elementos, um elemento

### 🔗 Listas Encadeadas

#### **Reverse Linked List** (Lucas)
- **Objetivo:** Inverter a ordem dos elementos de uma lista encadeada
- **Estratégia:** Iterativo - Manipular ponteiros em uma única passagem
- **Complexidade:** O(n) time, O(1) space
- **Caso de Uso:** Manipulação eficiente de estruturas encadeadas

#### **Merge Two Sorted Lists** (Lucas)
- **Objetivo:** Mesclar duas listas encadeadas ordenadas em uma única lista ordenada
- **Estratégia:** Two Pointers + Dummy Node - Comparar elementos e conectar
- **Complexidade:** O(n + m) time, O(1) space
- **Caso de Uso:** Merge Sort, fusão eficiente de dados ordenados

#### **Middle of the Linked List** (Diego)
- **Objetivo:** Encontrar o nó central da lista encadeada
- **Estratégia:** Two Pointers (Lento/Rápido) - Um ponteiro avança 1 passo e o outro 2 passos
- **Complexidade:** O(n) time, O(1) space
- **Caso de Uso:** Divisão de listas, algoritmos de busca e otimização de travessia
- **Testes:** Lista ímpar, lista par (segundo nó do meio), um elemento, dois elementos, lista vazia, três elementos

#### **Remove Nth Node From End** (Diego)
- **Objetivo:** Remover o n-ésimo nó a partir do final da lista
- **Estratégia:** Dois Ponteiros + Dummy Node - Mantém distância fixa de n+1 entre ponteiros
- **Complexidade:** O(n) time, O(1) space
- **Caso de Uso:** Manipulação segura de nós, especialmente remoção em listas encadeadas
- **Testes:** Remove 2º do fim, remove último, remove cabeça, um elemento, dois elementos (ambos os casos)

#### **Inserção Ordenada em Lista Encadeada** (Sandro)
- **Objetivo:** Inserir um elemento na posição correta em uma lista encadeada já ordenada
- **Estratégia:** Percorrer a lista até encontrar a posição de inserção e ajustar os ponteiros
- **Complexidade:** O(n) time, O(1) space
- **Caso de Uso:** Manutenção de listas ordenadas sem reordenação completa

#### **Remoção de Duplicatas em Lista Encadeada** (Sandro)
- **Objetivo:** Remover nós com valores repetidos de uma lista encadeada
- **Estratégia:** Set de valores visitados para detecção em O(1) e ajuste de ponteiros para remoção
- **Complexidade:** O(n) time, O(n) space
- **Caso de Uso:** Limpeza de dados em estruturas encadeadas

### 📚 Pilhas

#### **Min Stack** (Lucas)
- **Objetivo:** Implementar uma pilha que obtém o mínimo em O(1)
- **Estratégia:** Duas Pilhas - Uma auxiliar rastreia mínimos em cada nível
- **Complexidade:** Todas operações O(1)
- **Caso de Uso:** Otimizar operações frequentes de busca de mínimo

#### **Valid Parentheses** (Lucas)
- **Objetivo:** Validar se uma sequência de parênteses/colchetes/chaves está balanceada
- **Estratégia:** Stack - Empilar aberturas, desempilhar ao encontrar fechamentos
- **Complexidade:** O(n) time, O(n) space
- **Caso de Uso:** Validação de sintaxe, parsing de expressões

#### **Baseball Game** (Diego)
- **Objetivo:** Simular um sistema de pontuação baseado em operações sequenciais
- **Estratégia:** Stack - Empilhar pontuações válidas e aplicar operações (`+`, `D`, `C`)
- **Complexidade:** O(n) time, O(n) space
- **Caso de Uso:** Simulação de estados com histórico mutável
- **Testes:** Caso clássico, apenas números, operação D, operação C, operação +, sequência mista com negativos

#### **Daily Temperatures** (Diego)
- **Objetivo:** Para cada dia, calcular quantos dias faltam até uma temperatura maior
- **Estratégia:** Stack Monotônica Decrescente - Empilhar índices sem resposta e resolver ao encontrar temperatura maior
- **Complexidade:** O(n) time, O(n) space
- **Caso de Uso:** Problemas de "próximo elemento maior" em sequências
- **Testes:** Caso clássico, sequência crescente, decrescente, valores iguais, um elemento, pico no meio

#### **search for the k-th** (Sandro)
- **Objetivo:** buscar o k-ésimo elemento do topo
- **Estratégia:** Criar uma pilha que suporte push, pop, top, len e uma operação
- **Complexidade:** O(1) time, O(n) space
- **Caso de Uso:** push(10), push(20), push(30)
- **Testes:** Testes funcionais básicos, Testes de erro,  consistência, Teste simples de carga

#### **Adjacent pair reduction** (Sandro)
- **Objetivo:** reduzir removendo repetidamente pares adjacentes idênticos de caracteres até que não seja mais possível
- **Estratégia:** Percorer a string da esquerda para a direita e usamos uma pilha (lista) para manter os caracteres que "sobrevivem" até o ponto atual.
- **Complexidade:** O(n) time, O(n) space
- **Caso de Uso:** Limpeza/simplificação de entradas de texto
- **Testes:** Entrada vazia, par simples adjacente, encadeamento, manter iguais, remoção de todos, test_idempotencia

Todos os arquivos foram revisados e melhorados com:

### 📝 Documentação
- ✅ **Type Hints** - Tipos claros para parâmetros e retornos
- ✅ **Docstrings Completas** - Explicação de estratégia, argumentos, retorno e complexidade
- ✅ **Exemplos de Uso** - Demonstração de entrada/saída esperadas

### 🧪 Testes
- ✅ **Testes Abrangentes** - testes por arquivo
- ✅ **Edge Cases** - Listas vazias, um elemento, valores duplicados, etc
- ✅ **Validação Detalhada** - Cada teste mostra entrada, resultado e status

### 🔧 Código
- ✅ **Tratamento de Erros** - ValueError/IndexError para entradas inválidas
- ✅ **Análise de Complexidade** - Tempo e espaço documentados
- ✅ **Código Legível** - Variáveis nomeadas claramente com comentários

---

## 🚀 Como Executar

Cada arquivo pode ser executado diretamente:

```bash
# Arrays
python Lucas\best_time_to_buy_and_sell_stock.py
python Lucas\MaximumSubarray.py
python Diego\arrays\contains_duplicate.py
python Diego\arrays\product_except_self.py
python Sandro\TwoSum.py
python Sandro\ManipulacaoDoArray.py

# Listas Encadeadas
python Lucas\reverse_linked_list.py
python Lucas\merge_two_sorted_lists.py
python Diego\linked_lists\middle_of_linked_list.py
python Diego\linked_lists\remove_nth_from_end.py
python Sandro\InsercaoOrdenada.py
python Sandro\RemoveDuplicadaLista.py


# Pilhas
python Lucas\min_stack.py
python Lucas\valid_parentheses.py
python Diego\stacks\baseball_game.py
python Diego\stacks\daily_temperatures.py
python Sandro\k-esimoElementoPilha.py
python Sandro\Reduce-pairs.py

```

Todos os testes serão executados automáticamente e mostram o status (✓ PASSOU ou ✗ FALHOU).

---

## 📋 Exemplos de Execução

### Best Time to Buy and Sell Stock
```
============================================================
TESTES - MELHOR TEMPO PARA COMPRAR E VENDER AÇÕES
============================================================

Teste 1 - Caso clássico com lucro:
Preços: [7, 1, 5, 3, 6, 4]
Resultado: 5 (Esperado: 5)
Explicação: Compra em 1, vende em 6 => Lucro = 5
Status: ✓ PASSOU
```

### Valid Parentheses
```
============================================================
TESTES - VALIDAÇÃO DE PARÊNTESES
============================================================

Teste 1 - Parênteses simples válido:
Input: '()'
Resultado: True (Esperado: True)
Status: ✓ PASSOU

Teste 2 - Múltiplos tipos de parênteses:
Input: '()[]{}'
Resultado: True (Esperado: True)
Status: ✓ PASSOU
```

### Reverse Linked List
```
============================================================
TESTES - REVERSÃO DE LISTA ENCADEADA
============================================================

Teste 1 - Lista com 5 elementos:
Resultado: 5 -> 4 -> 3 -> 2 -> 1
Status: ✓ PASSOU
```

---

## 📊 Resumo de Testes

- **Total de Arquivos:** 16
- **Total de Testes:** 75+
- **Taxa de Sucesso:** 100% ✓

---

## 📚 Recursos e Referências

### Livros e Materiais
- **"Cracking the Coding Interview"** - Gayle Laakmann McDowell
- **"Introduction to Algorithms"** - Cormen, Leiserson, Rivest, Stein
- **"Data Structures and Algorithms in Python"** - Goodrich, Tamassia, Goldwasser

### Conceitos Estudados
- **Análise Assintótica:** Notação Big O para tempo e espaço
- **Arrays:** Busca, otimização de espaço e tempo
- **Listas Encadeadas:** Manipulação de ponteiros, reversão, mesclagem
- **Pilhas:** LIFO (Last In, First Out), aplicações em validações e simulações
- **Técnicas de Algoritmo:** Greedy, Dynamic Programming, Two Pointers, Stack Monotônica, Prefixos e Sufixos

### Plataformas de Referência
- LeetCode (Problemas de entrevista técnica)
- HackerRank (Problemas algorítmicos)
- GeeksforGeeks (Explicações de conceitos)

---

## 📝 Notas de Implementação

### Type Hints (Python 3.8+)
Todos os arquivos utilizam type hints para melhor documentação e detecção de erros:
```python
from typing import Optional, List, Dict

def funcao(param: int) -> str:
    """Função com type hints."""
    pass
```

### Docstrings
Cada função possui docstring completa com:
- Descrição clara do que faz
- Argumentos (Args)
- Retorno (Returns)
- Exceções (Raises)
- Complexidade (Tempo e Espaço)
- Exemplos de uso

### Testes Unitários
Cada arquivo inclui:
- Testes de casos normais
- Testes de edge cases
- Validação de saída esperada
- Formatação clara de resultados

---

## 🎓 Aprendizados Principais

1. **Importância da Análise de Complexidade** - Permite escolher o melhor algoritmo
2. **Manipulação de Estruturas de Dados** - Fundamental para otimização
3. **Type Safety** - Type hints ajudam na manutenção e refatoração
4. **Testes Abrangentes** - Essencial para garantir qualidade
5. **Documentação Clara** - Facilita entendimento e review de código

---

## 📞 Contato e Contribuições

Para sugestões ou melhorias:
- Abrir uma issue no repositório
- Fazer um pull request com melhorias
- Contactar os integrantes do projeto

---

**Última Atualização:** Março de 2026 | **Status:** Em Desenvolvimento ✓
