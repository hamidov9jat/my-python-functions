def count_after_some_index(my_list, x, spec_index = 0):
    '''
    Includes spec_index
    '''
    if my_list:
        return my_list[spec_index:].count(x)
    else:
        return None

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'apple']

print(count_after_some_index(fruits, 'apple'))
