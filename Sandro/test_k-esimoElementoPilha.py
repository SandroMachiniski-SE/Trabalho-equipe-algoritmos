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