from gen_random import gen_random
class Unique(object):
    def __init__(self, items, **kwargs):
        self.r = []
    
        for key,value in kwargs.items():
            if key=='ignore_case' and value==True:
                try:
                    items = [i.lower() for i in items]
                finally:
                    break

        for i in items:
            if i not in self.r:
                self.r.append(i)


    def __next__(self):
        try:
            x = self.r[self.begin]
            self.begin += 1
            return x
        except:
            raise StopIteration

    def __iter__(self):
        self.begin = 0
        return self
        
if __name__ == '__main__':
    a = [1,4,87,3,5,7,2,4,6,4,3,6,3,4,2]
    b = ['A', 'a', 'B', 'b']
    c = gen_random(10, 1, 3)
    for i in Unique(c):
        print(i)
