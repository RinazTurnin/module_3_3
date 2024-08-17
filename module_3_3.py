def print_params(a = 1, b = 'строка', c = True):
  print(a, b, c)

print_params()
print_params(2, 'строка', False)
print_params('Rinaz', 'Done')
print_params(50)
print_params(b = 25)
print_params(c = [1,2,3])

value_list = [5, False, 'привет']
value_dict = {'a': 10, 'b': bool, 'c': 'привет'}
print_params(*value_list)
print_params(**value_dict)

values_list_2 = [1998, 'Rinaz' ]
print_params(*values_list_2, 26)