from requests import get, post, patch
from .utils import __show, __skip_exception
from copy import deepcopy


BASE_URL = 'http://localhost:3000'


@__skip_exception
def get_director_movies(director, *, show=False):
    url = f'{BASE_URL}/director/{director.id}/movies'
    response = get(url)
    body = response.json()

    if show:
        __show(body, director.movies)

    if len(body) == len(director.movies):
        content_match = all(
            movie.is_valid(body[i])
            for i, movie in enumerate(director.movies)
        )

        return content_match

    return False


@__skip_exception
def post_movie(director, movie, *, show=False):
    url = f'{BASE_URL}/director/{director.id}/movies'
    data = movie.data()
    response = post(url, json=data)
    body = response.json()

    if show:
        __show(body, movie)

    if response.status_code >= 400:
        return False

    if movie.is_valid(body, is_new=True):
        director.movies.append(movie)
        movie.id = body['id']
        movie.director = director
        movie.director_id = director.id

        return True

    return False


@__skip_exception
def patch_movie(movie, new_movie_data, *, show=False):
    url = f'{BASE_URL}/director/{movie.director.id}/movies/{movie.id}'
    data = new_movie_data
    response = patch(url, json=data)
    body = response.json()

    if response.status_code >= 400:
        return False

    movie_copy = deepcopy(movie)
    movie_copy.update(new_movie_data)

    if show:
        __show(body, movie_copy)

    if movie_copy.is_valid(body):
        movie.update(new_movie_data)

        return True

    return False


@__skip_exception
def get_movies_by_keyword(movies, keyword, *, show=False):
    url = f'{BASE_URL}/movies/sinopsis/{keyword}'
    response = get(url)
    body = response.json()

    filtered_movies = [
        movie
        for movie in movies
        if keyword in movie.sinopsis
    ]

    if show:
        __show(body, filtered_movies)

    if len(body) == len(filtered_movies):
        content_match = all(
            movie.is_valid(body[i])
            for i, movie in enumerate(filtered_movies)
        )

        return content_match

    return False
