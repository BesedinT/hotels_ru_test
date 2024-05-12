def common_divisors(numbers_list: list[int]) -> list[int]:
    """Общие делители"""
    min_number = min(numbers_list)
    numbers_list.remove(min_number)
    result = []
    for i in range(1, (min_number//2)+1):
        if min_number % i == 0:
            result.append(i)
    result.append(min_number)
    for number in numbers_list:
        result_del = []
        for i in result:
            if number % i != 0:
                result_del.append(i)
        for number_del in result_del:
            result.remove(number_del)
    return result
