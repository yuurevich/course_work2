import pytest
from app import app
from utils import get_posts_all, get_post_by_pk


@pytest.fixture()
def correct_keys():
    return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_api_posts(correct_keys):
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200, "Статус код запроса всех постов неверный"
    assert type(response.json) == list, "Полученные данные не являются списком"
    assert set(response.json[0]) == correct_keys, "Ключи не совпадают"


def test_api_post(correct_keys):
    response = app.test_client().get('/api/posts/7')
    assert response.status_code == 200, "Статус код запроса всех постов неверный"
    assert set(response.json.keys()) == correct_keys, "Ключи не совпадают"
    assert type(response.json) == dict, "Данные поста имеют тип, отличный от словаря"


def test_load_data_is_list():
    data = get_posts_all()
    assert type(data) == list, 'Данные не являются списком'
    assert len(data) > 0, 'Список пустой'


def test_load_posts_correct_keys(correct_keys):
    data = get_posts_all()[0]
    data_keys = set(data.keys())
    assert correct_keys == data_keys, "Ключи не совпадают"


def test_load_post_is_dict():
    post = get_post_by_pk(1)
    assert type(post) == dict, 'Функция возвратила не словарь'


def test_load_post_correct_keys(correct_keys):
    data = get_post_by_pk(1)
    data_keys = set(data.keys())
    assert correct_keys == data_keys, "Ключи не совпадают"

