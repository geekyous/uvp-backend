import uuid
from _datetime import datetime


def gen_id():
    """生成唯一ID"""
    return uuid.uuid4().hex


def now():
    return datetime.now()
