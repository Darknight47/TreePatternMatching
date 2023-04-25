class Fact:
    def __init__(self, rel, _x, _y):
        self.relation = rel,
        self.x = _x
        self.y = _y
    
    def __str__(self):
        return f"{self.x} is {self.relation} for the {self.y}."