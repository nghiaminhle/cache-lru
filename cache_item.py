class CacheItem:
    next_item = None
    previous_item = None
    key = None
    value = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

