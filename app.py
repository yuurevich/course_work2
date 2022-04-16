from flask import Flask
from bookmarks.bookmarks import bookmarks_blueprint
from main.main import main_blueprint
from api.api import api_blueprint

app = Flask(__name__)

app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)

app.config['JSON_AS_ASCII'] = False


if __name__ == "__main__":
    app.run(debug=True)
