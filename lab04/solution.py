def winner(names: list[str], scores: list[float]) -> str:
    max_score = float('-inf')
    for i in range(len(scores)):
        if scores[i] > max_score:
            win = names[i]
            max_score = scores[i]
    return win

def average(scores: list[float]) -> float:
    if scores != []:
        avg = sum(scores) / len(scores)
        return round(avg, 2)
    return 0.0

def ranking(names: list[str], scores: list[float]) -> list[str]:
    data = [(names[i], scores[i]) for i in range(len(names))]
    data.sort(reverse = True, key = lambda elem: elem[1])
    sorted_names = [el[0] for el in data]
    return sorted_names

def above_average(names: list[str], scores: list[float]) -> list[str]:
    avg = sum(scores) / len(scores)
    f_names = [names[i] for i in range(len(names)) if scores[i] > avg]
    return f_names

if __name__ == "__main__":
    names =  ["Аня", "Боря", "Вика"]
    scores = [7.0,   9.0,    9.0]
    print(winner(names, scores), average(scores), ranking(names, scores), above_average(names, scores))
