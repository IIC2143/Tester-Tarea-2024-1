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

from data import DIRECTORS_A, MOVIES_A, RANKINGS_A


def test_3A():
    directors = deepcopy(DIRECTORS_A)
    movies = deepcopy(MOVIES_A)
    rankings = deepcopy(RANKINGS_A)

    results = {
        1: delete_all_directors(),
        2: post_director(directors[0]),
        3: post_director(directors[1]),
        4: post_director(directors[2]),
        5: post_movie(directors[0], movies[0]),
        6: post_movie(directors[0], movies[1]),
        7: post_movie(directors[1], movies[2]),
        8: post_movie(directors[1], movies[3]),
        9: post_movie(directors[2], movies[4]),
        10: post_movie(directors[2], movies[5]),
        11: post_ranking(directors[0], rankings[0]),
        12: post_ranking(directors[0], rankings[1]),
        13: post_ranking(directors[0], rankings[2]),
        14: post_ranking(directors[1], rankings[3]),
        15: post_ranking(directors[1], rankings[4]),
        16: post_ranking(directors[1], rankings[5]),
        17: post_ranking(directors[2], rankings[6]),
        18: post_ranking(directors[2], rankings[7]),
        19: post_ranking(directors[2], rankings[8]),
        20: get_director_rankings(directors[0]),
        21: get_director_rankings(directors[1]),
        22: get_director_rankings(directors[2]),
        23: get_ranking_top(rankings, 3),
        24: get_ranking_top(rankings, 1),
    }

    return results


if __name__ == '__main__':
    results = test_3A()

    for i, result in results.items():
        print(f'{i}. {result}')

    print(f'Total: {sum(results.values())}/{len(results)}')
