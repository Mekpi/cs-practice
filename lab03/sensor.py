limit = float(input())
n = int(input())
all_records = 0
all_errors = 0

print(f'Введите {n} записей:')
for i in range(n):
    record = input()
    all_records += 1
    if record == 'error':
        all_errors += 1

print(f'Всего записей: {all_records}')
print(f'Всего ошибок: {all_errors}')
