def how_many_computers(amount: int) -> str:
    """Склонение компьютеров"""
    amount_str = str(amount)
    if amount == 0:
        return 'Нет компьютеров'
    if amount < 0:
        return 'Введите положительное число'
    if amount_str[-1:] == '1' and amount_str[-2:] != '11':
        return f'{amount_str} компьютер'
    if amount_str[-1:] in (
        '2', '3', '4'
        ) and amount_str[-2:] not in (
            '12', '13', '14'
            ):
        return f'{amount_str} компьютера'
    return f'{amount_str} компьютеров'
