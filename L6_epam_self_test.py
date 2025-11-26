# Lists

def process_numbers(items):
    squared_list = []
    for item in items:
        try:
            squared_list.append(float(item)**2)
        except (ValueError, TypeError):
            continue

    return sorted(squared_list)

my_list = ['10', 'hello', 25, 3.5, None, '4', "item1"]
print(process_numbers(my_list))
