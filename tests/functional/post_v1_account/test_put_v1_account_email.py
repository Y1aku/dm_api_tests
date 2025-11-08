import random
from helpers.account_helper import AccountHelper
from restclient.configuration import Configuration as MailhogConfiguration
from restclient.configuration import Configuration as DmApiConfiguration
from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi


def test_put_v1_account_email():
    mailhog_configuration = MailhogConfiguration(host='http://5.63.153.31:5025')
    dm_api_configuration = DmApiConfiguration(host='http://5.63.153.31:5051', disable_log=False)

    account = DMApiAccount(configuration=dm_api_configuration)
    mailhog = MailHogApi(configuration=mailhog_configuration)

    account_helper = AccountHelper(dm_account_api=account, mailhog=mailhog)

    id = int(random.random() * 10000000000000000)
    name = "arbuzz"
    login = f"{name}{id}"
    email = f"{login}@mail.ru"
    password = '123456789'

    # Регистрация нового пользователя
    account_helper.register_new_user(login=login, password=password, email=email)

    # Авторизация пользователя
    account_helper.user_login(login=login, password=password, expected_code=200)

    id = int(random.random() * 10000000000000000)
    email = f"{name}{id}@mail.ru"

    # Меняем email
    account_helper.change_user_email(login=login, password=password, email=email)

    # Авторизуемся с новой неподтвержденной почтой (403)
    account_helper.user_login(login=login, password=password, expected_code=403)

    # Активировать пользователя сменившего почту
    account_helper.activate_changing_mail_token(login=login)

    # Авторизация пользователя
    account_helper.user_login(login=login, password=password, expected_code=200)
