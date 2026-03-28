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