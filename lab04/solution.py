def winner(names: list[str], scores: list[float]) -> str:
    max_score = float('-inf')
    for i in range(len(scores)):
        if scores[i] > max_score:
            win = names[i]
            max_score = scores[i]
    return win

def average(scores: list[float]) -> float:
    if scores != []:
        avr = sum(scores) / len(scores)
        return f'{avr:.2f}'
    return 0.0

def ranking(names: list[str], scores: list[float]) -> list[str]:
    data = [(names[i], scores[i]) for i in range(len(names))]
    data.sort(reverse = True, key = lambda elem: elem[1])
    sorted_names = [el[0] for el in data]
    return sorted_names

if __name__ == "__main__":
    names =  ["Аня", "Боря", "Вика"]
    scores = [7.0,   9.0,    9.0]
    print(winner(names, scores), average(scores), ranking(names, scores))
