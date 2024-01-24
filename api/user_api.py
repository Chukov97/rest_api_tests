import allure

from api.base_api import Api


class UserApi(Api):
    """ENDPOINT"""
    _ENDPOINT_USER = '/api/users/'

    @allure.step('Получение списка юзеров')
    def get_list_user(self):
        return self.get(url=Api._URL, endpoint=self._ENDPOINT_USER)


user_api = UserApi()
