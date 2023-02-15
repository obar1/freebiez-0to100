fav_col: str = input('enter fav col...')
match fav_col:
    case "black":
        print("too dark")
    case "wellow":
        print('like sunflow')
    case _:
        print('not recognized')
