limit = float(input('Введите порог: '))
n = int(input('Введите количество записей: '))
all_records = 0
all_errors = 0
excesses = 0
max_record = float('-inf')
sum = 0

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
        
print(all_records)
print(all_errors)
print(excesses)
print(f'{max_record:.1f}')
print(f'{sum/(all_records-all_errors):.1f}')
