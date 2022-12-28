def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор
    if len(args) == 1:
        for i in items:
            if i.get(*args) == None:
                continue
            yield i.get(*args)
    else:
        r = {}
        for i in range(len(items)):
            for key in items[i]:
                if items[i][key] == None:
                        continue
                if key in args:
                    r.update({key:items[i][key]})
            if r == {}:
                continue
            yield r

def main():
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'reen'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    for i in field(goods,'title', 'price'):
        print(i)
if __name__ == "__main__":
    main()
    
