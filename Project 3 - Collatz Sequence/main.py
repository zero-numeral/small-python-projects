import sys


def collatz(num):
    print(num, end='')
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        print(", " + str(num), end='')


if __name__ == "__main__":
    n = input("Введите начальное число n: ")

    if not n.isdecimal() or int(n) < 1:
        print("Число должно быть больше 0")
        sys.exit(0)

    collatz(int(n))

