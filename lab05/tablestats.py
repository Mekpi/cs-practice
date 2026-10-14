def read_rows(lines):
    lines = lines.copy()
    header = lines[0].strip().split(',')
    lines.pop(0)
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
    counts = sorted(counts.items(), key=lambda el: el[0])
    for type, qnt in counts:
        csv_str += f'{type},{qnt}\n'
    return csv_str


if __name__ == "__main__":
    with open('events.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    rows = read_rows(lines)
    counts = count_types(rows)
    errors = total_minutes(rows, 'ошибка')
    print(rows)
    print(counts)
    print(errors)
    print(to_csv(counts))