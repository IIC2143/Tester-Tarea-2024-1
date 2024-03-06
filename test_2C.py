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

from data import DIRECTORS_C, MOVIES_C, WRONG_MOVIES_2, WRONG_DIRECTORS_2


def test_2C():
    directors = deepcopy(DIRECTORS_C)
    bad_directors = deepcopy(WRONG_DIRECTORS_2)
    movies = deepcopy(MOVIES_C)
    bad_movies = deepcopy(WRONG_MOVIES_2)

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
        15: get_movies_by_keyword(movies, 'US'),
        16: get_movies_by_keyword(movies, 'death'),
        17: delete_director(directors, directors[0]),
        18: not post_movie(directors[1], bad_movies[0]),
        19: patch_movie(movies[4], {'movie': {'title': 'Talk to her'}}),
        20: not patch_movie(movies[0], {'movie': {'title': ''}}),
        21: not get_all_directors(bad_directors),
        22: not get_director(bad_directors[0]),
        23: not post_movie(bad_directors[0], bad_movies[0]),
        24: not get_director_movies(bad_directors[0]),
        25: not get_movies_by_keyword(bad_movies, ''),
        26: not delete_director(bad_directors, bad_directors[0]),
        27: not patch_movie(bad_movies[0], {'movie': {'title': ''}}),
        28: not patch_movie(bad_movies[0], {'movie': {'title': 'Into the wild'}}),
        29: delete_director(directors, directors[1]),
        30: get_all_directors(directors),
    }

    return results


if __name__ == '__main__':
    results = test_2C()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
