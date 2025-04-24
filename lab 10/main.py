def mat_input():
    matrix = []
    print("Enter the adjacency matrix line by line.")
    print("Press Enter twice (i.e., a blank line) after the last row to start:")

    while True:
        line = input() #read line by line
        if line.strip() == "": #empty line = end of input
            break
        row = line.strip().split() #split line by spaces into list of strings
        matrix.append(row) #add the row to the matrix

    return matrix #return raw adjacency matrix as list of strings

def weight_mat(r_matrix):
    n = len(r_matrix)
    graph = []
    for i in range(n):
        #convert each row and repl * or else convert to int
        row = [float('inf') if val in {'*'} else int(val) for val in r_matrix[i]]
        graph.append(row) #append converted row to graph
    return graph #return weighted matrix with actual numeric val

def psuedo(graph, start, end, vert):
    n = len(vert)
    ind_map = {v: i for i, v in enumerate(vert)} #map vertex names to indices
    L = [float('inf')] * n #distance labels init to *
    L[ind_map[start]] = 0 #set distance to start vertex as 0
    S = set() #set of vertices with final shortest distance
    prev = [None] * n #track previous vertex for shortest path reconstruction

    while len(S) < n:
        #find vertex not in s with minimal l value
        u = min((i for i in range(n) if i not in S), key=lambda x: L[x])
        S.add(u)  #add vertex to finalized set

        for v in range(n):
            #if vertex v is not in s and there is an edge from u to v
            if v not in S and graph[u][v] != float('inf'):
                    #edge if a shorter path is found
                if L[u] + graph[u][v] < L[v]:
                    L[v] = L[u] + graph[u][v] #change distance
                    prev[v] = u #change path

    #remake shorter path
    path = []
    current = ind_map[end]
    while current is not None:
        path.append(vert[current]) #add vertex to path
        current = prev[current] #change to prev
    path.reverse() #reverse to get correct order from start to end

    return path, L[ind_map[end]] #return path and total distance

def main():
    r_matrix = mat_input()  #raw adjacency matrix input from user
    n = len(r_matrix)
    vert = [chr(ord('a') + i) for i in range(n)] #make vertex labels starting at a
    graph = weight_mat(r_matrix) #convert raw matrix to weighted graph

    start, end = input().strip().split() #read start and end vertices
    path, distance = psuedo(graph, start, end, vert) #run psuedo
    print(', '.join(path), distance) #output shortest path and total distance

main()
