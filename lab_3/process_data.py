import json
from operator import concat
from unique2 import Unique
from field import field
from gen_random import gen_random
from cm_timer import cm_timer_1
from print_result import print_result

@print_result
def f1(arg):
    Data = []
    for i in field(arg, 'job-name'):
        Data.append(i)
    return Unique(Data, ignore_case=True)


@print_result
def f2(arg):
    return filter(lambda arg: arg.startswith('программист'), arg)


@print_result
def f3(arg):
    return list(map(lambda x: concat(x, ' c опытом Python'), arg))


@print_result
def f4(arg):
    return zip(arg, gen_random(len(arg),100000, 200000))

with open('data_light.json', encoding = "utf-8") as f:
    data = json.loads(f.read())

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
         
