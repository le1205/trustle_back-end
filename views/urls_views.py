from flask.views import MethodView
from flask import request
from controllers.urls_controller import URLController

class CheckUserName(MethodView):
    def post(self):
        username = request.get_json().get('username')
        result = URLController.is_username_present(username)
        return result, 200