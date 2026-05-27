def set_intersection_count(sets):

    common_elements = set.intersection(*sets)

    return len(common_elements)

sets1 = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
print(set_intersection_count(sets1))

sets2 = [{'a', 'b'}, {'b', 'c'}, {'c', 'd'}]
print(set_intersection_count(sets2))