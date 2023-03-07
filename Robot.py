class Robot:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def updateX(self, x) -> None:
        self.x = x

    def updateY(self, y) -> None:
        self.y = y

    def getX(self) -> int:
        return self.x

    def getY(self) -> int:
        return self.y

