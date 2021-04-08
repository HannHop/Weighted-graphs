f = open("floyd1.txt", "r")
line_list = f.readlines()
f.close()
print(line_list)

inf = 9999
# initialization
line_list = [line[:-1] for line in line_list]
print(line_list)
line_list = [x.split() for x in line_list]
print(line_list)
number_of_nodes = int(line_list[0][0])
number_of_edges = int(line_list[0][1])

distances = [[inf for _ in range(number_of_nodes + 1)] for _ in range(number_of_nodes + 1)]
predecessors = [[0 for _ in range(number_of_nodes + 1)] for _ in range(number_of_nodes + 1)]

for i in range(1, number_of_edges + 1):
    print(line_list[i])
    distances[int(line_list[i][0])][int(line_list[i][1])] = int(line_list[i][2])
    predecessors[int(line_list[i][0])][int(line_list[i][1])] = int(line_list[i][1])  # line 18

for i in range(1, number_of_nodes + 1):
    distances[i][i] = 0
    predecessors[i][i] = i  # pseudocode: line 18

for i in range(number_of_nodes + 1):
    print(distances[i])

for i in range(number_of_nodes + 1):
    print(predecessors[i])

for k in range(1, number_of_nodes + 1):
    for i in range(1, number_of_nodes + 1):
        if distances[i][k] is not inf:
            for j in range(1, number_of_nodes + 1):
                if (distances[i][k] + distances[k][j]) < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    predecessors[i][j] = predecessors[i][k]


def path(left, right):
    # print("Path {} -> {}".format(left, right))
    if predecessors[left][right] is 0:
        # print("Empty path")
        return []
    path_between_nodes = [left]
    while left is not right:
        # print("Current path -> {}".format(path_between_nodes))
        # print("Left -> {}".format(left))
        if left is 0:
            # print("no path")
            return []
        left = predecessors[left][right]
        path_between_nodes.append(left)
    return path_between_nodes

print("\n\n\n")

for pre in predecessors:
    print(pre)

for dys in distances:
    print(dys)

print(path(6, 2))

f = open("demofile2.txt", "a")
for i in range(1, number_of_nodes + 1):
    for j in range(1, number_of_nodes + 1):
        if i is not j:
            # pass
            if len(path(i, j)) is not 0:
                print('d[', i, ',', j, '] = ', distances[i][j], '-> path: ', path(i, j))
                

f.write("Now the file has more content!")
f.close()
