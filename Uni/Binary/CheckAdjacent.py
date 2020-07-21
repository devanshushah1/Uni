def CheckAdjacent(n1, n2):
    value = False
    my_dict = {}
    for i in range(n1, n2):
        value = False
        l = list(bin(i))
        for k in range(2, len(l) - 1):
            if l[k] == '1' and l[k + 1] == '1':
                value = True

        my_dict[i] = value
    return my_dict
