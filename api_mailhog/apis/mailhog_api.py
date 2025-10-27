import requests


# http://5.63.153.31:5025

class MailhogApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers

    def get_api_v2_messages(self):
        """
        Get users emails
        :return:
        """
        params = {
            'limit': '50'
        }
        response = requests.get(
            url=f'{self.host}/api/v2/messages',
            params=params, verify=False
        )
        return response
