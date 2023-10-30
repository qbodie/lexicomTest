import redis


class RedisTools:

    __redis_connect = redis.Redis(host='redis', port=6379)

    @classmethod
    def set_phone(cls, phone, address):

        cls.__redis_connect.set(phone, address)

    @classmethod
    def get_address(cls, phone):

        return cls.__redis_connect.get(phone)

    @classmethod
    def get_data(cls):

        return cls.__redis_connect.keys(pattern='*')
