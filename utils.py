import json


def get_posts_all():
    """Возвращает список всех постов"""
    with open('data/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_comments_all():
    """Возвращает список всех комментариев"""
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_pk_bookmark():
    """Возвращает номера постов добавленных в закладки"""
    with open('data/bookmarks.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def uploads_posts(posts):
    """Добавляет номер поста в закладки"""
    with open('data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)


def get_posts_by_user(user_name):
    """Возвращает список постов по имени"""
    result = [post for post in get_posts_all() if post['poster_name'].lower() == user_name.lower()]
    return result


def get_post_by_pk(pk):
    """Возвращает пост по номеру"""
    result = [post for post in get_posts_all() if post['pk'] == int(pk)]
    return result[0]


def get_comments_by_post_id(post_id):
    """Возвращает список комментариев по номеру поста"""
    result = [comment for comment in get_comments_all() if int(post_id) == comment['post_id']]
    return result


def search_for_posts(query):
    """Возвращает список постов, в контенте которого есть искомое слово"""
    result = [post for post in get_posts_all() if query.lower() in post['content'].lower()]
    return result[:10]


def get_posts_bookmark():
    """Возвращает список постов находящихся в закладках"""
    result = []
    post_ids = get_pk_bookmark()
    posts = get_posts_all()
    for id in post_ids:
        for post in posts:
            if post['pk'] == id:
                result.append(post)
    return result


def add_bookmarks(pk):
    """Добавляет номер поста в закладки"""
    pk_list = get_pk_bookmark()
    pk_list.append(int(pk))
    pk_set = set(pk_list)
    posts = list(pk_set)
    uploads_posts(posts)


def delete_bookmarks(pk):
    """Удаляет номер поста из закладок"""
    pk_list = get_pk_bookmark()
    pk_list.remove(int(pk))
    uploads_posts(pk_list)


