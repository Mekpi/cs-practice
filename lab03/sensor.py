limit = float(input('Введите порог: '))
n = int(input('Введите количество записей: '))
all_records = 0
all_errors = 0
excesses = 0
max_record = 0
sum = 0

print(f'Введите {n} записей:')
for i in range(n):
    record = input()
    all_records += 1
    if record == 'error':
        all_errors += 1
    else:
        record = float(record)
        excesses += 1 if record > limit else 0
        max_record = max(record, max_record)
        sum += record
        
print(f'Всего записей: {all_records}')
print(f'Всего ошибок: {all_errors}')
print(f'Всего превышений: {excesses}')
print(f'Максимальное показание: {max_record:.1f}')
print(f'Среднее показание: {sum/(all_records-all_errors):.1f}')
