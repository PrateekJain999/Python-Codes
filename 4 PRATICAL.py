L1 = [1, 3, 4, 6, 8] 
L2 = [4, 5, 6, 2, 10] 
  
# printing original lists 
print ("Original list 1 : " + str(L1)) 
print ("Original list 2 : " + str(L2)) 
  
# using list comprehension to  
# add two list  
L3 = [L1[i] + L2[i] for i in range(len(L1))]
  
# printing resultant list  
print ("Resultant list is : " + str(L3)) 
