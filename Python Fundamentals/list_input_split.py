# Consider a list (list = []). You can perform the following commands:[cite: 3]
# 
# 1. insert i e: Insert integer e at position i.[cite: 3]
# 2. print: Print the list.[cite: 3]
# 3. remove e: Delete the first occurrence of integer e.[cite: 3]
# 4. append e: Insert integer e at the end of the list.[cite: 3]
# 5. sort: Sort the list.[cite: 3]
# 6. pop: Pop the last element from the list.[cite: 3]
# 7. reverse: Reverse the list.[cite: 3]
# 
# Initialize your list and read in the value of n followed by n lines of commands where each command will[cite: 3]
# be of the 7 types listed above. Iterate through each command in order and perform the corresponding[cite: 3]
# operation on your list.[cite: 3]
# 
# Example[cite: 3]
# N = 4[cite: 3]
# append 1[cite: 3]
# append 2[cite: 3]
# insert 1 3[cite: 3]
# print[cite: 3]
# - append 1: Append 1 to the list, arr = [1].[cite: 3]
# - append 2: Append 2 to the list, arr = [1, 2].[cite: 3]
# - insert 1 3: Insert 3 at index 1. arr = [1, 3, 2].[cite: 3]
# - print: Print the array.[cite: 3]
# Output:[cite: 3]


if __name__ == '__main__':
    N = int(input())
    
    my_list = []
    
    for i in range(N):
        command = input().split()
        
        if command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(my_list)
        elif command[0] == "remove":
            my_list.remove(int(command[1]))
        elif command[0] == "append":
            my_list.append(int(command[1]))
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "pop":
            my_list.pop()
        elif command[0] == 'reverse':
            my_list.reverse()