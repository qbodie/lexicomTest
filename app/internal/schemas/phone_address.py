from pydantic import BaseModel, field_validator


class Phone(BaseModel):
    """ Валидирует номер телефона, который присылает пользователь """

    phone: str

    @field_validator('phone')
    def is_correct(cls, v: str) -> str:

        if len(v) != 10:
            raise ValueError('That\'s incorrect number')
        else:
            return v
