from flask import Blueprint, render_template, request
from utils import get_posts_all, get_posts_bookmark, get_post_by_pk, get_comments_by_post_id, get_posts_by_user, \
    search_for_posts


main_blueprint = Blueprint('main_blueprint', __name__, url_prefix='/')


@main_blueprint.route('/')
def posts():
    posts = get_posts_all()
    count_bookmarks = len(get_posts_bookmark())
    return render_template('index.html', posts=posts, count_bookmarks=count_bookmarks)


@main_blueprint.route('post/<pk>')
def post(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments, count_comments=len(comments))


@main_blueprint.route('/profile/<username>')
def profile(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)


@main_blueprint.route('/search/')
def search_page():
    s = request.args['s']
    posts = search_for_posts(s)
    return render_template('search.html', posts=posts, count=len(posts), s=s)
