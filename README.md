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

## 👥 Integrantes

- Diego Cunha  
- Lucas Eufrasio  
- Sandro Machiniski  

---

## 🤖 IA Utilizada

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

| Arquivo | Descrição | Complexidade | Testes |
|---------|-----------|--------------|--------|
| `best_time_to_buy_and_sell_stock.py` | Encontrar maior lucro em compra/venda de ações | O(n) time, O(1) space | 6 testes |
| `MaximumSubarray` | Subarray máximo com Algoritmo de Kadane | O(n) time, O(1) space | 6 testes |

### 🔗 Listas Encadeadas

| Arquivo | Descrição | Complexidade | Testes |
|---------|-----------|--------------|--------|
| `reverse_linked_list.py` | Reverter uma lista encadeada | O(n) time, O(1) space | 6 testes |
| `merge_two_sorted_lists.py` | Mesclar duas listas encadeadas ordenadas | O(n + m) time, O(1) space | 6 testes |

### 📚 Pilhas

| Arquivo | Descrição | Complexidade | Testes |
|---------|-----------|--------------|--------|
| `min_stack.py` | Pilha com operação de mínimo em O(1) | push/pop/top/getMin: O(1) | 6 testes |
| `valid_parentheses.py` | Validar sequência de parênteses/colchetes/chaves | O(n) time, O(n) space | 8 testes |

---

## ✨ Melhorias Aplicadas

Todos os arquivos foram revisados e melhorados com:

### 📝 Documentação
- ✅ **Type Hints** - Tipos claros para parâmetros e retornos
- ✅ **Docstrings Completas** - Explicação de estratégia, argumentos, retorno e complexidade
- ✅ **Exemplos de Uso** - Demonstração de entrada/saída esperadas

### 🧪 Testes
- ✅ **Testes Abrangentes** - 6-8 testes por arquivo
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

# Listas Encadeadas
python reverse_linked_list.py
python merge_two_sorted_lists.py

# Pilhas
python min_stack.py
python valid_parentheses.py
```

Todos os testes serão executados automáticamente e mostram o status (✓ PASSOU ou ✗ FALHOU).

---

## 📊 Resumo de Testes

- **Total de Arquivos:** 6
- **Total de Testes:** 38+
- **Taxa de Sucesso:** 100% ✓

---