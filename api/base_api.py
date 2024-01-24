import allure
import requests


class Api:
    """Основной класс для работы с API"""
    _URL = 'https://reqres.in'
    _TIMEOUT = 10

    def __init__(self):
        self.response = None

    # METHODS API

    @allure.step("Отправить POST-запрос")
    def post(self, url: str, endpoint: str, params: dict = None,
             json_body: dict = None, headers: dict = None):
        with allure.step(f"POST-запрос на url: {url}{endpoint}"
                         f"\n тело запроса: \n {json_body}"):
            self.response = requests.post(url=f"{url}{endpoint}",
                                          headers=headers,
                                          params=params,
                                          json=json_body,
                                          timeout=self._TIMEOUT)

        return self

    @allure.step("Отправить GET-запрос")
    def get(self, url: str, endpoint: str, params: dict = None, headers: dict = None):
        with allure.step(f"GET запрос на url: {url}{endpoint}"):
            self.response = requests.get(url=f"{url}{endpoint}",
                                         headers=headers,
                                         params=params)

        return self

    @allure.step("Отправить PUT запрос")
    def put(self, url: str, endpoint: str, params: dict = None, json_body: dict = None, headers: dict = None):
        with allure.step(f"PUT запрос на url: {url}{endpoint}"
                         f"\n тело запроса: \n {json_body}"):
            self.response = requests.put(url=f"{url}{endpoint}",
                                         headers=headers,
                                         params=params,
                                         json=json_body,
                                         timeout=self._TIMEOUT)

        return self

    @allure.step("Отправить DELETE запрос")
    def delete(self, url: str, endpoint: str, headers: dict = None):
        with allure.step(f"DELETE запрос на url: {url}{endpoint}"):
            self.response = requests.delete(url=f"{url}{endpoint}",
                                            headers=headers,
                                            timeout=self._TIMEOUT)
        return self

        # ASSERTIONS:

    @allure.step("Статус код ответа равен {expected_code}")
    def status_code_should_be(self, expected_code: int):
        """Проверяем статус код ответа actual_code на соответствие expected_code"""
        actual_code = self.response.status_code
        assert expected_code == actual_code, f"\nОжидаемый результат: {expected_code} " \
                                             f"\nФактический результат: {actual_code}"
        return self
