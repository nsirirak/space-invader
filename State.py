
class State:
    def __init__(self,screen, x, y):
        self.screen = screen
        self.screen_H, self.screen_V = screen.get_size()
        self.X = x
        self.Y = y
        self.direction = 1
        self.state = "live"

    def getPoint(self):
        return self.X, self.Y

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def setDirection(self, direction):
        self.direction = direction

