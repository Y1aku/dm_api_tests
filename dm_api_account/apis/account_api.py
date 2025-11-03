import requests
from restclient.client import RestClient
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=True,
            sort_keys=True
        )
    ]
)


class AccountApi(RestClient):

    def post_v1_account(self, json_data):
        """
        Register new user
        :param json_data:
        :return:
        """
        response = self.post(
            path='/v1/account',
            json=json_data
        )
        return response

    def put_v1_account_token(self, token):
        """
        Activate registred user
        :param token:
        :return:
        """
        headers = {
            'accept': 'text/plain'
        }
        response = self.put(
            path=f'/v1/account/{token}',
            headers=headers
        )
        return response

    def put_v1_account_change_email(self, json_data):
        """
        Change registered user email
        :param json_data:
        :return:
        """
        headers = {
            'accept': 'text/plain',
            'Content-Type': 'application/json',
        }
        response = requests.put(
            url=f'{self.host}/v1/account/email',
            headers=headers,
            json=json_data
        )
        return response
