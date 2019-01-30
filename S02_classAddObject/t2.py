"""
抽象基类

使用场景：
    1、在某些情况下希望判定某个对象的类型
    2、强制某个子类必须实现某些方法
"""

import abc


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set(self, key, value):
        pass

    @abc.abstractmethod
    def get(self, key):
        pass


# class CacheBase():
#     def get(self, key):
#         raise NotImplementedError
#
#     def set(self, key, value):
#         raise NotImplementedError


class RedisCache(CacheBase):
    def set(self, key, value):
        pass

    def get(self, key):
        pass


redis_chache = RedisCache()
redis_chache.set("k", "v")
