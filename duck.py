
from typing import Any

rarity = {
    "_":    "Common",
    "R":    "Rare",
    "E":    "Epic",
    "L":    "Legendary",
    "X":    "Exotic",
    "C":    "Cursed",
}

part = {
    "H":    "Head",
    "B":    "Body",
    "W":    "Wing",
}

class Part():
    def __init__(self,rarity:str,id:int) -> None:
        self.rarity = rarity
        self.id = id
        self.part = None

    def __str__(self) -> str:
        if self.part == None: raise Exception("Please Use Proper Class")
        return f"{rarity[self.rarity]} {part[self.part]} #{self.id}"
    
class Head(Part):
    def __init__(self, rarity, id) -> None:
        super().__init__(rarity, id)
        self.part = "H"

class Body(Part):
    def __init__(self, rarity, id) -> None:
        super().__init__(rarity, id)
        self.part = "B"

class Wing(Part):
    def __init__(self, rarity, id) -> None:
        super().__init__(rarity, id)
        self.part = "W"

class Duck():
    def __init__(self,head,body,wing,name=None):
        self.head = head
        self.body = body
        self.wing = wing

        self.name = name

    def __str__(self) -> str:
        return f"{self.name if self.name else 'This duck'} has:\n\tHead:{self.head}\n\tBody:{self.body}\n\tWing:{self.wing}"

def main():
    H_1 = Head("_",1)
    B_1 = Body("_",1)
    W_1 = Wing("_",1)

    Protoduck = Duck(H_1,B_1,W_1,"Protoduck")
    print(Protoduck)

if __name__ == "__main__":
    main()