import Stack as stack

class Hanaoi:
    def __init__(self,new_DiskSize=3):
        self.diskSize = new_DiskSize
        stack_A = stack.Stack(name="A")
        stack_B = stack.Stack(name="B")
        stack_C = stack.Stack(name="C")
        
        self.towers = {
            "A" : stack_A,
            "B" : stack_B,
            "C" : stack_C
        }
        
        for numIter in reversed(range(1,self.diskSize+1)):
            self.towers['A'].push(numIter)
    def move_disk(self):
        pass 
    def display(self):
        pass
hn = Hanaoi(3)