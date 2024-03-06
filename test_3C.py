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

from src.part_3 import (
    post_ranking,
    get_director_rankings,
    get_ranking_top,
    get_ranking_from_movie,
    delete_worst_director,
    get_ranking_pages,
)

from data import (
    DIRECTORS_C, MOVIES_C, RANKINGS_C,
    WRONG_MOVIES_2, WRONG_DIRECTORS_2, WRONG_RANKINGS,
)


def test_3C():
    directors = deepcopy(DIRECTORS_C)
    bad_directors = deepcopy(WRONG_DIRECTORS_2)
    movies = deepcopy(MOVIES_C)
    bad_movies = deepcopy(WRONG_MOVIES_2)
    rankings = deepcopy(RANKINGS_C)
    bad_rankings = deepcopy(WRONG_RANKINGS)

    results = {
        1: delete_all_directors(),
        2: post_director(directors[0]),
        3: post_director(directors[1]),
        4: not post_director(bad_directors[0]),
        5: not post_director(bad_directors[1]),
        6: post_director(directors[2]),
        7: not post_director(bad_directors[2]),
        8: get_all_directors(directors),
        9: get_director(directors[0]),
        10: get_director(directors[1]),
        11: not get_director(bad_directors[0]),
        12: not get_oscars(directors + bad_directors),
        13: post_movie(directors[0], movies[0]),
        14: post_movie(directors[0], movies[1]),
        15: get_oscars(directors),
        16: post_movie(directors[1], movies[2]),
        17: post_movie(directors[2], movies[3]),
        18: patch_movie(movies[3], {'movie': {'title': 'You talkin to me?'}}),
        19: get_director_movies(directors[0]),
        20: get_director_movies(directors[1]),
        21: get_director_movies(directors[2]),
        22: get_movies_by_keyword(movies, 'teenagers'),
        23: get_movies_by_keyword(movies, 'death'),
        24: not get_movies_by_keyword(movies, ''),
        25: not delete_director(directors, bad_directors[0]),
        26: not delete_director(bad_directors, bad_directors[0]),
        27: post_ranking(directors[0], rankings[0]),
        28: post_ranking(directors[0], rankings[1]),
        29: post_ranking(directors[0], rankings[2]),
        30: post_ranking(directors[1], rankings[3]),
        31: post_ranking(directors[1], rankings[4]),
        32: post_ranking(directors[1], rankings[5]),
        33: post_ranking(directors[2], rankings[6]),
        34: post_ranking(directors[2], rankings[7]),
        35: post_ranking(directors[2], rankings[8]),
        36: get_director_rankings(directors[0]),
        37: get_director_rankings(directors[1]),
        38: get_ranking_top(rankings, 3),
        39: get_ranking_from_movie(movies[0]),
        40: get_ranking_from_movie(movies[1]),
        41: delete_worst_director(directors, rankings, movies),
        42: get_director_rankings(directors[0]),
        43: not post_ranking(directors[0], bad_rankings[0]),
        44: not post_ranking(directors[0], bad_rankings[1]),
        45: not post_movie(directors[0], bad_movies[0]),
        46: not post_movie(directors[0], bad_movies[1]),
        47: not patch_movie(movies[0], {'movie': {'sinopsis': ''}}),
        48: not patch_movie(movies[0], {'movie': {'title': ''}}),
        49: get_all_directors(directors),
        50: delete_all_directors(),
    }

    return results


if __name__ == '__main__':
    results = test_3C()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
