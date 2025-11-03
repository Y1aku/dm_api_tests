import requests
from restclient.client import RestClient


# http://5.63.153.31:5025

class MailhogApi(RestClient):

    def get_api_v2_messages(self):
        """
        Get users emails
        :return:
        """
        params = {
            'limit': '50'
        }
        response = self.get(
            path='/api/v2/messages',
            params=params, verify=False
        )
        return response
