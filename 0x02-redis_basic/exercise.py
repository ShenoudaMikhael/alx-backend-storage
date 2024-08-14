import redis


class Cache:
    def __init__():

        r = redis.Redis()
        print(r.ping())
