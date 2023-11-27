def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 3)

def game(h):
    a, b = h
    if h >= 69: return