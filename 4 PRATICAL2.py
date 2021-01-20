def Cloning(L1): 
    L2 = [] 
    L2.extend(L1) 
    return L2
  
# Driver Code 
L1 = [4, 8, 2, 10, 15, 18] 
L2 = Cloning(L1) 
print("Original List:", L1) 
print("After Cloning:", L2) 
