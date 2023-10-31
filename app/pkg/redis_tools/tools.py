""" Инструмент для более удобного взаимодействия с redis """

import redis


class RedisTools:
    """ Класс взаимодействия с redis """

    __redis_connect = redis.Redis(host='redis', port=6379)

    @classmethod
    def set_phone(cls, phone, address):
        """ Создает новую пару вида номер-адрес """

        cls.__redis_connect.set(phone, address)

    @classmethod
    def get_address(cls, phone):
        """ Возвращает адрес по номеру """

        return cls.__redis_connect.get(phone)

    @classmethod
    def get_data(cls):
        """ Возвращает все ключи (номера) """

        return cls.__redis_connect.keys(pattern='*')
