import config

from flask_cors import CORS
from flask import Flask

app = Flask(__name__)

CORS(app, supports_credentials=True)


@app.route('/', methods=['GET'])
def healthcheck():
    return "Working"


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=False)
    
