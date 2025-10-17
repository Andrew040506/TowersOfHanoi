import Hanaoi as hanoi
import os 

def run():
    disk_size = int(input("Enter the size of the disk: "))
    Hanabas = hanoi.Hanaoi(disk_size)

    while True:
        print("Game start! Move all disks from A to C:\nType 'X' anytime to exit.")
        Hanabas.display()
        
        choice = input("Enter move (e.g. A C): ").split()
        if choice == "X":
            break
        elif all(item in "ABC" for item in choice) and len(choice) == 2:
            
            Hanabas.move_disk(from_tower=choice[0],to_tower= choice[1])
            
            if Hanabas.is_solved():
                Hanabas.display()
                print("You won!")
                print(f"Moves: {Hanabas.moves}")
                break
            else :
                os.system('cls')
        else:
            print("Invalid move!")

if __name__ == "__main__":
    run()