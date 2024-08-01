import config

from flask_cors import CORS
from flask import Flask
from src.routes.users_route import user_blueprint
from src.db import init_db

init_db()

app = Flask(__name__)


app.register_blueprint(user_blueprint)

CORS(app, supports_credentials=True)


@app.route('/', methods=['GET'])
def healthcheck():
    return "Working"


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=False)

