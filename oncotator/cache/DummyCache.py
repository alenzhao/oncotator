from oncotator.cache.Cache import Cache


class DummyCache(Cache):
    """Everything is a cache miss.  Ignores attempts to store new keys."""
    def __init__(self):
        pass

    def retrieve_from_cache(self, key):
        return None

    def store_into_cache(self, key, value):
        pass

    def close_cache(self):
        pass