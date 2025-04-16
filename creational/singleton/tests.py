from .singleton import SingletonMeta, singleton_decorator


def test_metaclass_singleton():
    class SomeSingleton(metaclass=SingletonMeta):
        ...

    a = SomeSingleton()
    b = SomeSingleton()
    assert a is b


def test_decorator_singleton():

    @singleton_decorator
    class SomeSingleton:
        ...

    a = SomeSingleton()
    b = SomeSingleton()
    assert a is b
