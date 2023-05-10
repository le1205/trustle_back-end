from flask.views import MethodView
from flask import request, jsonify
from services.name_generator import Generator

name_generator = Generator()


class FetchLinks(MethodView):
    def post(self):
        username = request.get_json().get('username')
        separators = request.get_json().get('separators')
        print(separators)
        result = name_generator.GenerateUserNamesAndFetch(username, separators)
        return result, 200
