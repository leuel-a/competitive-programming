from collections import deque

def main() -> None:
    n, d = input().split()
    candidates = list(map(int, input().split()))

    i = j = _sum = 0
    _deque = deque([])
    while j < len(candidates):
        while _deque and candidates[_deque[-1]] < candidates[j]:
            _deque.pop()
        _deque.append(j)

        _sum += candidates[j]
        if _sum >= d:
            while i <= _deque[0] <= j:
                _deque.pop()
            


