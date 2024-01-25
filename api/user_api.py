import allure

from api.base_api import Api


class UserApi(Api):
    """ENDPOINT"""
    _ENDPOINT_USER = '/api/users/'
    _ENDPOINT_REGISTER_USER = '/api/register'

    @allure.step('Получение списка юзеров')
    def get_list_user(self):
        return self.get(url=Api._URL, endpoint=self._ENDPOINT_USER)

    @allure.step('Получение юзера по id')
    def get_user_by_id(self, id_user: str):
        return self.get(url=Api._URL, endpoint=self._ENDPOINT_USER + id_user)

    @allure.step('Создание юзера')
    def create_user(self, param_request_body):
        return self.post(url=Api._URL, endpoint=self._ENDPOINT_USER, json_body=param_request_body)

    @allure.step('Удаление юзера')
    def delete_user(self, id_user: str):
        return self.delete(url=Api._URL, endpoint=self._ENDPOINT_USER + id_user)

    @allure.step('Неудачная регистрация')
    def unsuccessful_register(self, param_request_body):
        return self.post(url=Api._URL, endpoint=self._ENDPOINT_REGISTER_USER, json_body=param_request_body)

        # ASSERTIONS:

    @allure.step('Проверка длины списка юзеров')
    def check_len_user_list(self, len_list):
        actual_len = len(self.response.json()['data'])
        assert len_list == actual_len


user_api = UserApi()
