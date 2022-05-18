import logging
import threading

from the_eye.models import Event, Partner


class AddEventHandler(threading.Thread):
    def __init__(self, event: dict, partner: Partner):
        self._event = event
        self._partner = partner
        threading.Thread.__init__(self)

    def _create_event_response_handler(self, code: int):
        code_handler = {
            201: lambda x: x,  # Should not do anything
            400: lambda x: logging.error(f"Data Error while creating event: {x}"),
            500: lambda x: logging.error(f"Unexpected error while creating event: {x}"),
        }
        try:
            code_handler[code](self._event)
        except KeyError:
            logging.error(
                f"Unexpected key error {code} while creating event: {self._event.dict()}"
            )

    def run(self):
        code = Event.create_event(**self._event, partner_id=self._partner.id)
        self._create_event_response_handler(code)
