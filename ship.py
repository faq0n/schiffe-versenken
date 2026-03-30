class Ship:
    """Class that provides a Ship instance that can be checked on hits and win"""

    def __init__(self, startXY, endXY, lives):
        """Object starts in game at e.g. posX and goes to posY; stored in array [ A1,C1 ]"""
        self.startPos = startXY.split()
        self.endPos = endXY.split()
        self.lives = lives

    def get_sunken(lives):
        if lives < 1:
            print("Hit! Enemy Ship destroyed!")
            return True
        elif lives >= 1:
            print("Target found! Radar reports hit")
            return False
        else:
            "Already destroyed"

    def set_coordinates(startX: str, startY: int, endX: str, endY: int):
        try:
            if (startX and endX in "ABCDEFGHIJ") and (
                startY and endY in range(1, 10 + 1)
            ):
                startPos = [startX, startY]
                endPos = [endX, endY]
        except:
            print("Wrong Value \n Pausing Game!!!")

    def get_hit(self):
        return self.startPos, self.endPos
