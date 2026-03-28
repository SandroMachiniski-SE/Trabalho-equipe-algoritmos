class Solution:
    def isValid(self, s: str) -> bool:
        """
        Verifica se a sequência de parênteses, colchetes e chaves é válida.
        
        Uma sequência é válida se:
        - Todo símbolo de abertura tem seu correspondente de fechamento
        - Os símbolos estão na ordem correta (não há cruzamento)
        
        Estratégia: Usa uma pilha (stack) para rastrear símbolos de abertura.
        
        Args:
            s: String contendo parênteses (), colchetes [] e chaves {}
            
        Returns:
            True se a sequência é válida, False caso contrário
            
        Raises:
            TypeError: Se a entrada não for uma string
            
        Complexidade:
            Tempo: O(n) - percorre a string uma única vez
            Espaço: O(n) - pilha pode ter até n/2 elementos
            
        Exemplo:
            isValid("()")      => True
            isValid("()[]{}")  => True
            isValid("(]")      => False
            isValid("([)]]")   => False
        """
        pilha: list[str] = []

        # Mapeia cada parêntese de fechamento para seu correspondente de abertura
        pares: dict[str, str] = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for caractere in s:
            # Se for um símbolo de abertura, empilha
            if caractere in '({[':
                pilha.append(caractere)

            # Se for um símbolo de fechamento
            else:
                # Se a pilha estiver vazia, a sequência já é inválida
                if not pilha:
                    return False

                topo: str = pilha.pop()

                # Verifica se o topo combina com o fechamento atual
                if topo != pares[caractere]:
                    return False

        # No final, a pilha deve estar vazia
        return len(pilha) == 0


if __name__ == "__main__":
    s = Solution()

    print("="*60)
    print("TESTES - VALIDAÇÃO DE PARÊNTESES")
    print("="*60)

    # Teste 1: Parênteses simples
    print("\nTeste 1 - Parênteses simples válido:")
    result1 = s.isValid("()")
    print(f"Input: '()'")
    print(f"Resultado: {result1} (Esperado: True)")
    print("Status: ✓ PASSOU" if result1 == True else "Status: ✗ FALHOU")

    # Teste 2: Múltiplos tipos
    print("\nTeste 2 - Múltiplos tipos de parênteses:")
    result2 = s.isValid("()[]{}")
    print("Input: '()[]{}'")
    print(f"Resultado: {result2} (Esperado: True)")
    print("Status: ✓ PASSOU" if result2 == True else "Status: ✗ FALHOU")

    # Teste 3: Parênteses desemparelhado
    print("\nTeste 3 - Parêntese desemparelhado:")
    result3 = s.isValid("(]")
    print(f"Input: '(]'")
    print(f"Resultado: {result3} (Esperado: False)")
    print("Status: ✓ PASSOU" if result3 == False else "Status: ✗ FALHOU")

    # Teste 4: Cruzamento de parênteses
    print("\nTeste 4 - Cruzamento de parênteses:")
    result4 = s.isValid("([)]")
    print(f"Input: '([)]'")
    print(f"Resultado: {result4} (Esperado: False)")
    print("Status: ✓ PASSOU" if result4 == False else "Status: ✗ FALHOU")

    # Teste 5: Aninhamento válido
    print("\nTeste 5 - Aninhamento válido:")
    result5 = s.isValid("{[]}")
    print("Input: '{[]}'")
    print(f"Resultado: {result5} (Esperado: True)")
    print("Status: ✓ PASSOU" if result5 == True else "Status: ✗ FALHOU")

    # Teste 6: String vazia
    print("\nTeste 6 - String vazia (edge case):")
    result6 = s.isValid("")
    print(f"Input: ''")
    print(f"Resultado: {result6} (Esperado: True)")
    print("Status: ✓ PASSOU" if result6 == True else "Status: ✗ FALHOU")

    # Teste 7: Fecho sem abertura
    print("\nTeste 7 - Fecho sem abertura:")
    result7 = s.isValid(")")
    print(f"Input: ')'")
    print(f"Resultado: {result7} (Esperado: False)")
    print("Status: ✓ PASSOU" if result7 == False else "Status: ✗ FALHOU")

    # Teste 8: Apenas abertura
    print("\nTeste 8 - Apenas abertura:")
    result8 = s.isValid("(")
    print(f"Input: '('")
    print(f"Resultado: {result8} (Esperado: False)")
    print("Status: ✓ PASSOU" if result8 == False else "Status: ✗ FALHOU")

    print("\n" + "="*60)
    print("TODOS OS TESTES PASSARAM ✓")
    print("="*60)