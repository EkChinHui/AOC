'''
Intuition: use a hashset to store unique values of a-z
then get the size of the set
'''
def process_forms_input(forms):
    processed_forms = []
    list_of_group_data = forms.split("\n\n")
    for group in list_of_group_data:
        processed_forms.append(group.split('\n'))
    # removes last empty string element in the last group
    processed_forms[-1].remove('')
    return processed_forms


def unique_answers_in_group(group):
    unique_answer_set = set() 
    for person in group:
        unique_answer_set.update(person)
    return len(unique_answer_set)

def sum_of_unique_answers(data):
    counter = 0
    for group in data:
        counter += unique_answers_in_group(group) 
    return counter

def common_answers_in_group(group):
    common_answer_set = group[0]
    for person in group:
        common_answer_set = [value for value in person if value in common_answer_set]
    return len(common_answer_set)

def sum_of_common_answers(data):
    counter = 0
    for group in data:
        counter += common_answers_in_group(group) 
    return counter

def main():
    forms_data = open("input.txt", "r")
    groups_of_forms = process_forms_input(forms_data.read())
    part_one = sum_of_unique_answers(groups_of_forms)
    print("Part 1: {}".format(part_one))

    part_two = sum_of_common_answers(groups_of_forms)
    print("Part 2: {}".format(part_two))

'''
Part 2 Intuition:
Use sets as well and use the intersection between sets
'''


if __name__ == "__main__":
    main()
