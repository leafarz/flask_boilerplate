from functools import wraps

from flask import request


def parse_request(serializer):
    """
    Decorator to parse incoming request data.

    Args:
        serializer: Serializer to use after obtaining the data
    
    Returns:
        req_data: The parsed json
    """
    def decorator(f):
        @wraps(f)
        def wrapper(self, *args, **kwargs):
            switch={
                "application/json": lambda: request.get_json(),
                "application/x-www-form-urlencoded": lambda: {k:request.form[k] for k in request.form.keys()}
            }
            if request.content_type in switch:
                req_data=serializer.dump(switch[request.content_type]())
            else:
                abort(415, "Content type not supported")

            return f(self, req_data, *args, **kwargs)
        return wrapper
    return decorator
