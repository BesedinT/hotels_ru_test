def multiplication_table(number):
    """Таблица умножения"""
    for i in range(1, number+1):
        for j in range(i, i*number+1, i):
            print(j, end='\t')
        print()
