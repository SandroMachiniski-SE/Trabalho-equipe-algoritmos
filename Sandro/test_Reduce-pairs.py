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