def safe_input(example):
    symbol = None

    try:

        symbol = input(example)

    except (EOFError, KeyboardInterrupt):

        pass

    return symbol


if __name__ == '__main__':
    print(safe_input('please input: '))
