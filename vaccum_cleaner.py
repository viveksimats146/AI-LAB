# l = input().split()
# pos = input()

# cost = 0
# pos = int(pos)

# for i in range(len(l)):
#     if i == pos:              # Position selected by user
#         if l[i] == 'D':
#             l[i] = 'C'
#             cost += 1
#         else:
#             cost += 1
#     else:
#         if l[i] == 'D':      # Other positions that are 'D'
#             cost += 1

# print("Updated list:", l)
# print("Total cost:", cost)
# Input list of rooms (C or D)
rooms = input("Enter rooms (C/D): ").split()

# Input current vacuum position
pos = int(input("Enter vacuum position: "))

cost = 0  # total cost

for i in range(len(rooms)):
    
    if i == pos:  # vacuum is in this room
        print(f"Vacuum is in room {i}")

        if rooms[i] == 'D':  # clean if dirty
            print("Room is Dirty → Cleaning...")
            rooms[i] = 'C'
            cost += 1  # cleaning cost
        else:
            print("Room is already Clean.")

        cost += 1  # checking/visiting room cost

    else:
        if rooms[i] == 'D':
            print(f"Room {i} is Dirty → Not cleaned now, cost counted")
            cost += 1   # cost of leaving dirt

print("\nFinal Room State:", rooms)
print("Total Cost:", cost)