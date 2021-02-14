from string import ascii_lowercase

def print_rangoli(size):
    latters = ascii_lowercase
    result = []

    for n in range(size):
        strings = '-'.join(latters[n: size])
        result.append((strings[::-1] + strings[1:]).center((4 * size) - 3, '-'))
    print('\n'.join(result[::-1]+result))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)