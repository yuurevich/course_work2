from flask import Blueprint, jsonify
from utils import get_posts_all, get_post_by_pk

api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')


@api_blueprint.route('/posts')
def api_posts():
    data = get_posts_all()
    return jsonify(data)


@api_blueprint.route('/posts/<pk>')
def api_post(pk):
    data = get_post_by_pk(pk)[0]
    return jsonify(data)
