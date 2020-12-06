f = open("input.txt", "r")

contents = f.readlines()
arr = [0 if i== '\n' else int(i.strip()) for i in contents]
print(arr)

def sum_2020(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i + 1,length):
            if arr[i] + arr[j] == 2020:
                print("{}, {}".format(arr[i], arr[j]))
                return arr[i] * arr[j]


# print(sum_2020(arr))


def sum_2020_three(arr): 
    length = len(arr)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if arr[i] + arr[j] + arr[k] == 2020:
                    print("{}, {}, {}".format(arr[i], arr[j], arr[k]))
                    return arr[i] * arr[j] * arr[k]


print(sum_2020_three(arr))
