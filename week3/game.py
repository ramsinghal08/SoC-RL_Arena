import numpy as np
from capture import capture_area

class Game:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.board = np.zeros((r, c), dtype=int)
        self.people = []

    def add(self, p):
        self.people.append(p)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if 0 <= p.y + dr < self.r and 0 <= p.x + dc < self.c:
                    self.board[p.y + dr, p.x + dc] = p.num

    def update(self):
        for person in self.people:
            if person.is_dead == True:
                continue
                
            new_x = person.x + person.dx
            new_y = person.y + person.dy
            
            if new_x < 0 or new_x >= self.c or new_y < 0 or new_y >= self.r:
                continue 
                
            nxt = self.board[new_y, new_x]
            
            if nxt > 0 and nxt != person.num:
                continue 
                
            if nxt == -person.num:
                person.is_dead = True
                continue
                
            if nxt < 0 and nxt != -person.num:
                enemy_num = -nxt
                for enemy in self.people:
                    if enemy.num == enemy_num:
                        enemy.is_dead = True
                        self.board[self.board == -enemy.num] = 0
            
            curr = self.board[person.y, person.x]
            
            if curr != person.num:
                self.board[person.y, person.x] = -person.num
                
            person.x = new_x
            person.y = new_y
            
            was_out = not person.safe
            is_in = (self.board[person.y, person.x] == person.num)
            
            if was_out and is_in:
                capture_area(self.board, person.num, self.r, self.c)
                
            person.safe = is_in

    def restart(self):
        self.board = np.zeros((self.r, self.c), dtype=int)
        for person in self.people:
            person.reset_player()
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= person.y + dr < self.r and 0 <= person.x + dc < self.c:
                        self.board[person.y + dr, person.x + dc] = person.num