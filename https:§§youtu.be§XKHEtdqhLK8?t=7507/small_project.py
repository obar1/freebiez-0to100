# small project to put things together

import random
import math
nums = []
for i in range(0, 52):
    nums.append(str(i))
faces = ['k', 'q', 'j', '*a*']
cards = nums + faces


def cards_test(max_it, len_cards, len_faces):
    # pick len_faces in the max
    count_is_numeric = 0
    for i in range(1, max_it):
        count_is_numeric += ("".join(cards[:len_faces]).isnumeric() == True)
    return count_is_numeric / len_cards / max_it


max_it = int(round(float('10{:E}'.format(100000))))
for i in range(1, max_it, int(max_it / 10)):
    res = 0
    try:
        res =  cards_test(i, len(cards), len(faces))
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        print("it* {:^10} * {:.21f}".format(i, res))