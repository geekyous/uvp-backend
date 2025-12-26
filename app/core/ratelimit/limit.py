import app.core.cache as cache


async def allow_request(key: str, limit: int, window: int) -> bool:
    """

    :param key:
    :param limit:
    :param window:
    :return:
    """
    current = await cache.redis_client.incr(key)
    if current == 1:
        await cache.redis_client.expire(key, window)
    return current <= limit
