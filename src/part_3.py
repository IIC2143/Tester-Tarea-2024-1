from requests import get, post, delete
from copy import deepcopy
from .utils import __show, __skip_exception


BASE_URL = 'http://localhost:3000'


@__skip_exception
def post_ranking(director, ranking, *, show=False):
    url = f'{BASE_URL}/ranking/{director.id}'
    data = ranking.data()
    response = post(url, json=data)
    body = response.json()

    if show:
        __show(body, ranking)

    if ranking.is_valid(body, is_new=True):
        director.rankings.append(ranking)
        ranking.id = body['id']
        ranking.director = director
        ranking.director_id = director.id

        return True

    return False


@__skip_exception
def get_director_rankings(director, *, show=False):
    url = f'{BASE_URL}/ranking/{director.id}'
    response = get(url)
    body = response.json()

    if show:
        __show(body, director.rankings)

    if len(body) == len(director.rankings):
        content_match = all(
            ranking.is_valid(body[i])
            for i, ranking in enumerate(director.rankings)
        )

        return content_match

    return False


@__skip_exception
def get_ranking_top(rankings, quantity, *, show=False):
    url = f'{BASE_URL}/ranking/top/{quantity}'
    response = get(url)
    body = response.json()

    rankings_copy = deepcopy(rankings)

    sorted_rankings = sorted(rankings_copy, key=lambda ranking: ranking.true_score(), reverse=True)
    selected = sorted_rankings[:quantity]

    if show:
        __show(body, selected)

    if len(selected) == len(body) == quantity:
        return all(
            ranking.is_valid(body[i])
            for i, ranking in enumerate(selected)
        )

    return False


@__skip_exception
def get_ranking_from_movie(movie, *, show=False): #B
    url = f'{BASE_URL}/movies/{movie.id}/director/rankings'
    response = get(url)
    body = response.json()

    if show:
        __show(body, movie.director.rankings)

    if len(body) == len(movie.director.rankings):
        content_match = all(
            ranking.is_valid(body[i])
            for i, ranking in enumerate(movie.director.rankings)
        )

        return content_match
    
    return False


@__skip_exception
def delete_worst_director(directors, rankings, movies, *, show=False): #B
    url = f'{BASE_URL}/director/ranking/low'
    response = delete(url)
    body = response.json()

    lowest_ranking = min(rankings, key=lambda ranking: ranking.true_score())
    director = lowest_ranking.director

    if show:
        __show(body, director)

    if director.is_valid(body):
        for movie in director.movies:
            # movie.destroy()
            movies.remove(movie)

        for ranking in director.rankings:
            # ranking.destroy()
            rankings.remove(ranking)

        director.destroy()
        directors.remove(director)

        return True

    return False


@__skip_exception
def get_ranking_pages(rankings, *, show=False):
    url = f'{BASE_URL}/ranking/pages/all'
    response = get(url)
    body = response.json()

    print(body)
    

    expected = {
        'imdb': [
            ranking for ranking in rankings if ranking.page == 'imdb'
        ],
        'rotten_tomatoes': [
            ranking for ranking in rankings if ranking.page == 'rotten_tomatoes'
        ],
        'metacritic': [
            ranking for ranking in rankings if ranking.page == 'metacritic'
        ],
    }

    print(expected)

    if show:
        __show(body, expected)

    for page in expected:
        if len(body[page]) != len(expected[page]):
            return False

        for i, ranking in enumerate(expected[page]):
            if not ranking.is_valid(body[page][i]):
                return False

    return True
