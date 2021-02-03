def foo(b_list):
    val = int(''.join(map(str, 1 * b_list)), 2)
    return val


if __name__ == '__main__':
    l = [0, 1, 0, 1, 1, 1, 1]
    x = foo(l)

    print(x)
