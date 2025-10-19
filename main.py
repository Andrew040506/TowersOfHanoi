import Hanoi as hanoi
import os 

def run():
    disk_size = int(input("Enter the size of the disk: "))
    Hanoi = hanoi.Hanoi(disk_size)

    print("Game start! Move all disks from A to C:")
    while True:
        print("Type 'X' anytime to exit.")
        Hanoi.display()
        
        choice = input("Enter move (e.g. A C): ").split()
        if choice[0].upper().strip() == "X":
            break
        elif all(item in "ABC" or "abc" for item in choice) and len(choice) == 2:
            os.system('cls')
            Hanoi.move_disk(from_tower=choice[0].upper(),to_tower= choice[1].upper())
            
            if Hanoi.is_solved():
                os.system('cls')
                Hanoi.display()
                print("Congratulations! You solved the Towers of Hanoi!")
                print(f"Moves: {Hanoi.moves}")
                break
        else:
            print("Invalid move!")

if __name__ == "__main__":
    run()