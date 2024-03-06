from copy import deepcopy

from src.part_1 import (
    get_all_directors,
    post_director,
    get_director,
    delete_director,
    delete_all_directors,
    get_oscars,
)

from src.part_2 import (
    get_director_movies,
    post_movie,
    patch_movie,
    get_movies_by_keyword,
)

from data import DIRECTORS_A, MOVIES_A


def test_2A():
    directors = deepcopy(DIRECTORS_A)
    movies = deepcopy(MOVIES_A)

    results = {
        1: delete_all_directors(),
        2: post_director(directors[0]),
        3: post_director(directors[1]),
        4: post_director(directors[2]),
        5: get_all_directors(directors),
        6: post_movie(directors[0], movies[0]),
        7: post_movie(directors[0], movies[1]),
        8: post_movie(directors[1], movies[2]),
        9: post_movie(directors[1], movies[3]),
        10: post_movie(directors[2], movies[4]),
        11: post_movie(directors[2], movies[5]),
        12: get_director_movies(directors[0]),
        13: get_director_movies(directors[1]),
        14: get_director_movies(directors[2]),
        15: patch_movie(movies[0], {'movie': {'title': 'Tiempos Violentos'}}),
        16: get_director(directors[0]),
    }

    return results


if __name__ == '__main__':
    results = test_2A()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
