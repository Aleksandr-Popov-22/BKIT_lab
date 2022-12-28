from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import cowsay


def main():

    r = Rectangle("синего", 17, 17)
    c = Circle("зеленого", 17)
    s = Square("красного", 17)
    print(r)
    print(c)
    print(s)
    cowsay.cow(str(r) + '\n' + str(c) + '\n' + str(s))

if __name__ == "__main__":
    main()
