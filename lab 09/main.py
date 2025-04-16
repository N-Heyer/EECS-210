'''
Name:Nick Heyer 
KUID:3142337
LAB Session:Thursday 4:30pm
LAB Assignment: 09
Description: This program takes in an adjacency matrix and determines if the
graph is connnected or not connected
Collaborators: NONE
'''
# search for all reachable nodes
def mat(matrix, visited, node):
    visited[node] = True #mark node as visited
    for neighbor, connected in enumerate(matrix[node]):#checks all possible close nodes around
        if connected == 1 and not visited[neighbor]:#if edge and other close node not visited
            mat(matrix, visited, neighbor)#recurse to visit other close node

#check if graph is connected
def is_connected(matrix):
    n = len(matrix) #num of nodes in graph
    visited = [False] * n #init all false, track nodes
    mat(matrix, visited, 0) #start from first node
    return all(visited) #if all nodes are visited it is connected

#read matrix from user
matrix = [] #store matrix
print("Enter the adjacency matrix line by line (empty line to finish):")
while True:
    line = input().strip()
    if line == "":
        break #stop when empty line is entered
    row = list(map(int, line.split())) #convert input into a list of ints
    matrix.append(row) #add row to matrix

#check if graph is connected and print result
if is_connected(matrix):
    print("connected")
else:
    print("not connected")
