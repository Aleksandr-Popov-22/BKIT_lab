def print_result(f):
    def wrapper(a):
        print(f.__name__)
        res = f(a)
        if type(res) == list:
            for i in res:
                print(i)
        elif type(res) == dict:
            for k,v in res.items():
                print(k, '=', v)
        elif type(res) == int or type(res) == str:
            print(res)
        elif type(res) == zip:
            for name, number in res:
                print(name, number)
                
        return res
    return wrapper

@print_result
def test(a):
    return a

def main():
    test(1)
    test('iu5')
    test({'a': 1, 'b': 2})
    test([1, 2])

if __name__ == '__main__':
    main()
