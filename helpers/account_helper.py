from json import loads
from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi


class AccountHelper:
    def __init__(self, dm_account_api: DMApiAccount, mailhog: MailHogApi):
        self.dm_account_api = dm_account_api
        self.mailhog = mailhog

    def register_new_user(self, login: str, password: str, email: str):
        json_data = {
            'login': login,
            'email': email,
            'password': password
        }

        # Регистрация нового пользователя
        response = self.dm_account_api.account_api.post_v1_account(json_data=json_data)
        assert response.status_code == 201, f"Пользователь не был создан {response.json()}"

        # Получить активационный токен
        token = self.get_activation_token_by_login(login=login)

        # Активация зарегистрированного пользователя
        response = self.activate_token(token=token)

        return response

    def user_login(self, login: str, password: str, expected_code: int, remember_me: bool = True):
        json_data = {
            'login': login,
            'password': password,
            'rememberMe': remember_me
        }

        status_messages = {
            200: "Пользователь не смог авторизоваться",
            403: "Ожидалась ошибка авторизации"
        }

        # Авторизация пользователя
        response = self.dm_account_api.login_api.post_v1_account_login(json_data=json_data)
        message = status_messages.get(expected_code)
        assert response.status_code == expected_code, message

        return response

    def change_user_email(self, login: str, password: str, email: str):
        json_data = {
            'login': login,
            'password': password,
            'email': email
        }

        # Меняем email
        response = self.dm_account_api.account_api.put_v1_account_change_email(json_data=json_data)
        assert response.status_code == 200, "Пользователь не смог поменять email"

        return response

    def activate_token(self, token: str):

        # Активировать токен
        response = self.dm_account_api.account_api.put_v1_account_token(token=token)
        assert response.status_code == 200, "Пользователь не активирован"

        return response

    def get_activation_token_by_login(self, login: str):

        # Получить письма из почтового ящика
        response = self.mailhog.mailhog_api.get_api_v2_messages()
        assert response.status_code == 200, f"Письма не были получены"

        token = None
        for item in response.json()['items']:
            user_data = loads(item['Content']['Body'])
            user_login = user_data['Login']
            if user_login == login:
                token = user_data['ConfirmationLinkUrl'].split('/')[-1]
        assert token is not None, f"Токен для пользователя {login} не был получен"

        return token
