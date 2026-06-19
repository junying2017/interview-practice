import pytest

from src.lru_cache import LRUCache


def test_get_missing_key_returns_minus_one():
    cache = LRUCache(2)
    assert cache.get("a") == -1


def test_put_and_get():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    assert cache.get("b") == 2


def test_evicts_least_recently_used():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)  # evicts "a"
    assert cache.get("a") == -1
    assert cache.get("b") == 2
    assert cache.get("c") == 3


def test_get_refreshes_recency():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.get("a")  # "a" is now most recently used
    cache.put("c", 3)  # evicts "b" instead of "a"
    assert cache.get("a") == 1
    assert cache.get("b") == -1
    assert cache.get("c") == 3


def test_put_updates_existing_key():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("a", 100)
    assert cache.get("a") == 100


def test_invalid_capacity_raises():
    with pytest.raises(ValueError):
        LRUCache(0)
