import random
from dm_api_account.apis.account_api import AccountApi
from restclient.configuration import Configuration as DmApiConfiguration


def test_post_v1_account():
    dm_api_configuration = DmApiConfiguration(host='http://5.63.153.31:5051', disable_log=False)
    account_api = AccountApi(configuration=dm_api_configuration)

    # Регистрация нового пользователя
    login = f"arbuzz{int(random.random() * 10000000000000000)}"
    email = f"{login}@mail.ru"
    password = '123456789'

    json_data = {
        'login': login,
        'email': email,
        'password': password,
    }

    response = account_api.post_v1_account(json_data=json_data)
    assert response.status_code == 201, f"Пользователь не был создан {response.json()}"
