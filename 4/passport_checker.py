import re

passport_file = open("input.txt", "r")

passport_info = passport_file.read().split("\n\n")

'''
test_str = "byr:1955 hcl:#fffffd\necl:blu"
print(re.split('\n| ', test_str))

split_test_str = "foo:bar"
x,y = split_test_str.split(":")
print("x:{} y:{}".format(x, y))

# string slicing
string = "Hello World!"
print(string[6:])
'''

def valid_passports_checker(data, check_validity=False):
    passports = process_passport_input(data)
    counter = 0
    for passport in passports:
        if check_validity: 
            if contains_all_valid_fields(passport): 
                counter += 1
        elif contains_all_fields(passport):
            counter += 1
    return counter

# takes in a string of data and outputs a list of dict of passport fields 
# and their values
def process_passport_input(data):
    list_passports = []
    for passport_data in data:
        passport = {}
        fields_str_arr = re.split('\n| ', passport_data)
        for field in fields_str_arr:
            if field == '':
                break
            field_key, field_value = field.split(':')
            passport[field_key] = field_value
        list_passports.append(passport)
    return list_passports


def contains_all_fields(passport):
    valid_checks = {'byr': False, 'iyr' : False, 'eyr' : False, 'hgt' : False,
            'hcl' : False, 'ecl' : False, 'pid' : False}
    for info in passport:
        if info in valid_checks:
            valid_checks[info] = True
    return all(valid_checks.values()) 

print("Part 1: {}".format(valid_passports_checker(passport_info)))


def contains_all_valid_fields(passport):
    all_valid = True
    valid_checks = {'byr': False, 'iyr' : False, 'eyr' : False, 'hgt' : False,
            'hcl' : False, 'ecl' : False, 'pid' : False}
    for key in passport:
        if key in valid_checks:
            valid_checks[key] = not valid_checks[key] 
            all_valid = all_valid and is_valid_field(key, passport[key])
    return all(valid_checks.values()) and all_valid 

def is_valid_field(key, value):
    if key == 'byr':
        return is_year_valid(1920, 2002, value)
    elif key == 'iyr':
        return is_year_valid(2010, 2020, value)
    elif key == 'eyr':
        return is_year_valid(2020, 2030, value) 
    elif key == 'hgt':
        return is_height_valid(value)
    elif key == 'hcl':
        return is_hair_color_valid(value)
    elif key == 'ecl':
        return is_eye_color_valid(value)
    elif key == 'pid':
        return is_passport_id_valid(value)
    else:
        # might be better to throw an exception here
        return False 

def is_year_valid(least, most, actual):
    is_four_digits = re.match('^\d{4}$', actual)
    return (least <= int(actual) <= most) and bool(is_four_digits)

def is_height_valid(value):
    metric = value[-2:]
    if metric == 'cm':
        return 150 <= int(value[:-2]) <= 193
    elif metric == 'in':
        return 59 <= int(value[:-2]) <= 76
    else:
        return False

def is_hair_color_valid(value):
    return bool(re.match("#[0-9|a-f]{6}", value))

def is_eye_color_valid(value):
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return value in valid_eye_colors

def is_passport_id_valid(value):
    return bool(re.match('^\d{9}$', value))

# Part 2 add validity check

print("Part 2: {}".format(valid_passports_checker(passport_info, True)))
