import numpy as np

class Game:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.board = np.zeros((r, c), dtype=int)
        self.people = []

    def add(self, p):
        self.people.append(p)
        self.board[p.y, p.x] = p.num

    def update(self):
        moves = {}
        
        for person in self.people:
            if person.is_dead == True:
                continue
            
            new_x = person.x + person.dx
            new_y = person.y + person.dy
            moves[person] = (new_x, new_y)

        counts = {}
        for m in moves.values():
            if m in counts:
                counts[m] += 1
            else:
                counts[m] = 1

        for person, nxt in list(moves.items()):
            nx = nxt[0]
            ny = nxt[1]

            if nx < 0 or nx >= self.c or ny < 0 or ny >= self.r:
                person.is_dead = True
                del moves[person]
                continue

            if self.board[ny, nx] != 0:
                person.is_dead = True
                del moves[person]
                continue

            if counts[nxt] > 1:
                person.is_dead = True
                del moves[person]
                continue

        for person in self.people:
            if not person.is_dead and person in moves:
                person.path.append((person.x, person.y))
                
                person.x = moves[person][0]
                person.y = moves[person][1]
                self.board[person.y, person.x] = person.num

    def restart(self):
        self.board = np.zeros((self.r, self.c), dtype=int)
        for person in self.people:
            person.reset_player()
            self.board[person.y, person.x] = person.num