from api.app import app
from api.app import db

from posts.blueprint import posts

import view

app.register_blueprint(posts, url_prefix = "/blog")


if __name__ == "__main__":
    app.run()