boarding_pass_file = open("input.txt", 'r')

boarding_passes = [i.strip() for i in boarding_pass_file.readlines()]
# print(boarding_passes)

# BFFFBBF 
# 1000110
# 70

# RRR
# 111
# 7
''' Solving process 
just replace B with 1 and F with 0 then convert to decimal
similarly, replace R with 1 and L with 0 then convert to decimal
'''

def get_max_boarding_pass_seat_id(boarding_passes):
    max_seat_id = 0
    for boarding_pass in boarding_passes:
        seat_id = get_boarding_pass_seat_id(boarding_pass)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id

def get_boarding_pass_seat_id(boarding_pass):
    row, col = get_boarding_pass_row_col(boarding_pass)
    return row * 8 + col 

'''
boarding_pass should be a string with the first 7 chars converted to
binary representing rows and last 3 chars represeting cols
use int(binary_value, 2) to convert bin -> dec
'''
def get_boarding_pass_row_col(boarding_pass):
    binary_row = boarding_pass[:7].replace("B", "1").replace("F","0")
    binary_col = boarding_pass[-3:].replace("R", "1").replace("L","0")
    row = int(binary_row, 2)
    col = int(binary_col, 2)
    return row, col

print("Part 1: {}".format(get_max_boarding_pass_seat_id(boarding_passes)))

# Part 2 (Find my seat)
'''
intuition: 
put all seat numbers in a list, sort and traverse
'''

def find_my_seat(boarding_passes):
    seat_ids = []
    for boarding_pass in boarding_passes:
        seat_ids.append(get_boarding_pass_seat_id(boarding_pass))
    seat_ids.sort()
    print(seat_ids)
    previous = seat_ids[0]
    for i in range(1,len(seat_ids)):
        if seat_ids[i] - previous > 1:
            return seat_ids[i] - 1
        previous = seat_ids[i]
print("Part 2: My seat is {}".format(find_my_seat(boarding_passes)))

