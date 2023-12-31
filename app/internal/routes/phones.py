from fastapi import APIRouter, Query
from app.pkg.redis_tools.tools import RedisTools
from app.internal.schemas.phone_address import Phone

router = APIRouter(
    prefix='/api/v1'
)


def is_exist(phone: str):
    """
    Проверка наличия номера в списке уже имеющихся

    Возвращает ошибку или True
    """

    if phone not in [s.decode('utf-8') for s in RedisTools.get_data()]:

        return {
            'error': 'Phone doesn\'t exist...'
        }

    return True


@router.get('/get_all')
def get_all():

    return RedisTools.get_data()


@router.get('/check_data')
def get_address(phone: str):

    if is_exist(phone):

        return {
            'address': RedisTools.get_address(phone)
        }


@router.post('/write_data')
def write_data(phone: str, address: str):

    RedisTools.set_phone(phone, address)

    return {
        'success': "Done!"
    }


@router.patch('/write_data')
def update_data(phone: str, address:str):

    if is_exist(phone):

        RedisTools.set_phone(phone, address)

        return {
            'success': 'Address has been updated'
        }
