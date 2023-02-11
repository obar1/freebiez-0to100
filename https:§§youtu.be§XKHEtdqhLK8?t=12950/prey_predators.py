class Prey:
    def flee(self):
        pass


class Predator:
    def hunt(self):
        pass


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass
