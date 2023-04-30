class Fact:
    def __init__(self, rel, _x, _y=None):
        self.relation = rel
        self.x = _x
        self.y = _y
    
    def __str__(self):
        if(self.y != "."):
            return f"{self.x} is the {self.relation} of {self.y}!"
        else:
            return f"{self.x} is {self.relation}!"