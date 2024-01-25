from pydantic import BaseModel


class UnsuccessfulRegisterData(BaseModel):
    email: str
