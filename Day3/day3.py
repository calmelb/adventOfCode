file = open("input.txt","r")
text = file.readlines()
grid = []
max_width = 0
totals = 1

pos_change = [[1,1], [1,3], [1,5], [1,7], [2,1]]  # Down, Right ('-' index for up or left)
counts = []


for i in text:
    tmp = i.strip()
    grid.append((tmp.strip()))

# print(grid[current_coords[0]][current_coords[1]])
max_width = len(grid[0])

# def get_position():
#     print(current_coords)
#     return
for pos in pos_change:
    counts1 = 0
    current_coords = [0,0] # Row, Column
    while current_coords[0] < len(grid)-1:
        current_coords = [current_coords[0] + pos[0],
                          current_coords[1] + pos[1]]
        if current_coords[1] > max_width-1:
            tmp = current_coords[1] - max_width
            current_coords[1] = tmp
        if grid[current_coords[0]][current_coords[1]] == "#":
            counts1 = counts1 + 1
    counts.append(counts1)
    print(counts)

for i in counts:
    totals = totals * i

print(totals)