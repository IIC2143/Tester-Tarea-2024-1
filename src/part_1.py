from requests import get, post, delete
from .models import Director
from .utils import __show, __skip_exception


BASE_URL = 'http://localhost:3000'


@__skip_exception
def get_all_directors(directors: list[Director], *, show=False):
    url = f'{BASE_URL}/directors'
    response = get(url)
    body = response.json()

    if show:
        __show(body, directors)

    if len(body) == len(directors):
        content_match = all(
            director.is_valid(body[i])
            for i, director in enumerate(directors)
        )

        return content_match

    return False


@__skip_exception
def post_director(director: Director, *, show=False):
    url = f'{BASE_URL}/directors'
    data = director.data()
    response = post(url, json=data)
    body = response.json()

    if show:
        __show(body, director)

    if response.status_code >= 400:
        return False

    if director.is_valid(body, is_new=True):
        director.id = body['id']

        return True

    return False


@__skip_exception
def get_director(director: Director, *, show=False):
    url = f'{BASE_URL}/director/{director.id}'
    response = get(url)
    body = response.json()

    if show:
        __show(body, director)

    return director.is_valid(body)


@__skip_exception
def delete_director(directors: list[Director], director: Director, *, show=False):
    url = f'{BASE_URL}/director/{director.id}'
    response = delete(url)
    body = response.json()

    if show:
        __show(body, {})

    if body == {}:
        directors.remove(director)

        return True

    return False


@__skip_exception
def delete_all_directors(*, show=False):
    url = f'{BASE_URL}/directors'
    response = delete(url)
    body = response.json()

    if show:
        __show(body, [])

    return body == []


@__skip_exception
def get_oscars(directors: list[Director], *, show=False):
    url = f'{BASE_URL}/directors/oscars'
    response = get(url)
    body = response.json()

    oscars = list(filter(lambda x: x.has_oscars, directors))

    if show:
        __show(body, oscars)

    if len(body) == len(oscars):
        content_match = all(
            oscars[i].is_valid(body[i])
            for i in range(len(oscars))
        )

        return content_match

    return False
