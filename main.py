# This is a sample Python script.
from Fruit import Fruit


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    fruit = Fruit("Banana")

    print(fruit.fruit_name.capitalize())
    fruit.fruit_name = 'apple'
    print(fruit.fruit_name.capitalize())
    # del fruit.fruit_name
    # print(fruit.fruit_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
