import app.core.cache as cache
import hashlib


async def is_feature_enabled(feature: str, ak: str):
    """
    Feature Flag 启用判断
    :param feature: 特征标识
    :param ak: ak
    :return: True:
    """
    enabled = await cache.redis_client.get(f"feature:{feature}:enabled")
    if enabled != "true":
        return False

    # 白名单优先
    if await cache.redis_client.sismember(
            f"feature:{feature}:whitelist",
            ak):
        return True
    ratio = int(await cache.redis_client.get(f"feature:{feature}:ratio") or 0)
    if ratio <= 0:
        return False
    h = int(hashlib.md5(ak.encode()).hexdigest(), 16) % 10
    return h % 100 < ratio
