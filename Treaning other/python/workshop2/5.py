
class Bowler:
    default_speed = 110
    def average_speed(default_speed=110):
        return default_speed

class FastBowler(Bowler):
    ball = super
    def average_speed():
        default_speed=ball.average_speed()+(30/100)*ball.average_speed()
        return default_speed

    

class SpinnerBowler(Bowler):
    ball = super
    def average_speed():
        default_speed=ball.average_speed()-(12/100)*ball.average_speed()
        return default_speed

ball = Bowler
print(ball.average_speed())

fast = FastBowler
print(fast.average_speed())

spin = SpinnerBowler
print(spin.average_speed())