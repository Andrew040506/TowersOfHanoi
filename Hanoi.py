import Stack as stack

class Hanoi:
    def __init__(self,new_DiskSize):
        self.diskSize = new_DiskSize
        
        self.moves = 0
        
        self.towers = {
            "A" : stack.Stack(name="A"),
            "B" : stack.Stack(name="B"),
            "C" : stack.Stack(name="C")
        }

        for numIter in reversed(range(1,self.diskSize+1)):
            self.towers['A'].push(numIter)

    def move_disk(self, from_tower, to_tower):

        if self.towers[from_tower].peek() == -1:
            print("")
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
        self.moves +=1

    def display(self):
        max_size = self.diskSize
        max_width = 3 + 2 * (max_size - 1) + 4
        height = max_size
        towers = self.towers

        tower_data = {k: v.get_items() for k, v in towers.items()}

        print("\n" + "=" * (max_width * 3 + 12)+"\n")
        for level in range(height - 1, -1, -1):
            for name in ["A", "B", "C"]:
                disks = tower_data[name]
                if level < len(disks):
                    size = disks[level]
                    width = 3 + 2 * (size - 1)  
                    stars = "*" * width
                    print(stars.center(max_width), end="   ")
                else:
                    print("|".center(max_width), end="   ")
            print()
        print("-" * (max_width * 3 + 12))
        print("A".center(max_width), "B".center(max_width+5), "C".center(max_width-2)+"\n")
        return
    def is_solved(self):
        return self.towers["B"].is_empty() & self.towers["A"].is_empty()