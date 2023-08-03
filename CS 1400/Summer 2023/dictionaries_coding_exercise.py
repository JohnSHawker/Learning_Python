#------------------------------------------------------------------------------
# problem 1
#------------------------------------------------------------------------------

# WRITE YOUR CODE HERE
def find_key(dictionary, requested_value):
    for key in dictionary.keys():
        value = dictionary.get(key)
        if value == requested_value:
            return key

# test code below
if __name__ == "__main__":
    example_dict = {
        1 : ['red', 'blue', 'green'],
        'Josh Jung' : (9, 10),
        3 : {0 : 0},
        9000 : 'impale mat a'
        }

    key = find_key(example_dict, 'impale mat a')
    print(key)

#------------------------------------------------------------------------------
# problem 2
#------------------------------------------------------------------------------

# WRITE YOUR CODE HERE
def move_to_bottom(dictionary, requested_key):
    if requested_key in dictionary:
        last = dictionary.pop(requested_key)
        dictionary[requested_key] = last
        return dictionary
    else:
        return 'The key is not in the dictionary'

# test code below
if __name__ == "__main__":
    example_dict = {
        1 : 'one',
        2 : 'two',
        3 : 'three'
    }

    print(move_to_bottom(example_dict, 4))

#------------------------------------------------------------------------------
# problem 3
#------------------------------------------------------------------------------

# WRITE YOUR CODE HERE
def swap(dictionary):
    for key, value in dictionary.items():
        try:
            hash(key)
        except TypeError:
            return 'Cannot swap the keys and values for this dictionary'
        try:
            hash(value)
        except TypeError:
            return 'Cannot swap the keys and values for this dictionary'
    new_dict = dict([(value, key) for key, value in dictionary.items()])
    return new_dict

# test code below
if __name__ == "__main__":
    example_dict = {
        1 : 'one',
        2 : 'two',
        3 : (4, 5)
    }

    swapped = swap(example_dict)
    print(swapped)

#------------------------------------------------------------------------------
# problem 4
#------------------------------------------------------------------------------

# WRITE YOUR CODE HERE
def is_nested(dictionary):
    new_list = []
    new_dictionary = {}
    new_tuple = ()
    for key, value in dictionary.items():
        if type(key) == type(new_tuple) or type(key) == type(new_list) or type(key) == type(new_dictionary) or type(value) == type(new_tuple) or type(value) == type(new_dictionary) or type(value) == type(new_list):
            return True
    return False

# test code below
if __name__ == "__main__":
    example_dict = {
        1 : 'one',
        2 : 'two',
        3 : [4, 5]
    }

    print(is_nested(example_dict))

#------------------------------------------------------------------------------
# problem 5
#------------------------------------------------------------------------------

# WRITE YOUR CODE HERE
import json

def compare(file1, file2):
    with open(file1) as f1:
        with open(file2) as f2:
            json_f1 = json.load(f1)
            json_f2 = json.load(f2)
            if json_f1 == json_f2:
                return 'The dictionaries are equal'
            elif len(json_f1) == len(json_f2):
                return 'Dictionary 1 and dictionary 2 have the same length'
            elif len(json_f1) > len(json_f2):
                return 'Dictionary 1 is longer than dictionary 2'
            elif len(json_f1) < len(json_f2):
                return 'Dictionary 2 is longer than dictionary 1'


# test code below
if __name__ == "__main__":
    import sys

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    print(compare(file1, file2))