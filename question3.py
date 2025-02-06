def flatten_tuple(t):
    flattened = tuple()

    for elem in t:

        if not isinstance(elem, tuple):
            flattened += (t,)
            break
        else:
            flattened += flatten_tuple(elem)

    return flattened


t = ((35, 46), ((67, 70), (8, 11), (10, 111)), ((21, 12), (3, 4)))

print(flatten_tuple(t))
