def war(M, n):
    #init W as a copt of the user input matrix M
    W = [[M[i][j] for j in range(n)] for i in range(n)]
    
    #iterate through each node K
    for k in range(n):
        #iterate through each row i
        for i in range(n):
            #iterate through each column j
            for j in range(n):
                #update the algo to include paths through k
                W[i][j] = W[i][j] or (W[i][k] and W[k][j])
    
    return W  #return the computed transitive closure matrix

#read matrix data from user
n = int(input("Enter the number of rows/columns (EX: 3 for 3x3 or 4 for 4x4): ")) #get matrix size from user
M = []
print("Enter the matrix row by row (space-separated values):")
for _ in range(n):
    row = list(map(int, input().split()))  #read each row as a line of ints
    M.append(row)

#compute using war algo
result = war(M, n)

#print the result of transitive closure
print("Transitive closure:")
for row in result:
    print(" ".join(map(str, row)))#print each row in a readable manner