class MovingObject(object):
    def __init__(self):
        self.speed = 1.0
        self.move_vector = [0.0, 0.0]

    def change_move(self, direction, k):
        k = k * self.speed
        if direction == u'UP':
            self.move_vector[1] -= k
        elif direction == u'DOWN':
            self.move_vector[1] += k
        elif direction == u'LEFT':
            self.move_vector[0] -= k
        elif direction == u'RIGHT':
            self.move_vector[0] += k

    def move(self, center):
        center.x += self.move_vector[0]
        center.y += self.move_vector[1]
