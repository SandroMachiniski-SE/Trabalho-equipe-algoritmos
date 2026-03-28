import unittest
from typing import List


def verificar_duplicados(numeros: List[int]) -> bool:
    """
    Esta função recebe uma lista de números inteiros e retorna True
    se algum número aparecer mais de uma vez.
    """

    # Criamos um 'set' (conjunto). No Python, conjuntos não aceitam itens repetidos
    # e são muito rápidos para busca de informações.
    vistos = set()

    # Iniciamos um laço de repetição para olhar cada número da lista, um por um.
    for num in numeros:

        # Verificamos se o número atual já foi adicionado ao nosso conjunto 'vistos'.
        if num in vistos:
            # Se ele já está no conjunto, significa que encontramos uma duplicata.
            # O 'return' encerra a função de imediato enviando o valor True.
            return True

        # Se o número não estava no conjunto, nós o adicionamos agora
        # para que possamos checar se ele aparece de novo nos próximos ciclos.
        vistos.add(num)

    # Se o laço 'for' terminar de percorrer toda a lista e nunca entrar no 'if',
    # significa que todos os números são únicos.
    return False


class TestVerificarDuplicados(unittest.TestCase):

    def test_lista_com_duplicata_simples(self):
        """Teste 1: Lista com um número repetido deve retornar True."""
        self.assertTrue(verificar_duplicados([1, 2, 3, 1]))

    def test_lista_sem_duplicatas(self):
        """Teste 2: Lista com todos os números diferentes deve retornar False."""
        self.assertFalse(verificar_duplicados([1, 2, 3, 4]))

    def test_lista_vazia(self):
        """Teste 3: Lista vazia não possui duplicatas, deve retornar False."""
        self.assertFalse(verificar_duplicados([]))

    def test_lista_com_um_elemento(self):
        """Teste 4: Lista com apenas um elemento nunca terá duplicata."""
        self.assertFalse(verificar_duplicados([42]))

    def test_lista_com_negativos_duplicados(self):
        """Teste 5: Deve detectar duplicatas em números negativos."""
        self.assertTrue(verificar_duplicados([-1, -2, -3, -1]))

    def test_todos_elementos_iguais(self):
        """Teste 6: Lista onde todos os elementos são iguais deve retornar True."""
        self.assertTrue(verificar_duplicados([7, 7, 7, 7]))


if __name__ == "__main__":
    unittest.main(verbosity=2)