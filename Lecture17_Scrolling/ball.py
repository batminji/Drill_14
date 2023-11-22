from pico2d import *
import game_world
import game_framework
import random
import server


class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()


    def draw(self):
        self.sx, self.sy = self.x - self.bg.window_left, self.y - self.bg.window_bottom
        self.image.draw(self.sx, self.sy)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                other.ball = self # 소년이 볼을 소유하도록.
                pass
            case 'zombie:ball':
                other.ball = self

    def set_background(self, bg):
        # fill here
        self.bg = bg
        pass