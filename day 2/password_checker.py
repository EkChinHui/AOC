f = open("input.txt", 'r')

arr = [i.strip() for i in f.readlines()]

# print(arr)

def password_check_range(arr):
    no_valid_pw = 0
    for entry in arr:
        # splits each line by spaces then the first element which is the range 
        # is split by -
        bounds = entry.split()[0].split('-')
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])
        letter = entry.split()[1][0]
        password = entry.split()[2]
        count = 0

        for ch in password:
            if ch == letter:
                count += 1
        if lower_bound <= count <= upper_bound:
            no_valid_pw += 1
    return no_valid_pw

# print(password_check_range(arr))


def password_check_position(arr):
    no_valid_pw = 0
    for entry in arr:
        # splits each line by spaces then the first element which is the range 
        # is split by -
        bounds = entry.split()[0].split('-')
        first_position = int(bounds[0]) - 1
        second_position = int(bounds[1]) - 1
        letter = entry.split()[1][0]
        password = entry.split()[2]
        
        if (password[first_position] == letter) ^ (password[second_position] == letter): 
            no_valid_pw += 1
    return no_valid_pw

print(password_check_position(arr))
