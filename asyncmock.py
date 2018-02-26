import functools
import asyncio

__all__ = ['asyncmock']


class AsyncMock:
    result = {}

    def __init__(self, instance):
        if instance is None:
            raise RuntimeError("Unable to continue without instance.")

        self.instance = instance

    def set_result(self, method_name, result):
        AsyncMock.result[method_name] = result
        async def mocked_method(self, result):
            response = await AsyncMock.get_result(method_name)
            return response
        mocked_method.__doc__ = "this is a mocked object"
        mocked_method.__name__ = method_name
        setattr(self.instance.__class__, mocked_method.__name__, mocked_method)

    @staticmethod
    async def get_result(method_name):
        return AsyncMock.result[method_name]
