from flask import Blueprint, render_template, redirect
from utils import get_posts_bookmark, add_bookmarks, delete_bookmarks


bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, url_prefix='/bookmarks')


@bookmarks_blueprint.route('/')
def bookmarks():
    posts = get_posts_bookmark()
    return render_template('bookmarks.html', posts=posts, )


@bookmarks_blueprint.route('/add/<pk>')
def add_post(pk):
    add_bookmarks(pk)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/delete/<pk>')
def delete_post(pk):
    delete_bookmarks(pk)
    return redirect("/bookmarks", code=302)

