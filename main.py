f = open("floyd1.txt", "r")
line_list = f.readlines()
f.close()
print(line_list)

line_list = [line[:-1] for line in line_list]
print(line_list)
line_list = [x.split() for x in line_list]
print(line_list)
number_of_nodes = line_list[0][0]
number_of_edges = line_list[0][1]
