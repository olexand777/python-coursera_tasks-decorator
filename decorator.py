import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapper


@to_json
def get_data():
    return {
        'data': 42
    }


print(type(get_data()))
