def prime_numbers(a: int, b: int) -> list[int]:
    """Простые числа из диапазона"""
    result = []
    if a < 2 and b < 2:
        return []
    if a > b:
        a, b = b, a
    if a < 2:
        a = 2
    for i in range(a, b+1):
        if i % 2 == 0:
            if i == 2:
                result.append(i)
            continue
        d = 3
        while (d * d) <= i and i % d != 0:
            d += 2
        if (d * d) > i:
            result.append(i)
    return result
