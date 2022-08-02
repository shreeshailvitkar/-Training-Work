def find_pair(list, target,n):
    flag = 0
    print(type(list),type(target))
    for i in range(0,n):
        for j in range(i,n):
            if list[i]+list[j] == target:
                print("index ", i+1, j+1)
                flag = 1
    if flag == 0:
        print("Value not Avalible")


lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	lst.append(ele) # adding the element
	
print(lst)

target = int(input("Enter Target"))

find_pair(lst,target,n)

