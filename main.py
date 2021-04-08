from collections import deque

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


f = open("demofile2.txt", "w")

for i in range(1, number_of_nodes + 1):
    for j in range(1, number_of_nodes + 1):
        if i is not j:
            if len(path(i, j)) is not 0:
                f.write("d[{},{}] = {} PATH: {}\n".format(i, j, distances[i][j], '-'.join(map(str, path(i, j)))))

f.close()


# BFS part:

def to_adjacency_list(nodes):
    adjacency_list = {}

    for node in nodes:
        [start, end, _weight] = node

        adjacency_list[start] = adjacency_list.get(start, []) + [int(end)]

    return adjacency_list


def bfs_path(adjacency_list, start, end):
    visited = [False] * (len(adjacency_list.keys()) + 1)
    queue = deque()

    visited[start] = True
    queue.append([start])

    while len(queue):
        node_path = queue.popleft()
        node = node_path[-1]

        if node == end:
            return node_path

        neighbours = adjacency_list.get(str(node))

        for neighbour in neighbours:
            if not visited[neighbour]:
                visited[neighbour] = True

                neighbour_path = list(node_path)
                neighbour_path.append(neighbour)
                queue.append(neighbour_path)  # add all prev unvisited neighbours to queue to visit them in next "round"

    return []


print(bfs_path(to_adjacency_list(line_list[1:]), 1, 4))
