input_file = open("input.txt", "r")

slope = input_file.readlines()

def tree_checker(slope, right, down):
    arr = slope_to_2d_array(slope)
    counter = 0
    for i in range(len(arr)):
        j = i * right
        if i * down >= len(arr):
            return counter 
        if j >= len(arr[i]):
            j = j % len(arr[i * down]) 
        if arr[i * down][j] == '#':
            counter += 1
    return counter

def slope_to_2d_array(slope):
    arr = []

    for i in range(len(slope)):
        arr.append([])
        for char in slope[i].strip():
            arr[i].append(char)

    return arr

print("Part 1: {}".format(tree_checker(slope, 3, 1)))

def multiply_routes(slope, dic):
    counter = 1;
    for trees in dic:
        right = trees[0]
        down = trees[1]
        counter *= tree_checker(slope, right, down)
    return counter
       

dic = [[1,1], [3,1], [5,1], [7,1], [1,2]]
print("Part 2: {}".format(multiply_routes(slope, dic)))




