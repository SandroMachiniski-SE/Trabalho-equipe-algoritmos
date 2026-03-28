from typing import List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack = []  # índices

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)

    return answer

if __name__ == "__main__":
    assert daily_temperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    print("daily_temperatures: testes ok")
