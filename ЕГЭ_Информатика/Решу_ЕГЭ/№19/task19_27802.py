from functools import lru_cache
def moves(h):
    return h + 1, h + 4, h * 5

@lru_cache(None)
def game(h):
    if h >= 68: return 'W'

    if any(game(m) == 'W' for m in moves(h)): return 'P1'

    if all(game(m) == 'P1'for m in moves(h)): return 'B1'

for s in range(1, 200):
    if game(s) == 'P1':
        print(s, game(s))

        # ДОДЕЛАТЬ