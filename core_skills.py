import random

def filter_below_10(x):
    return x < 10


rand_list = []
for i in range(1,10):
    rand_list.append(random.randint(1,20))

list_comprehension_below_10 = [x for x in rand_list if x < 10]

list_filter_below_10 = list(filter(filter_below_10, rand_list))
