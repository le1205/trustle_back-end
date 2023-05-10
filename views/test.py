from flask.views import MethodView

class PingView(MethodView):
    def get(self):
        return {'response': 'pong!'}, 200