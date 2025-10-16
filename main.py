import Hanaoi as hanoi

def main():
    disk_size = int(input("Enter the size of the disk: "))
    Hanabas = hanoi.Hanaoi(disk_size)

    while True:
        print("Game start! Move all disks from A to C:\nType 'X' anytime to exit.")
        #print("(print disk and poles)")
        Hanabas.display()
        choice = input("Enter move (e.g. A C): ")
        choice = choice.split()
        #print(choice)
        if choice == "X":
            break
        elif all(item in "ABC" for item in choice) and len(choice) == 2:
            Hanabas.move_disk(choice[0], choice[1])
            #print(choice[0], "->", choice[1])
        else:
            print("Invalid move!")

if __name__ == "__main__":
    main()