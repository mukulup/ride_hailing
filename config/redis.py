# config/redis.py
import redis
from config.settings import settings

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True
)


def get_redis() -> redis.Redis:
    """Dependency for injecting redis client if needed in future"""
    return redis_client