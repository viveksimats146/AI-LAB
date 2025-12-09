b = [' '] * 9
p = 'X'

def show():
    print(b[0], b[1], b[2])
    print(b[3], b[4], b[5])
    print(b[6], b[7], b[8])

def win():
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    for x, y, z in w:
        if b[x] == b[y] == b[z] != " ":
            return True
    return False

for _ in range(9):
    show()
    i = int(input("Enter position (0-8): "))

    if i < 0 or i > 8:
        print("Invalid index! Try again.")
        continue

    if b[i] != ' ':
        print("Spot already taken! Try again.")
        continue

    b[i] = p

    if win():
        show()
        print(p, "wins!")
        break

    # switch player
    p = 'O' if p == 'X' else 'X'
