class Cricket:
    def __init__(self,type,run,wickets):
        self.type = type
        self.run = run
        self.wicket = wickets
        #self.speed = max_speed

    def max_speed(self, speed=25):
        #self.max_speed = speed
        return speed



class Blower(Cricket):
    #OVerride
    def max_speed(self, speed=50):
        return speed

blow = Blower("Oneday",255,1)
print(blow.max_speed())
