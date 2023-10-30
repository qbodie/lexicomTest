from pydantic import BaseModel, field_validator


class PhoneAddress(BaseModel):

    phone: int
    address: str

    @field_validator('phone')
    def is_correct(cls, v: int) -> int:

        if len(v) != 10:
            raise ValueError('That\'s incorrect number')
        else:
            return v
