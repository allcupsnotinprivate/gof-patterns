# Use Case: In-Memory Cache Manager (Singleton)
#
# This class represents a shared in-memory cache that is accessed
# from different parts of an application. Using the Singleton pattern
# ensures that only one instance of the cache exists during runtime.
#
# Benefits:
# - Shared data access: all components interact with the same cache.
# - Prevents duplication: avoids multiple cache instances and conflicting values.
# - Optimized memory usage and data consistency.
#
# Common usage scenarios:
# - Caching API responses or expensive computations.
# - Storing session/state data in web or CLI applications.
# - Sharing data between loosely coupled modules.

from singleton import SingletonMeta


class Cache(metaclass=SingletonMeta):

    def __init__(self):
        self.store = {}

    def set(self, key, value):
        self.store[key] = value

    def get(self, key):
        return self.store.get(key)


if __name__ == "__main__":
    cache1 = Cache()
    cache1.set("foo", "Bar")

    cache2 = Cache()
    print(cache2.get("foo"))
