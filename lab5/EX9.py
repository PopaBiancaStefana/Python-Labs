
def dict_for_each_pair(pairs):

    return [{"sum": pair[0] + pair[1], "prod": pair[0]*pair[1], "pow": pair[0]**pair[1]} for pair in pairs]


if __name__ == '__main__':
   print(dict_for_each_pair(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] ))
