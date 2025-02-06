list1 = [('Hi', 14), ('there', 16), ('Jane', 28)]

list2 = [('Jane', 12), ('Hi', 4), ('there', 21)]


def group_summation(lists):
    s_dict = {}

    for l in lists:
        for elem in l:
            if elem[0] not in s_dict:
                s_dict[elem[0]] = elem[1]
            else:
                s_dict[elem[0]] += elem[1]

    return [(k, v) for k, v in s_dict.items()]


print(group_summation([list1, list2]))
