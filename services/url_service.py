import httpx
from concurrent.futures import ThreadPoolExecutor
from httpx import ConnectTimeout, ReadTimeout
from data.urls import URL

class URLService:
    @staticmethod
    def check_url(site, username, result_list):
        url = site.replace('@username', username)
        try:
            with httpx.Client(timeout=(5,14)) as client:
                response = client.get(url)
                if response.status_code == 200:
                    result_list.append({url: True})
                else: 
                    result_list.append({site: False})
        except (ConnectTimeout, ReadTimeout):
            print('Request time out: ', url)
            result_list.append({site: None})
        except Exception as e:
            print('Request error: ',str(e), url)
            result_list.append({site: None})

    @staticmethod
    def is_username_present(username):
        resutl_list = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(lambda site: URLService.check_url(site, username, resutl_list), URL)
        
        return resutl_list