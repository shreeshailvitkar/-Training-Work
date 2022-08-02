def return_prime(lst,n):
    flag = 2
    lst1 = []
    for i in range(0,n):
        for j in range(2,lst[i]):
            print("from to ",j)
            if lst[i]%j==0:
                flag = 1
            else:
                flag = 0
           
    print(lst1)
    
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	lst.append(ele) # adding the element
	
print(lst)



return_prime(lst,n)
