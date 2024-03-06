from copy import deepcopy

from src.part_1 import (
    get_all_directors,
    post_director,
    get_director,
    delete_director,
    delete_all_directors,
    get_oscars,
)

from data import DIRECTORS_B, WRONG_DIRECTORS


def test_1B():
    directors = deepcopy(DIRECTORS_B)
    bad_directors = deepcopy(WRONG_DIRECTORS)

    results = {
        1: delete_all_directors(),
        2: post_director(directors[0]),
        3: post_director(directors[1]),
        4: not post_director(bad_directors[0]),
        5: post_director(directors[2]),
        6: not post_director(bad_directors[1]),
        7: get_all_directors(directors),
        8: get_director(directors[0]),
        9: get_director(directors[1]),
        10: get_director(directors[2]),
        11: get_oscars(directors),
        12: delete_director(directors, directors[0]),
        13: get_all_directors(directors),
    }

    return results


if __name__ == '__main__':
    results = test_1B()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
