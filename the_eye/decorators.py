from functools import wraps

from flask import abort, request, make_response
from pydantic.error_wrappers import ValidationError


def validate_schema(input_model=None, output_model=None):
    def callable(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if input_model:
                    data = input_model(**request.get_json())
                    response, status = func(data, *args, **kwargs)
                else:
                    response, status = func(*args, **kwargs)
                if output_model:
                    return make_response(output_model(**response).dict(), status)
                else:
                    return make_response(response, status)
            except ValidationError as e:
                return make_response(f"Validation error - {e}", 400)

        return wrapped

    return callable
