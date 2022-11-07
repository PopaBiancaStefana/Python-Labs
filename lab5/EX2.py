def sum_1(*args, **keywords):

    s = 0
    for keyword in keywords:
        s += int(keywords[keyword])
    return s
    

anonymous_function = lambda *args, **keywords: sum([val for val in keywords.values()])


def main():
    
        print(sum_1(1, b=2, c=3))
        print(anonymous_function( 5, a=1, b=2, c=3))

if __name__ == '__main__':
    main()
