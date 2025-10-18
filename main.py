import Hanoi as hanoi
import os 

def run():
    disk_size = int(input("Enter the size of the disk: "))
    Hanabas = hanoi.Hanoi(disk_size)

    print("Game start! Move all disks from A to C:")
    while True:
        print("Type 'X' anytime to exit.")
        Hanabas.display()
        
        choice = input("Enter move (e.g. A C): ").split()
        if choice[0].upper().strip() == "X":
            break
        elif all(item in "ABC" for item in choice) and len(choice) == 2:
            os.system('cls')
            Hanabas.move_disk(from_tower=choice[0],to_tower= choice[1])
            
            if Hanabas.is_solved():
                Hanabas.display()
                print("Congratulations! You solved the Towers of Hanoi!")
                print(f"Moves: {Hanabas.moves}")
                break
        else:
            print("Invalid move!")

if __name__ == "__main__":
    run()