def winner(names: list[str], scores: list[float]) -> str:
    max_score = float('-inf')
    for i in range(len(scores)):
        if scores[i] > max_score:
            win = names[i]
            max_score = scores[i]
    return win
