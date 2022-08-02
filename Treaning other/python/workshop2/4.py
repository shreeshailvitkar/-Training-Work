class Cricket:
    country = "india"
    def __init__(self,type,run,wickets):
        self.type = type
        self.run = run
        self.wicket = wickets
        #self.speed = max_speed




class Blower(Cricket):
    pass
class Batsman(Cricket):
    pass
 
blow = Blower("Test",200,2)
print(blow.country)

bat = Batsman("OneDay",250,5)
print(blow.country)