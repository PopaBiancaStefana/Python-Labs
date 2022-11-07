#cu list comprehension
def method1 (string):
    return [ch for ch in string if ch.lower() in "aeiou"]


#lambda
method2 = lambda string: [ch for ch in string if ch.lower() in "aeiou"]


#filter
def method3(string):
    return list(filter(lambda x: x.lower() in "aeiou", string))

def main():
    print(method3("Aeeobbbb"))


if __name__ == '__main__':
    main()
