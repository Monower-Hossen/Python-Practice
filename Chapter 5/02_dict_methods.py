my_dict = {
    'a': 1,
    'b': 2
}
#get()
print(my_dict.get('b'))  # Output: 2
print(my_dict.get('c', 'Not found'))  # Output: Not found

#keys()
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])

#values()
print(my_dict.values())  # Output: dict_values([1, 2])

#items()
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2)])

#update()
my_dict = {'a': 1}
my_dict.update({'b': 2, 'c': 3})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}

#pop()
my_dict = {'a': 1, 'b': 2}
value = my_dict.pop('a')
print(value)  # Output: 1
print(my_dict)  # Output: {'b': 2}

#popitem()
my_dict = {'a': 1, 'b': 2}
item = my_dict.popitem()
print(item)  # Output: ('b', 2) (or ('a', 1), depending on insertion order)
print(my_dict)  # Output: {'a': 1} (or empty if 'b' was the last item)

#clear()
my_dict = {'a': 1, 'b': 2}
my_dict.clear()
print(my_dict)  # Output: {}

#setdefault()
my_dict = {'a': 1}
value = my_dict.setdefault('b', 2)
print(value)  # Output: 2
print(my_dict)  # Output: {'a': 1, 'b': 2}

#copy()
my_dict = {'a': 1, 'b': 2}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2}

