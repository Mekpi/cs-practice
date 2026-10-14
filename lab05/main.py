from tablestats import *

path = input()

with open(path, 'r', encoding='utf-8') as table:
    rows = read_rows(table)

counts = count_types(rows)
errors = total_minutes(rows, 'ошибка')

print(len(rows))
print(len(counts))
print(errors)

with open('summary.csv', 'w', encoding='utf-8') as out:
    out.write(to_csv(counts))