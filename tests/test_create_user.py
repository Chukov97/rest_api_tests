import allure
from api.user_api import user_api
from data.user_data import USER_DATA
from schemas.create_user_schema import create_user_schema


@allure.title("Создание юзера")
def test_create_user():
    user_api.create_user(USER_DATA.model_dump()).status_code_should_be(201).json_schema_should_be_valid(create_user_schema)


@allure.title('Валидация созданного юзера')
def test_create_user_valid():
    response = user_api.create_user(USER_DATA.model_dump())
    response.have_value_in_response_parameter('name', USER_DATA.name)
    response.have_value_in_response_parameter('job', USER_DATA.job)
