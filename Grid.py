class Grid:

    def __init__(self, lower, upper) -> None:
        self.upper = upper
        self.lower = lower

    def getUpper(self) -> int:
        return self.upper
    
    def getLower(self) -> int:
        return self.lower

    