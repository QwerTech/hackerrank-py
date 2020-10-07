if __name__ == '__main__':
    scores, students = [], []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name, score])

    scores = sorted(scores, reverse=True)
    first = scores.pop()
    while scores:
        second = scores.pop()
        if second != first:
            break

    [print(st) for st in sorted([st[0] for st in students if st[1] == second])]
