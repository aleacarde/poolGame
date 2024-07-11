class Ball:
    # number to ball types

    def __init__(self, number: int, mass: float) -> None:
        assert isinstance(number, int)
        self.__number = number
        self.__ball_type = self.__determine_ball_type()

    @property
    def number(self) -> int:
        return self.__number
    
    @property
    def ball_type(self) -> str:
        return self.__ball_type

    def __determine_ball_type(self) -> None:
        assert self.number > 0 and self.number < 15
        if self.number < 8:
            return "solid"
        elif self.number > 8:
            return "stripe"
        elif self.number == 8:
            return "8-ball"
        else:
            return "cue-ball"
