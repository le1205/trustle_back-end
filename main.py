from flask import Flask
from flask_restful import Api
from views.test import PingView

app = Flask(__name__)
api = Api(app)

api.add_resource(PingView, '/ping')

if __name__ == '__main__':
    app.run(debug=True)