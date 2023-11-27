from functools import lru_cache
def moves(h):
    return h + 1, h + 2, h * 3
@lru_cache(None)
def game(h):
    if h >= 55: return 'W'
    if any(game(h) == 'W' for h in moves(h)): return 'P1'
    if any(game(h) == 'P1' for h in moves(h)): return 'B1'
    if any(game(h) == 'B1' for h in moves(h)): return 'P2'
    if all(game(h) == 'P1' or game(h) == 'P2' for h in moves(h)): return 'B2'

for s in range(1, 200):
    if game(s) == 'B1':
        print(s, game(s))