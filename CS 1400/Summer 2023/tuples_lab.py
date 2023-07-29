"""
_______________________________________________________________________________
Lab 1: prompt 1

    doctor_called = ("The doctor called today to see if I had any problems\
            getting my medication and if my condition had improved with the\
            medication since I took it.")

Given the sentence contained in the tuple called doctor_called shown in the
code above, create a function called find_longest_string_and_freq to find the
longest string in doctor_called and to compute the number of times the longest
string was used.

The expected output:

    ('medication', 2)
_______________________________________________________________________________
"""
# MY SOLUTION:
# doctor_called = ("The doctor called today to see if I had any problems\
        # getting my medication and if my condition had improved with the\
        # medication since I took it.")

# def find_longest_string_and_freq(string):
#     words = string.split()
#     longest_word = max(words, key=len)
#     longest_word_freq = words.count(longest_word)
#     output = (longest_word, longest_word_freq)
#     print(output)
#     return output

# find_longest_string_and_freq(doctor_called)

# THEIR SOLUTION:
# def find_longest_string_and_freq(data):
#   data_split = data.split(" ")
#   longest_string = max(data_split, key = len)
#   longest_string_freq = data_split.count(longest_string)
#   return(longest_string, longest_string_freq)

"""
_______________________________________________________________________________
Lab 1: Prompt 2
Using tuple packing, swap the values of the two variables shown in the code
below so that the variable dog contains the string 'dog', and the variable cat
contains the string 'cat'.

    dog = 'cat'
    cat = 'dog'

The expected output:

    Value of variable 'dog': dog
    Value of variable 'cat': cat
_______________________________________________________________________________
"""

# MY SOLUTION:
# dog = 'cat'
# cat = 'dog'
# (dog, cat) = (cat, dog)
# print(f"Value of variable 'dog': {dog}")
# print(f"Value of variable 'cat': {cat}")

# THEIR SOLUTION:
# dog = 'cat'
# cat = 'dog'

# (dog, cat) = (cat, dog)
# print("Value of variable 'dog':", dog)
# print("Value of variable 'cat':", cat)

"""
_______________________________________________________________________________
Lab 2: Prompt 1
Create a function called find_avg_grade to compute the average class grade on
the Computer Science Midterm Exam from the following tuple called
midterm_grades rounded to the nearest second decimal place.

    midterm_grades = (('Mackenzie', 89), ('Nakai', 92), ('Dante', 85),\
        ('Max', 96), ('Hadja', 98), ('Jayda', 90))

The expected output:

    91.67
_______________________________________________________________________________
"""

# MY SOLUTION:
# midterm_grades = (('Mackenzie', 89), ('Nakai', 92), ('Dante', 85),\
#     ('Max', 96), ('Hadja', 98), ('Jayda', 90))

# def find_avg_grade(x):
#     i = 0
#     total = 0
#     for _, grade in x:
#         total = total + grade
#         i += 1
#     avg = round((total / i), 2)
#     print(avg)
#     return avg

# find_avg_grade(midterm_grades)

# THEIR SOLUTION:
# def find_avg_grade(data):
#   sum_of_grades = 0
#   count = 0
#   for element in data:
#     sum_of_grades += element[1]
#     count += 1
#   return(round((sum_of_grades / count), 2))

"""
_______________________________________________________________________________
Lab 2: Prompt 2
Create a function called find_unique_tuple_freq to compute the number of times
a unique sub tuple occurs in the tuple called values.
Hint: The sub tuples (9,4) and (4,9) represent the same unique sub tuple.

    values = ((9,4), (3,6), (4,9), (3,4))

The expected output:

    3
_______________________________________________________________________________
"""

# MY SOLUTION:

# values = ((9,4), (3,6), (4,9), (3,4))

# def find_unique_tuple_freq(values):


# find_unique_tuple_freq(values)

# THEIR SOLUTION:
# values = ((9,4), (3,6), (4,9), (3,4))

# def find_unique_tuple_freq(data):
#     unique_tuple_freq = len(list(set(tuple(sorted(subtuple)) for subtuple in\
#         list(data))))
#     print(unique_tuple_freq)
#     return(unique_tuple_freq)

# find_unique_tuple_freq(values)

"""
_______________________________________________________________________________
Lab Challenge: Prompt 1
"""

rating_key = ('Food', 'Release year', 'Dish type', 'Dish weight',\
    'Dish taste', 'Dish surprise', 'Cost value', 'Rating')

sampler = (2019, 'Appetizer', 8, 4, 0, 2, 4.375)
antipasto_platter = (2022, 'Appetizer', 8, 4, 1, 2, 4.6875)
zuchinni_sticks = (2022, 'Appetizer', 4, 3, 0, 5, 3.75)
garlic_bread = (2016, 'Appetizer', 5, 6, 0, 4, 4.6875)
bruschetta_trio = (2016, 'Appetizer', 7, 8, 2, 8, 7.8125)
stuffed_portabella = (2018, 'Appetizer', 5, 4, 1, 8, 5.625)
eggplant_parm_sandwich = (2020, 'Sandwich', 8, 4, 0, 6, 5.625)
chick_n_caesar_wrap = (2018, 'Sandwich', 7, 10, 1, 9, 8.4375)
italian_deli = (2016, 'Sandwich', 10, 7, 0, 10, 8.4375)
classic_burger = (2021, 'Sandwich', 9, 7, 0, 10, 8.125)
meatball_on_a_ciabatta = (2016, 'Sandwich', 9, 6, 0, 7, 6.875)
chick_n_parmesan = (2016, 'Entree', 9, 7, 0, 6, 6.875)
eggplant_parmesan = (2018, 'Entree', 7, 4, 0, 6, 5.3125)
lasagna = (2019, 'Entree', 8, 10, 2, 9, 9.0625)
spaghetti_meatballs = (2019, 'Entree', 8, 8, 0, 10, 8.125)
tiramisu = (2016, 'Dessert', 3, 9, 2, 10, 7.5)
cannoli = (2019, 'Dessert', 3, 9, 1, 2, 4.6875)
chocolate_cake = (2019, 'Dessert', 4, 8, 0, 6, 5.625)
chocolate_almond_croissant = (2022, 'Dessert', 5, 10, 2, 4, 6.5625)

all_menu_items = (sampler, antipasto_platter, zuchinni_sticks, garlic_bread,\
        bruschetta_trio, stuffed_portabella, eggplant_parm_sandwich,\
        chick_n_caesar_wrap, italian_deli, classic_burger,\
        meatball_on_a_ciabatta, chick_n_parmesan, eggplant_parmesan, lasagna,\
        spaghetti_meatballs, tiramisu, cannoli, chocolate_cake,\
        chocolate_almond_croissant)

print(f"All Menu Items: {all_menu_items}\n")

menu_item_ratings = (sampler[6], antipasto_platter[6], zuchinni_sticks[6],\
    garlic_bread[6], bruschetta_trio[6], stuffed_portabella[6],\
    eggplant_parm_sandwich[6], chick_n_caesar_wrap[6], italian_deli[6],\
    classic_burger[6], meatball_on_a_ciabatta[6], chick_n_parmesan[6],\
    eggplant_parmesan[6], lasagna[6], spaghetti_meatballs[6], tiramisu[6],\
    cannoli[6], chocolate_cake[6], chocolate_almond_croissant[6])

print(f"Menu Item Ratings: {menu_item_ratings}\n")

average_menu_item_rating = round((sum(menu_item_ratings) / len(all_menu_items)\
    ), 4)

print(f"Average Menu Item Ratings: {average_menu_item_rating}")

print(sorted(menu_item_ratings, reverse=True))

# THEIR SOLUTION:
# all_menu_items = ((sampler, ) + (antipasto_platter, ) + (zuchinni_sticks, ) + (garlic_bread, ) + (bruschetta_trio, ) + (stuffed_portabella, ) + (eggplant_parm_sandwich, ) + (chick_n_caesar_wrap, ) + (italian_deli, ) + (classic_burger, ) + (meatball_on_a_ciabatta, ) + (chick_n_parmesan, ) + (eggplant_parmesan, ) + (lasagna, ) + (spaghetti_meatballs, ) + (tiramisu, ) + (cannoli, ) + (chocolate_cake, ) + (chocolate_almond_croissant, ))
# print("All Menu Items:", all_menu_items)

# menu_item_ratings_list = [element[6] for element in all_menu_items]
# menu_item_ratings = tuple(menu_item_ratings_list)
# print("Menu Item Ratings:", menu_item_ratings)

# average_menu_item_rating = round((sum(menu_item_ratings)/len(menu_item_ratings)), 4)
# print("Average Menu Item Rating:", average_menu_item_rating)

# THEIR SOLUTION:
# print("Menu Items Ranked In Order from Best to Worst:\n")
# for counter_value, (menu_item, menu_item_rating) in enumerate(sorted(zip(menu_items, menu_item_ratings), key = lambda element: element[1], reverse = True), 1):
#   print(counter_value, ":", menu_item, "with a rating of:", menu_item_rating, ".")