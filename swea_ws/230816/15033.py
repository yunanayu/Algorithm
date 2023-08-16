def game(s, e):
    if s == e:
        return 위치, 값?

    w1 = game(왼쪽반)
    w2 = game(오른쪽반)
    return winner(w1,w2)