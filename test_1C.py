from copy import deepcopy

from src.part_1 import (
    get_all_directors,
    post_director,
    get_director,
    delete_director,
    delete_all_directors,
    get_oscars,
)

from data import DIRECTORS_C, WRONG_DIRECTORS_2


def test_1C():
    directors = deepcopy(DIRECTORS_C)
    bad_directors = deepcopy(WRONG_DIRECTORS_2)

    results = {
        1: delete_all_directors(),
        2: post_director(directors[0]),
        3: post_director(directors[1]),
        4: post_director(directors[2]),
        5: not post_director(bad_directors[0]),
        6: not post_director(bad_directors[1]),
        7: not post_director(bad_directors[2]),
        8: get_all_directors(directors),
        9: get_director(directors[0]),
        10: get_director(directors[1]),
        11: not get_director(bad_directors[0]),
        12: get_oscars(directors),
        13: delete_director(directors, directors[0]),
        14: delete_director(directors, directors[1]),
        15: not delete_director(directors, bad_directors[0]),
        16: get_all_directors(directors),
        17: not post_director(bad_directors[0]),
        18: not post_director(bad_directors[1]),
    }

    return results


if __name__ == '__main__':
    results = test_1C()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
