import Stack as stack

class Hanaoi:
    def __init__(self,new_DiskSize):
        self.diskSize = new_DiskSize
        
        self.towers = {
            "A" : stack.Stack(name="A"),
            "B" : stack.Stack(name="B"),
            "C" : stack.Stack(name="C")
        }
        
        for numIter in reversed(range(1,self.diskSize+1)):
            self.towers['A'].push(numIter)
    
    def move_disk(self, from_tower, to_tower):
        
        if self.towers[from_tower] is None:
            return 
        # validate if from tower is fit to target tower
        elif self.towers[to_tower].peek() != -1:
            
            from_tower_disk = self.towers[from_tower].peek()
            to_tower_disk = self.towers[to_tower].peek()
            if from_tower_disk > to_tower_disk:
                print("Invalid move: Cannot place larger disk on smaller one!")
                return 
        
        toMove = self.towers[from_tower].pop()
        self.towers[to_tower].push(toMove)
            
    def display(self):
        # For testing 
        for k,v in self.towers.items():
            print(v.__str__())
            
    def is_solved(self):
        pass 

hanaoi = Hanaoi(3)

hanaoi.move_disk("A","B")
hanaoi.move_disk("A","C")

hanaoi.move_disk("B","C")
hanaoi.move_disk("A","B")

hanaoi.display()