def generatePermutation(N): 
  
    P = [] 
      
    # Generates permutation of even length N 
    for i in range(1, int(N/2)+1): 
          
        # Stores 2*i - 1 at position i in the output 
        P.append(2*i - 1) 
          
        # Stores 2*i at position N+1-i in the output 
        P.append(2*i) 
  
    return P 
      
# Driver Code 
N = 4
P = generatePermutation(N)
print(*P)
