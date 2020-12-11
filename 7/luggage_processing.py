import re

'''
Intuition:
data structure:
{<Bag type>: {<Bag types contained in key>: <no. of bags>...}...}
'''

'''
Assuming first 2 words of each sentence is the colored bag 
subsequent contained bags are comma separated
'''

# memoized values
bags_containing_shiny_gold = set()

def process_rules_data(data):
    # remove empty strings
    bag_dictionary = dict()
    data.remove('')
    for bag in data:
        key_match = re.search(r'''(?P<key>^[a-zA-Z]+ [a-zA-Z]+)''', bag)
        key = key_match.group('key')
        values = re.findall(r'(?P<value>\d [a-zA-Z]+ [a-zA-Z]+)', bag)
        contained_bag_dict = dict()
        for value in values:
            contained_bag_color = re.search("[a-zA-Z]+ [a-zA-Z]+$", value).group()
            contained_bag_qty = re.search("\\d", value).group()
            contained_bag_dict[contained_bag_color] = int(contained_bag_qty)
        bag_dictionary[key] = contained_bag_dict
    return bag_dictionary

def count_bags_containing_shiny_gold_bag(rules):
    counter = 0
    for bag in rules:
        counter += contains_shiny_gold_recursive(bag, rules)
    # minus 1 since a shiny gold bag does not contain itself
    return counter - 1

def contains_shiny_gold_recursive(bag, rules):
    contained_bags = rules[bag]
    if bag == "shiny gold" or bag in bags_containing_shiny_gold:
        return True
    elif len(contained_bags) > 0:
        return any([contains_shiny_gold_recursive(x, rules) for x in contained_bags])
    else:
        return False

def counts_bags_contained_recursively(bag, rules):
    contained_bags = rules[bag]
    # print([contained_bags[x] * counts_bags_contained_recursively(x, rules) for x in contained_bags])
    count = 1
    for s in contained_bags:
        multiplier = contained_bags[s]
        count += counts_bags_contained_recursively(s,rules) * multiplier
    return count

def main():
    rules_data_file = open("input.txt", "r")
    list_of_rules = process_rules_data(rules_data_file.read().split('.\n'))
    print("Part 1: {}".format(count_bags_containing_shiny_gold_bag(list_of_rules)))
    # ans 12128
    print("Part 2: {}".format(counts_bags_contained_recursively("shiny gold", list_of_rules) - 1))
    example_rule = {"shiny gold":{"dark red":2}, "dark red":{"dark orange":2},
            "dark orange":{"dark yellow":2}, "dark yellow":{"dark green":2},
            "dark green":{"dark blue":2}, "dark blue":{"dark violet":2},
            "dark violet":{}}
    print("my ans {}".format(counts_bags_contained_recursively("shiny gold", example_rule) - 1))


if __name__ == "__main__":
    main()


