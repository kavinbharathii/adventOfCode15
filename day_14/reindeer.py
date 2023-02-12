

class Reindeer:
    def __init__(self, name: str, speed: int, time: int, rest: int):
        self.name = name
        self.speed = speed

        self.temprest = rest
        self.rest = rest

        self.temptime = time
        self.time = time

        self.dist = 0
        self.point = 0

    def __str__(self):
        return f"{self.name}:\n\tspeed: {self.speed}\n\ttime:  {self.time}\n\trest: {self.rest}\n\tdist: {self.dist}\n\tpoints: {self.point}"

    def move(self):
        if self.time > 0:
            self.dist += self.speed
            self.time -= 1

        else:
            self.rest -= 1

            if self.rest == 0:
                self.time = self.temptime
                self.rest = self.temprest



if __name__ == "__main__":
    comet = Reindeer("Comet", 14, 10, 127)
    dancer = Reindeer("Dancer", 16, 11, 162)

    for _ in range(1000):
        comet.move()
        dancer.move()

    print(comet)
    print(dancer)

