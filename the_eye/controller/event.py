import logging
import threading
from time import sleep

from the_eye.model.event import Event


class AddEventhandler(threading.Thread):
    def __init__(self, event: dict):
        self._event = event
        threading.Thread.__init__(self)

    def _create_event_response_handler(self, code):
        code_handler = {
            201: lambda x: x,  # Should not do anything
            400: lambda x: logging.warning(f"Data Error while creating event: {x}"),
            500: lambda x: logging.warning(
                f"Unexpected error while creating event: {x}"
            ),
        }
        try:
            code_handler[code](self._event)
        except KeyError:
            logging.warning(
                f"Unexpected key error {code} while creating event: {self._event.dict()}"
            )

    def run(self):
        code = Event.create_event(**self._event)
        self._create_event_response_handler(code)
