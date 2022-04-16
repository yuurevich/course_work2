from utils import get_posts_all, get_post_by_pk


def test_load_data_is_list():
    data = get_posts_all()
    assert type(data) == list, 'Данные не являются списком'
    assert len(data) > 0, 'Список пустой'


def test_load_posts_correct_keys():
    correct_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    data = get_posts_all()[0]
    data_keys = set(data.keys())
    assert correct_keys == data_keys, "Ключи не совпадают"


def test_load_post_is_dict():
    post = get_post_by_pk(1)
    assert type(post) == dict, 'Функция возвратила не словарь'


def test_load_post_correct_keys():
    correct_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    data = get_post_by_pk(1)
    data_keys = set(data.keys())
    assert correct_keys == data_keys, "Ключи не совпадают"

