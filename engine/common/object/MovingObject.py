class MovingObject(object):
    def __init__(self):
        self.speed = 1.0
        self.move_vector = [0.0, 0.0]

    def start_move(self, direction):
        self.change_move(direction, self.speed)

    def stop_move(self, direction):
        self.change_move(direction, -self.speed)

    def change_move(self, direction, k):
        if direction == u'UP':
            self.move_vector[1] -= k
        elif direction == u'DOWN':
            self.move_vector[1] += k
        elif direction == u'LEFT':
            self.move_vector[0] -= k
        elif direction == u'RIGHT':
            self.move_vector[0] += k

    def move(self):
        self.centerx += self.move_vector[0]
        self.centery += self.move_vector[1]
