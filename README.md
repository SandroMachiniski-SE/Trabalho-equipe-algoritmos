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
| **Sandro Machiniski** | Two Sum (Array) |
| **Diego Cunha** | Contains Duplicate, Product Except Self, Middle of Linked List, Remove Nth From End |

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
| `two_sum.py` | Encontrar dois números que somam um alvo | Sandro | O(n) time, O(n) space | - |
| `best_time_to_buy_and_sell_stock.py` | Encontrar maior lucro em compra/venda de ações | Lucas | O(n) time, O(1) space | 6 testes |
| `MaximumSubarray` | Subarray máximo com Algoritmo de Kadane | Lucas | O(n) time, O(1) space | 6 testes |
| `contains_duplicate.py` | Retorna True se existir valor repetido | Diego | O(n) time, O(n) space | 2 testes |
| `product_except_self.py` | Produto de todos exceto o atual (sem divisão) | Diego | O(n) time, O(n) space | 1 teste |

### 🔗 Listas Encadeadas

| Arquivo | Descrição | Autoria | Complexidade | Testes |
|---------|-----------|---------|--------------|--------|
| `reverse_linked_list.py` | Reverter uma lista encadeada | Lucas | O(n) time, O(1) space | 6 testes |
| `merge_two_sorted_lists.py` | Mesclar duas listas encadeadas ordenadas | Lucas | O(n + m) time, O(1) space | 6 testes |
| `middle_of_linked_list.py` | Encontrar o elemento central da lista | Diego | O(n) time, O(1) space | 1 teste |
| `remove_nth_from_end.py` | Remover o n-ésimo nó a partir do final | Diego | O(n) time, O(1) space | 1 teste |

### 📚 Pilhas

| Arquivo | Descrição | Autoria | Complexidade | Testes |
|---------|-----------|---------|--------------|--------|
| `min_stack.py` | Pilha com operação de mínimo em O(1) | Lucas | push/pop/top/getMin: O(1) | 6 testes |
| `valid_parentheses.py` | Validar sequência de parênteses/colchetes/chaves | Lucas | O(n) time, O(n) space | 8 testes |

---

## 🎯 Descrição dos Algoritmos

### 📊 Arrays

#### **Two Sum** (Sandro)
- **Objetivo:** Encontrar dois números em um array que somam um valor alvo
- **Estratégia:** Hash Map - Armazenar valores visitados para busca O(1)
- **Complexidade:** O(n) time, O(n) space
- **Caso de Uso:** Problemas de busca com par de elementos

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
- **Objetivo:** Identificar se algum elemento aparece mais de uma vez em um array.
- **Estratégia:** Utilização de `set()` para busca em tempo constante.
- **Complexidade:** O(n) time, O(n) space.

#### **Product of Array Except Self** (Diego)
- **Objetivo:** Calcular o produto de todos os números exceto o atual sem usar divisão.
- **Estratégia:** Técnica de Prefixos e Sufixos (duas passagens no array).
- **Complexidade:** O(n) time, O(n) space.

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

#### **Remove Nth Node From End** (Diego)
- **Objetivo:** Remover o n-ésimo nó a partir do final da lista
- **Estratégia:** Dois ponteiros + Dummy Node - Mantém distância fixa entre ponteiros
- **Complexidade:** O(n) time, O(1) space
- **Caso de Uso:** Manipulação segura de nós, especialmente remoção em listas encadeadas

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
python best_time_to_buy_and_sell_stock.py
python MaximumSubarray
python .\Diego\arrays\contains_duplicate.py
python .\Diego\arrays\product_except_self.py

# Listas Encadeadas
python reverse_linked_list.py
python merge_two_sorted_lists.py

# Pilhas
python min_stack.py
python valid_parentheses.py
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

- **Total de Arquivos:** 10
- **Total de Testes:** 43+
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
- **Pilhas:** LIFO (Last In, First Out), aplicações em validações
- **Técnicas de Algoritmo:** Greedy, Dynamic Programming, Two Pointers, Stack-based

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