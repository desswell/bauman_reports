from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from fabulous import text

def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)
    print(text.Text("Useless", color='#ffffee', shadow=True, skew=4))
if __name__ == "__main__":
    main()