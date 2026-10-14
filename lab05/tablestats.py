def read_rows(lines):
    header = lines.readline().strip().split(',')
    rows = []
    for line in lines:
        row = {}
        line = line.strip().split(',')

        if len(header) != len(line):
            continue
        for j in range(len(header)):
            row[header[j]] = line[j].strip()
        rows.append(row)
    return rows


def count_types(rows):
    types = {}
    for row in rows:
        type = row['тип']
        types[type] = types.get(type, 0) + 1
    return types


def total_minutes(rows, kind):
    minutes = 0.0
    for row in rows:
        type = row['тип']
        if type == kind:
            minutes += float(row['минуты'])
    return round(minutes, 1)


def to_csv(counts):
    csv_str = 'тип,количество\n'
    for type, qnt in counts.items():
        csv_str += f'{type},{qnt}\n'
    return csv_str


if __name__ == "__main__":
    with open('events.csv', 'r', encoding='utf-8') as f:
        rows = read_rows(f)
    counts = count_types(rows)
    errors = total_minutes(rows, 'ошибка')
    print(rows)
    print(counts)
    print(errors)
    print(to_csv(counts))