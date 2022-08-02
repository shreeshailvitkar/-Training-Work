
class Bowler:
    def __init__(self, speed):
        self.speed = speed

class PartTimeBowler(Bowler):
    pass

parttimebowler = PartTimeBowler(200)
print(isinstance(parttimebowler,Bowler))

  