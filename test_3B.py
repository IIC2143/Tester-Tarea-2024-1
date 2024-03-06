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

from data import DIRECTORS_B, MOVIES_B, RANKINGS_B


def test_3B():
    directors = deepcopy(DIRECTORS_B)
    movies = deepcopy(MOVIES_B)
    rankings = deepcopy(RANKINGS_B)

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
        15: post_ranking(directors[0], rankings[0]),
        16: post_ranking(directors[0], rankings[1]),
        17: post_ranking(directors[0], rankings[2]),
        18: post_ranking(directors[1], rankings[3]),
        19: post_ranking(directors[1], rankings[4]),
        20: post_ranking(directors[1], rankings[5]),
        21: post_ranking(directors[2], rankings[6]),
        22: post_ranking(directors[2], rankings[7]),
        23: post_ranking(directors[2], rankings[8]),
        24: get_director_rankings(directors[0]),
        25: get_director_rankings(directors[1]),
        26: get_ranking_from_movie(movies[0]),
        27: get_ranking_from_movie(movies[4]),
        28: delete_worst_director(directors, rankings, movies),
        29: delete_worst_director(directors, rankings, movies),
        30: delete_worst_director(directors, rankings, movies),
        31: get_all_directors(directors),
    }

    return results


if __name__ == '__main__':
    results = test_3B()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
