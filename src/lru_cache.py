from collections import OrderedDict


class LRUCache:
    """Fixed-capacity cache that evicts the least-recently-used entry
    once it grows beyond capacity. Backed by OrderedDict for O(1)
    get/put with recency tracking."""

    def __init__(self, capacity: int):
        """Create a cache that holds at most `capacity` entries."""
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self._data: OrderedDict = OrderedDict()

    def get(self, key):
        """Return the value for `key`, or -1 if absent. Marks the
        key as most recently used."""
        if key not in self._data:
            return -1
        self._data.move_to_end(key)
        return self._data[key]

    def put(self, key, value) -> None:
        """Insert or update `key` with `value`, marking it as most
        recently used. Evicts the least-recently-used entry if the
        cache exceeds capacity."""
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        if len(self._data) > self.capacity:
            self._data.popitem(last=False)
