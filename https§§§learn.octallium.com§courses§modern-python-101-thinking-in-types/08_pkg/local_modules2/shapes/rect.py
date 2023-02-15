class Rect:
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def __str__(self) -> str:
        return f"{type(self)} with {self.base} {self.height}"
