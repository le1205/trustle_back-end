from flask import Flask
from flask_restful import Api
from views.test import PingView
from views.urls_views import CheckUserName

app = Flask(__name__)
api = Api(app)

api.add_resource(PingView, '/ping')
api.add_resource(CheckUserName, '/urls')

if __name__ == '__main__':
    app.run(debug=True)