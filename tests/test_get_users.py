import allure
from api.user_api import user_api


@allure.title("Получение списка юзеров")
def test_get_users_list():
    user_api.get_list_user().status_code_should_be(200)

