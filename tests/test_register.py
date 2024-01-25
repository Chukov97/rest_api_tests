import allure
from api.user_api import user_api
from data.register_data import UNSUCCESSFUL_REGISTER_DATA
from schemas.register_schema import unsuccessful_register_schema


@allure.title("Неудачная регистрация")
def test_unsuccessful_register():
    user_api.unsuccessful_register(UNSUCCESSFUL_REGISTER_DATA.model_dump()).status_code_should_be(
        400).json_schema_should_be_valid(unsuccessful_register_schema)


@allure.title("Проверка текста ошибки при неудачной регистрации")
def test_unsuccessful_register_validate_error():
    user_api.unsuccessful_register(UNSUCCESSFUL_REGISTER_DATA.model_dump()).have_value_in_response_parameter('error',
                                                                                                       'Missing password')
