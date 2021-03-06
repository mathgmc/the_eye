from functools import wraps
import logging
from flask import request, make_response
from werkzeug.exceptions import Unauthorized
from pydantic.error_wrappers import ValidationError

from the_eye.models import Partner


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
                logging.error(
                    f"Validation error - {e}; For envent: {request.get_json()}"
                )
                return make_response(f"Validation error - {e}", 400)

        return wrapped

    return callable


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if "Authorization" in request.headers:
            token = request.headers["Authorization"]
            partner = Partner.get_partner(token)

            if not partner:
                raise Unauthorized("You need a valid token to access this route")
            if partner == -1:
                raise Unauthorized("Error trying to query your token")

            return f(partner, *args, **kws)

        raise Unauthorized("You need a valid token to access this route")

    return decorated_function
