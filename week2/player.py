class Player:
    def __init__(self, start_x, start_y, dir_x, dir_y, color, num):
        self.start_x = start_x
        self.start_y = start_y
        self.start_dx = dir_x
        self.start_dy = dir_y
        
        self.x = start_x
        self.y = start_y
        self.dx = dir_x
        self.dy = dir_y
        
        self.color = color
        self.num = num
        self.path = []
        self.is_dead = False

    def reset_player(self):
        self.x = self.start_x
        self.y = self.start_y
        self.dx = self.start_dx
        self.dy = self.start_dy
        self.path = []
        self.is_dead = False