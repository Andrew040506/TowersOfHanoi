
You are tasked to implement the Towers of Hanoi game in Python using stacks implemented
with linked lists. The Towers of Hanoi is a classic puzzle where the goal is to move all disks
from Tower A to Tower C, following a set of rules.
Requirements
1. You must use Stacks and must be implemented using a linked list.
2. The program must:
    o Ask the user for the number of disks (3 to 10 disks).
    o Represent each tower (A, B, C) as a stack.
    o Display the disks using * characters, where:
        § Disk of size 1 = ***
        § Disk of size 2 = *****
        § Disk of size 3 = *******
        § and so on …
            (The middle * must always align with the tower |. + 2 "*" every increase of disk size)
3. Rules of the game:
    o Only one disk may be moved at a time.
    o A disk can only be moved if it is the top disk of a tower.
    o No larger disk may be placed on top of a smaller disk.
4. User interaction:
    o The player enters moves in the format A C (move top disk from Tower A to
    Tower C).
    o The program must validate moves and display an error message for invalid
    moves.
    o Typing X exits the game immediately.
5. The game ends when all disks are successfully moved to Tower C or when the user
types x