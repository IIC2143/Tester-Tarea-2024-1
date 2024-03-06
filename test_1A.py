from copy import deepcopy

from src.part_1 import (
    get_all_directors,
    post_director,
    get_director,
    delete_director,
    delete_all_directors,
    get_oscars,
)

from data import DIRECTORS_A


def test_1A():
    directors = deepcopy(DIRECTORS_A)

    results = {
        1: delete_all_directors(),
        2: post_director(directors[0]),
        3: post_director(directors[1]),
        4: post_director(directors[2]),
        5: get_all_directors(directors),
        6: get_director(directors[0]),
        7: get_director(directors[1]),
        8: get_director(directors[2]),
        9: get_oscars(directors),
        10: delete_director(directors, directors[0]),
        11: get_all_directors(directors),
    }

    return results


if __name__ == '__main__':
    results = test_1A()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
