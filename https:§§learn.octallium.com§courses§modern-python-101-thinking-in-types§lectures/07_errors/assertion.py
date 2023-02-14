def find_friends(name: str) -> None:
    friends = ['cece', 'roko', 'niko', 'mario']

    try:
        assert name in friends
    except AssertionError:  # https://docs.python.org/3/library/exceptions.html?highlight=assertionerror#AssertionError
        print('not a friend')
        # https://docs.python.org/3/library/exceptions.html?highlight=valueerror#ValueError
        raise ValueError('check friendship')
    else:
        print('a friend')
    finally:
        print(f'for {name}')


find_friends('mario')

find_friends('sarah')
