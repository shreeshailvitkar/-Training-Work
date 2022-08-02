class Cricket:
    def __init__(self,type,run,wickets):
        self.type = type
        self.run = run
        self.wicket = wickets

cri = Cricket("oneDay",250,5)
print(cri.type,cri.run,cri.wicket)

class Blower(Cricket):
    pass
blower = Blower("Test", 200, 2)
print("Type:", blower.type, "Run:", blower.run, "Wickets:", blower.wicket)