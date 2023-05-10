from services.url_service import URLService

class URLController:
    @staticmethod
    def is_username_present(username):
        return URLService.is_username_present(username)